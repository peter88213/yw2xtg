"""Class for XPress tagged file processing. 

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
import os
import re
from string import Template

from pywriter.file.file_export import FileExport


class XtgFile(FileExport):
    """XPress tagged file representation
    """

    DESCRIPTION = 'XPress tagged file'
    EXTENSION = '.XTG'
    SUFFIX = ''

    def __init__(self, filePath, **kwargs):
        FileExport.__init__(self, filePath)

        self.fileHeader = kwargs['fileHeader']
        self.partTemplate = kwargs['partTemplate']
        self.chapterTemplate = kwargs['chapterTemplate']
        self.firstSceneTemplate = kwargs['firstSceneTemplate']
        self.sceneTemplate = kwargs['sceneTemplate']
        self.appendedSceneTemplate = kwargs['appendedSceneTemplate']
        self.sceneDivider = kwargs['sceneDivider']

        self.tagTextBody = kwargs['textBody']
        self.tagItalic = kwargs['italic']
        self.tagItalic0 = kwargs['italic0']
        self.tagBold = kwargs['bold']
        self.tagBold0 = kwargs['bold0']
        self.tagAcronym = kwargs['acronym']
        self.tagAcronym0 = kwargs['acronym0']
        self.tagFigure = kwargs['figure']
        self.tagFigure0 = kwargs['figure0']

        self.adjust_digits = kwargs['adjust_digits']
        self.space_points = kwargs['space_points']
        self.per_chapter = kwargs['per_chapter']

    def convert_from_yw(self, text):
        """Convert yw7 markup to Markdown.
        """
        if text is None:
            return ''

        XTG_REPLACEMENTS = [
            #--- Escape XPress Tags code-specific characters.
            ['@', '┌┐@>'],
            ['<', '┌┐<>'],
            ['\\', '┌┐\\>'],
            ['┌┐', '<\\'],
            #--- Replace yWriter tags with XPress tags.
            ['[i]', self.tagItalic],
            ['[/i]', self.tagItalic0],
            ['[b]', self.tagBold],
            ['[/b]', self.tagBold0],
            ['  ', ' '],
        ]

        try:

            for r in XTG_REPLACEMENTS:
                text = text.replace(r[0], r[1])

        except AttributeError:
            return ''

        #--- Encode non-breaking spaces.

        text = text.replace('\xa0', '<\\!p>')

        #--- Remove highlighting, alignment,
        # strikethrough, and underline tags.

        text = re.sub('\[\/*[h|c|r|s|u]\d*\]', '', text)

        #--- Remove comments.

        text = re.sub('\/\*.+?\*\/', '', text)

        #--- Adjust digit-separating blanks.

        if self.adjust_digits:
            text = re.sub('(\d) (\d)', '\\1<\\![>\\2', text)

        #--- Space digit-separating points.

        if self.space_points:
            text = re.sub('(\d+)\.', '\\1.<\\![>', text)
            text = text.replace('<\\![> ', ' ')

        #--- Assign "figure" style.

        text = re.sub('(\d+)', self.tagFigure + '\\1' + self.tagFigure0, text)

        #--- Assign "acronym" style.

        text = re.sub('([A-ZÄ-Ü]{2,})', self.tagAcronym +
                      '\\1' + self.tagAcronym0, text)

        #--- Assign the second paragraph "textBody" style.

        t = text.split('\n', 1)
        text = ('\n' + self.tagTextBody).join(t)

        return text

    def get_chapterMapping(self, chId, chapterNumber):
        """Return a mapping dictionary for a chapter section. 
        """

        ROMAN = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        def number_to_roman(n):
            """Return n as a Roman number.
            Credit goes to the user 'Aristide' on stack overflow.
            https://stackoverflow.com/a/47713392
            """

            result = []

            for (arabic, roman) in ROMAN:
                (factor, n) = divmod(n, arabic)
                result.append(roman * factor)

                if n == 0:
                    break

            return "".join(result)

        TENS = {30: 'thirty', 40: 'forty', 50: 'fifty',
                60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
        ZERO_TO_TWENTY = (
            'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
        )

        def number_to_english(n):
            """Return n as a number written out in English.
            Credit goes to the user 'Hunter_71' on stack overflow.
            https://stackoverflow.com/a/51849443
            """

            if any(not x.isdigit() for x in str(n)):
                return ''

            if n <= 20:
                return ZERO_TO_TWENTY[n]

            elif n < 100 and n % 10 == 0:
                return TENS[n]

            elif n < 100:
                return number_to_english(n - (n % 10)) + ' ' + number_to_english(n % 10)

            elif n < 1000 and n % 100 == 0:
                return number_to_english(n / 100) + ' hundred'

            elif n < 1000:
                return number_to_english(n / 100) + ' hundred ' + number_to_english(n % 100)

            elif n < 1000000:
                return number_to_english(n / 1000) + ' thousand ' + number_to_english(n % 1000)

            return ''

        chapterMapping = FileExport.get_chapterMapping(
            self, chId, chapterNumber)

        if chapterNumber:
            chapterMapping['ChNumberEnglish'] = number_to_english(
                chapterNumber).capitalize()
            chapterMapping['ChNumberRoman'] = number_to_roman(chapterNumber)

        else:
            chapterMapping['ChNumberEnglish'] = ''
            chapterMapping['ChNumberRoman'] = ''

        if self.chapters[chId].suppressChapterTitle:
            chapterMapping['Title'] = ''

        return chapterMapping

    def get_chapters(self):
        """Process the chapters and nested scenes.
        Return a list of strings, or a message, depending on 
        the per_chapter variable.
        Extend the superclass method for the 'document per chapter'
        option.
        """

        if not self.per_chapter:
            return FileExport.get_chapters(self)

        projectDir = os.path.dirname(self.filePath)

        if projectDir == '':
            projectDir = '.'

        chapterNumber = 0
        sceneNumber = 0
        wordsTotal = 0
        lettersTotal = 0

        for chId in self.srtChapters:
            lines = []

            dispNumber = 0

            if not self.chapterFilter.accept(self, chId):
                continue

            # The order counts; be aware that "Todo" and "Notes" chapters are
            # always unused.

            # Has the chapter only scenes not to be exported?

            sceneCount = 0
            notExportCount = 0
            doNotExport = False
            template = None

            for scId in self.chapters[chId].srtScenes:
                sceneCount += 1

                if self.scenes[scId].doNotExport:
                    notExportCount += 1

            if sceneCount > 0 and notExportCount == sceneCount:
                doNotExport = True

            if self.chapters[chId].chType == 2:
                # Chapter is "ToDo" type (implies "unused").

                if self.todoChapterTemplate != '':
                    template = Template(self.todoChapterTemplate)

            elif self.chapters[chId].chType == 1:
                # Chapter is "Notes" type (implies "unused").

                if self.notesChapterTemplate != '':
                    template = Template(self.notesChapterTemplate)

            elif self.chapters[chId].isUnused:
                # Chapter is "really" unused.

                if self.unusedChapterTemplate != '':
                    template = Template(self.unusedChapterTemplate)

            elif self.chapters[chId].oldType == 1:
                # Chapter is "Info" type (old file format).

                if self.notesChapterTemplate != '':
                    template = Template(self.notesChapterTemplate)

            elif doNotExport:

                if self.notExportedChapterTemplate != '':
                    template = Template(self.notExportedChapterTemplate)

            elif self.chapters[chId].chLevel == 1 and self.partTemplate != '':
                template = Template(self.partTemplate)

            else:
                template = Template(self.chapterTemplate)
                chapterNumber += 1
                dispNumber = chapterNumber

            if template is not None:
                lines.append(template.safe_substitute(
                    self.get_chapterMapping(chId, dispNumber)))

            # Process scenes.

            sceneLines, sceneNumber, wordsTotal, lettersTotal = self.get_scenes(
                chId, sceneNumber, wordsTotal, lettersTotal, doNotExport)
            lines.extend(sceneLines)

            # Process chapter ending.

            template = None

            if self.chapters[chId].chType == 2:

                if self.todoChapterEndTemplate != '':
                    template = Template(self.todoChapterEndTemplate)

            elif self.chapters[chId].chType == 1:

                if self.notesChapterEndTemplate != '':
                    template = Template(self.notesChapterEndTemplate)

            elif self.chapters[chId].isUnused:

                if self.unusedChapterEndTemplate != '':
                    template = Template(self.unusedChapterEndTemplate)

            elif self.chapters[chId].oldType == 1:

                if self.notesChapterEndTemplate != '':
                    template = Template(self.notesChapterEndTemplate)

            elif doNotExport:

                if self.notExportedChapterEndTemplate != '':
                    template = Template(self.notExportedChapterEndTemplate)

            elif self.chapterEndTemplate != '':
                template = Template(self.chapterEndTemplate)

            if template is not None:
                lines.append(template.safe_substitute(
                    self.get_chapterMapping(chId, dispNumber)))

            if lines == []:
                continue

            text = self.fileHeader + ''.join(lines)

            filePath = projectDir + '/' + \
                str(dispNumber).zfill(4) + '_' + \
                self.chapters[chId].title + self.EXTENSION

            try:
                with open(filePath, 'w', encoding='utf-8') as f:
                    f.write(text)

            except:
                return('ERROR: Cannot write "' +
                       os.path.normpath(filePath) + '".')

        return 'SUCCESS: All chapters written.'

    def write(self):
        """Create a template-based output file. 
        Return a message string starting with 'SUCCESS' or 'ERROR'.
        Extend the superclass method for the 'document per chapter'
        option.
        """
        if self.per_chapter:
            return self.get_chapters()

        else:
            return FileExport.write(self)
