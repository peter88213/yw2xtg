"""Provide a class for XPress tagged file processing. 

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import shutil
import os
import re
from string import Template

from pywriter.pywriter_globals import ERROR
from pywriter.file.file_export import FileExport


class XtgFile(FileExport):
    """XPress tagged file representation.
    """

    DESCRIPTION = 'XPress tagged file'
    EXTENSION = '.XTG'
    SUFFIX = ''
    _XTG_OUT = 'XTG_Chapters'

    def __init__(self, filePath, **kwargs):
        super().__init__(filePath)

        self._fileHeader = kwargs['file_header']
        self._partTemplate = kwargs['part_template']
        self._chapterTemplate = kwargs['chapter_template']
        self._firstSceneTemplate = kwargs['first_scene_template']
        self._sceneTemplate = kwargs['scene_template']
        self._appendedSceneTemplate = kwargs['appended_scene_template']
        self._sceneDivider = kwargs['scene_divider']

        self._tagFirstParagraph = kwargs['first_paragraph']
        self._tagIndentedParagraph = kwargs['indented_paragraph']
        self._tagOtherParagraph = kwargs['other_paragraph']
        self._tagItalic = kwargs['italic']
        self._tagItalic0 = kwargs['italic0']
        self._tagBold = kwargs['bold']
        self._tagBold0 = kwargs['bold0']
        self._tagAcronym = kwargs['acronym']
        self._tagAcronym0 = kwargs['acronym0']
        self._tagFigure = kwargs['figure']
        self._tagFigure0 = kwargs['figure0']

        self._adjustDigits = kwargs['adjust_digits']
        self._spacePoints = kwargs['space_points']
        self._perChapter = kwargs['per_chapter']

    def _convert_from_yw(self, text, quick=False):
        """Convert yw7 markup to Markdown.
        """
        XTG_REPLACEMENTS = [
            # Escape XPress Tags code-specific characters.
            ('@', '┌┐@>'),
            ('<', '┌┐<>'),
            ('\\', '┌┐\\>'),
            ('┌┐', '<\\'),
        ]
        
        if quick:
            # Just clean up a one-liner without sophisticated formatting.
            
            try:
    
                for yw, xt in XTG_REPLACEMENTS:
                    text = text.replace(yw, xt)
                    
                return text
    
            except AttributeError:
                return ''
                        
        XTG_REPLACEMENTS.extend([
            # Replace yWriter tags with XPress tags.
            ('[i]', self._tagItalic),
            ('[/i]', self._tagItalic0),
            ('[b]', self._tagBold),
            ('[/b]', self._tagBold0),
            ('  ', ' '),
            # Format paragraphs.
            ('\n\n', f'\r\r{self._tagFirstParagraph}'),
            ('\n', f'\n{self._tagOtherParagraph}'),
            ('\r', '\n'),
        ])

        try:

            for yw, xt in XTG_REPLACEMENTS:
                text = text.replace(yw, xt)

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

        if self._adjustDigits:
            text = re.sub('(\d) (\d)', '\\1<\\![>\\2', text)

        #--- Space digit-separating points.

        if self._spacePoints:
            text = re.sub('(\d+)\.', '\\1.<\\![>', text)
            text = text.replace('<\\![> ', ' ')

        #--- Assign "figure" style.

        text = re.sub('(\d+)', f'{self._tagFigure}\\1{self._tagFigure0}', text)

        #--- Assign "acronym" style.

        text = re.sub('([A-ZÄ-Ü]{2,})', f'{self._tagAcronym}\\1{self._tagAcronym0}', text)

        return text

    def _get_chapterMapping(self, chId, chapterNumber):
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
                return f'{number_to_english(n - (n % 10))} {number_to_english(n % 10)}'

            elif n < 1000 and n % 100 == 0:
                return f'{number_to_english(n / 100)} hundred'

            elif n < 1000:
                return f'{number_to_english(n / 100)} hundred {number_to_english(n % 100)}'

            elif n < 1000000:
                return f'{number_to_english(n / 1000)} thousand {number_to_english(n % 1000)}'

            return ''

        chapterMapping = super()._get_chapterMapping(chId, chapterNumber)

        if chapterNumber:
            chapterMapping['ChNumberEnglish'] = number_to_english(chapterNumber).capitalize()
            chapterMapping['ChNumberRoman'] = number_to_roman(chapterNumber)

        else:
            chapterMapping['ChNumberEnglish'] = ''
            chapterMapping['ChNumberRoman'] = ''

        if self.chapters[chId].suppressChapterTitle:
            chapterMapping['Title'] = ''

        return chapterMapping

    def _get_chapters(self):
        """Process the chapters and nested scenes.
        Return a list of strings, or a message, depending on the _perChapter variable.
        Extend the superclass method for the 'document per chapter' option.
        """

        if not self._perChapter:
            return super()._get_chapters()

        # Create a directory for the output. Delete contents, if exist.

        xtgDir = os.path.dirname(self.filePath)

        if xtgDir == '':
            xtgDir = '.'

        xtgDir = f'{xtgDir}/{self._XTG_OUT}'

        if os.path.isdir(xtgDir):
            shutil.rmtree(xtgDir)

        os.makedirs(xtgDir)

        chapterNumber = 0
        sceneNumber = 0
        wordsTotal = 0
        lettersTotal = 0

        for chId in self.srtChapters:
            lines = []

            dispNumber = 0

            if not self._chapterFilter.accept(self, chId):
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

                if self._todoChapterTemplate != '':
                    template = Template(self._todoChapterTemplate)

            elif self.chapters[chId].chType == 1:
                # Chapter is "Notes" type (implies "unused").

                if self._notesChapterTemplate != '':
                    template = Template(self._notesChapterTemplate)

            elif self.chapters[chId].isUnused:
                # Chapter is "really" unused.

                if self._unusedChapterTemplate != '':
                    template = Template(self._unusedChapterTemplate)

            elif self.chapters[chId].oldType == 1:
                # Chapter is "Info" type (old file format).

                if self._notesChapterTemplate != '':
                    template = Template(self._notesChapterTemplate)

            elif doNotExport:

                if self._notExportedChapterTemplate != '':
                    template = Template(self._notExportedChapterTemplate)

            elif self.chapters[chId].chLevel == 1 and self._partTemplate != '':
                template = Template(self._partTemplate)

            else:
                template = Template(self._chapterTemplate)
                chapterNumber += 1
                dispNumber = chapterNumber

            if template is not None:
                lines.append(template.safe_substitute(self._get_chapterMapping(chId, dispNumber)))

            # Process scenes.

            sceneLines, sceneNumber, wordsTotal, lettersTotal = self._get_scenes(
                chId, sceneNumber, wordsTotal, lettersTotal, doNotExport)
            lines.extend(sceneLines)

            # Process chapter ending.

            template = None

            if self.chapters[chId].chType == 2:

                if self._todoChapterEndTemplate != '':
                    template = Template(self._todoChapterEndTemplate)

            elif self.chapters[chId].chType == 1:
                
                if self._notesChapterEndTemplate != '':
                    template = Template(self._notesChapterEndTemplate)

            elif self.chapters[chId].isUnused:

                if self._unusedChapterEndTemplate != '':
                    template = Template(self._unusedChapterEndTemplate)

            elif self.chapters[chId].oldType == 1:

                if self._notesChapterEndTemplate != '':
                    template = Template(self._notesChapterEndTemplate)

            elif doNotExport:

                if self._notExportedChapterEndTemplate != '':
                    template = Template(self._notExportedChapterEndTemplate)

            elif self._chapterEndTemplate != '':
                template = Template(self._chapterEndTemplate)

            if template is not None:
                lines.append(template.safe_substitute(self._get_chapterMapping(chId, dispNumber)))

            if lines == []:
                continue

            text = f'{self._fileHeader}{"".join(lines)}'

            # Fix the tags of indented paragraphs.
            # This is done here to include the scene openings.

            text = re.sub('\n\@.+?:\> ', f'\n{self._tagIndentedParagraph}', text)
            xtgPath = f'{xtgDir}/{dispNumber:04}_{self.chapters[chId].title}{self.EXTENSION}'

            try:
                with open(xtgPath, 'w', encoding='utf-8') as f:
                    f.write(text)

            except:
                return(f'{ERROR}Cannot write "{os.path.normpath(xtgPath)}".')

        return 'All chapters written.'

    def _get_text(self):
        """Assemble the whole text applying the templates.
        Return a string to be written to the output file.
        Override the superclass.
        """
        lines = self._get_fileHeader()
        lines.extend(self._get_chapters())
        text = ''.join(lines)

        # Fix the tags of indented paragraphs.
        # This is done here to include the scene openings.

        text = re.sub('\n\@.+?:\> ', f'\n{self._tagIndentedParagraph}', text)
        return text

    def write(self):
        """Create a template-based output file. 
        Return a message beginning with the ERROR constant in case of error.
        Extend the superclass method for the 'document per chapter'
        option.
        """
        if self._perChapter:
            return self._get_chapters()

        else:
            return super().write()
