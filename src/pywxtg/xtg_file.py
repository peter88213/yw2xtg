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
