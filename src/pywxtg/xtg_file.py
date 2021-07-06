"""Class for XPress tagged file processing. 

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import re

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

    def convert_from_yw(self, text):
        """Convert yw7 markup to Markdown.
        """
        XTG_REPLACEMENTS = [
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
            text = ''

        # Encode non-breaking spaces.

        text = text.replace('\xa0', '<\\!p>')

        # Remove highlighting, alignment,
        # strikethrough, and underline tags.

        text = re.sub('\[\/*[h|c|r|s|u]\d*\]', '', text)

        # Remove comments.

        text = re.sub('\/\*.+?\*\/', '', text)

        # Adjust digit-separating blanks.

        text = re.sub('(\d) (\d)', '\\1<\\![>\\2', text)

        # Adjust digit-separating points.

        text = re.sub('(\d+)\.', '\\1.<\\![>', text)
        text = text.replace('<\\![> ', ' ')

        # Assign "figure" style.

        text = re.sub('(\d+)', self.tagFigure + '\\1' + self.tagFigure0, text)

        # Assign "acronym" style.

        text = re.sub('([A-ZÄ-Ü]{2,})', self.tagAcronym +
                      '\\1' + self.tagAcronym0, text)

        # Assign the second paragraph "textBody" style.

        t = text.split('\n', 1)
        text = ('\n' + self.tagTextBody).join(t)

        return(text)

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
