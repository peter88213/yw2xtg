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
        self.FIRST_LINE_INDENT = kwargs['FIRST_LINE_INDENT']
        self.EMPHASIZE = kwargs['EMPHASIZE']
        self.STRONG_EMPHASIZE = kwargs['STRONG_EMPHASIZE']
        self.ACRONYM = kwargs['ACRONYM']
        self.FIGURE = kwargs['FIGURE']
        self.SCENE_DIVIDER = kwargs['SCENE_DIVIDER']

        self.fileHeader = '<v11.10><e9>\n'
        self.partTemplate = '@' + self.HEADING_1 + ':${Title}\n'
        self.chapterTemplate = '@' + self.HEADING_2 + ':${Title}\n'
        self.sceneTemplate = '@' + self.TEXT_BODY + ':$SceneContent\n'
        self.sceneDivider = '@' + self.HEADING_3 + ':' + self.SCENE_DIVIDER + '\n'

    def convert_from_yw(self, text):
        """Convert yw7 markup to Markdown.
        """
        def assign_acronym(i):
            return('<@' + self.ACRONYM + '>' + i.group() + '<@$>')

        def assign_figure(i):
            return('<@' + self.FIGURE + '>' + i.group() + '<@$>')

        XTG_REPLACEMENTS = [
            ['[i]', '<@' + self.EMPHASIZE + '>'],
            ['[/i]', '<@$>'],
            ['[b]', '<@' + self.STRONG_EMPHASIZE + '>'],
            ['[/b]', '<@$>'],
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

        # Assign acronyms "ACRONYM" style.

        matchstr = re.compile('[A-ZÄ-Ü]{2,}')
        text = matchstr.sub(assign_acronym, text)

        # Replace digit-separating blanks.

        text = re.sub('(\d) (\d)', '\\1<\\![>\\2', text)

        # Assign figures "FIGURE" style.

        matchstr = re.compile('\d+')
        text = matchstr.sub(assign_figure, text)

        # Assign the second paragraph "FIRST_LINE_INDENT" style.

        t = text.split('\n', 1)

        text = ('\n@' + self.FIRST_LINE_INDENT + ':').join(t)

        return(text)
