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
        self.HEADING_1 = kwargs['HEADING_1']
        self.HEADING_2 = kwargs['HEADING_2']
        self.HEADING_3 = kwargs['HEADING_3']
        self.TEXT_BODY = kwargs['TEXT_BODY']
        self.SCENE_DIVIDER = kwargs['SCENE_DIVIDER']

        self.tagTextBody = kwargs['textBody']
        self.tagItalic = kwargs['italic']
        self.tagItalic0 = kwargs['italic0']
        self.tagBold = kwargs['bold']
        self.tagBold0 = kwargs['bold0']
        self.tagAcronym = kwargs['acronym']
        self.tagAcronym0 = kwargs['acronym0']
        self.tagFigure = kwargs['figure']
        self.tagFigure0 = kwargs['figure0']

        self.fileHeader = '<v11.10><e9>\n'
        self.partTemplate = self.HEADING_1 + '${Title}\n'
        self.chapterTemplate = self.HEADING_2 + '${Title}\n'
        self.sceneTemplate = self.TEXT_BODY + '$SceneContent\n'
        self.sceneDivider = self.HEADING_3 + self.SCENE_DIVIDER + '\n'

    def convert_from_yw(self, text):
        """Convert yw7 markup to Markdown.
        """
        def assign_acronym(i):
            return(self.tagAcronym + i.group() + self.tagAcronym0)

        def assign_figure(i):
            return(self.tagFigure + i.group() + self.tagFigure0)

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

        # Replace digit-separating blanks.

        text = re.sub('(\d) (\d)', '\\1<\\![>\\2', text)

        # Assign figures "figure" style.

        matchstr = re.compile('\d+')
        text = matchstr.sub(assign_figure, text)

        # Assign acronyms "acronym" style.

        matchstr = re.compile('[A-ZÄ-Ü]{2,}')
        text = matchstr.sub(assign_acronym, text)

        # Assign the second paragraph "textBody" style.

        t = text.split('\n', 1)

        text = ('\n' + self.tagTextBody).join(t)

        return(text)
