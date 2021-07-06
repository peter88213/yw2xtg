#!/usr/bin/env python3
"""Export yWriter project to XPress tagged text.

Version @release

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
import os
from configparser import ConfigParser

from pywriter.converter.yw_cnv_ui import YwCnvUi
from pywriter.ui.ui_tk import UiTk
from pywriter.yw.yw7_file import Yw7File
from pywxtg.xtg_file import XtgFile

from tkinter import messagebox


class Exporter(YwCnvUi):
    """A converter class for XPress tagged file export."""
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [XtgFile]


SCENE_DIVIDER = ''

STYLES = ['textBody',
          'italic',
          'italic0',
          'bold',
          'bold0',
          'acronym',
          'acronym0',
          'figure',
          'figure0',
          ]

TEMPLATES = ['fileHeader',
             'partTemplate',
             'chapterTemplate',
             'firstSceneTemplate',
             'sceneTemplate',
             'appendedSceneTemplate',
             'sceneDivider',
             ]


def set_defaults(iniPath):

    if messagebox.askyesno(
            'WARNING', 'No valid initialization data found at "' + os.path.normpath(iniPath) + '".\nUse default settings?'):

        return dict(
            suffix='',

            fileHeader='<v11.10><e9>\n',
            partTemplate='@Heading 1:${Title}\n',
            chapterTemplate='@Heading 1:${Title}\n',
            firstSceneTemplate='@Text body:$SceneContent\n',
            sceneTemplate='@Text body:$SceneContent\n',
            appendedSceneTemplate='$SceneContent\n',
            sceneDivider='@Heading 3:' + SCENE_DIVIDER + '\n',

            textBody='@First line indent:',
            italic='<@Emphasis>',
            italic0='<@$>',
            bold='<@Small caps>',
            bold0='<@$>',
            acronym='<y095.0>',
            acronym0='<y$>',
            figure='',
            figure0='',
        )

    else:
        return None


def run(sourcePath):
    converter = Exporter()
    converter.ui = UiTk('Export XTG from yWriter @release')

    #--- Try to get persistent configuration data

    try:
        iniPath = os.path.dirname(sourcePath)

        if iniPath == '':
            iniPath = './yw2xtg'

        else:
            iniPath += '/yw2xtg'

        iniFile = iniPath + '/yw2xtg.ini'
        config = ConfigParser()

        if os.path.isfile(iniFile):

            config.read(iniFile)
            kwargs = {'suffix': ''}

            for style in STYLES:
                kwargs[style] = config.get('STYLES', style)

            for template in TEMPLATES:

                with open(iniPath + '/' + template + '.XTG', 'r', encoding='utf-8') as f:
                    kwargs[template] = f.read()

        else:
            kwargs = set_defaults(iniPath)

    except:
        kwargs = set_defaults(iniPath)

    if kwargs is not None:
        converter.run(sourcePath, **kwargs)

    else:
        converter.ui.set_info_how('ERROR: Action canceled by user.')

    converter.ui.start()


if __name__ == '__main__':

    try:
        sourcePath = sys.argv[1]

    except:
        sourcePath = None

    run(sourcePath)
