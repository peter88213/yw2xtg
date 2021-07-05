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

    SCENE_DIVIDER = '* * *'

    fileHeader = '''**${Title}**  
  
*${AuthorName}*  
  
'''

    partTemplate = '\n# ${Title}\n\n'

    chapterTemplate = '\n## ${Title}\n\n'

    sceneTemplate = '<!---${Title}--->${SceneContent}\n\n'

    sceneDivider = '\n\n' + SCENE_DIVIDER + '\n\n'

    def __init__(self, filePath, **kwargs):
        FileExport.__init__(self, filePath)

    def convert_from_yw(self, text):
        """Convert yw7 markup to Markdown.
        """

        MD_REPLACEMENTS = [
            ['[i]', '*'],
            ['[/i]', '*'],
            ['[b]', '**'],
            ['[/b]', '**'],
            ['/*', '<!---'],
            ['*/', '--->'],
            ['  ', ' '],
        ]

        if not self.markdownMode:
            MD_REPLACEMENTS[:0] = [['\n', '\n\n']]

        try:

            for r in MD_REPLACEMENTS:
                text = text.replace(r[0], r[1])

            # Remove highlighting, alignment,
            # strikethrough, and underline tags.

            text = re.sub('\[\/*[h|c|r|s|u]\d*\]', '', text)

        except AttributeError:
            text = ''

        return(text)
