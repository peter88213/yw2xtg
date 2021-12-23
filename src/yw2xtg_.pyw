#!/usr/bin/env python3
"""Export yWriter project to XPress tagged text.

Version @release

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import argparse

from pywriter.ui.ui_tk import UiTk
from pywriter.ui.ui import Ui
from pywxtg.xtg_config import XtgConfig
from pywxtg.xtg_exporter import XtgExporter


SUFFIX = ''
APPNAME = 'yw2xtg'

SCENE_DIVIDER = ''

STYLES = dict(textBody='@First line indent:',
              italic='<@Emphasis>',
              italic0='<@$>',
              bold='<@Small caps>',
              bold0='<@$>',
              acronym='',
              acronym0='',
              figure='',
              figure0='',

              )

TEMPLATES = dict(fileHeader='<v11.10><e9>\n',
                 partTemplate='@Heading 1:${Title}\n',
                 chapterTemplate='@Heading 1:${Title}\n',
                 firstSceneTemplate='@Text body:$SceneContent\n',
                 sceneTemplate='@Text body:$SceneContent\n',
                 appendedSceneTemplate='$SceneContent\n',
                 sceneDivider='@Heading 3:' + SCENE_DIVIDER + '\n',
                 )

OPTIONS = dict(adjust_digits=True,
               space_points=True,
               per_chapter=False,
               )


def run(sourcePath, silentMode=True, installDir=''):

    if silentMode:
        ui = Ui('')

    else:
        ui = UiTk('Export XTG from yWriter @release')

    #--- Try to get persistent configuration data

    sourceDir = os.path.dirname(sourcePath)

    if sourceDir == '':
        sourceDir = './' + APPNAME + '/'

    else:
        sourceDir += '/' + APPNAME + '/'

    iniFileName = APPNAME + '.ini'
    iniFiles = [installDir + iniFileName, sourceDir + iniFileName]

    configuration = XtgConfig(STYLES, OPTIONS, TEMPLATES)

    for iniFile in iniFiles:
        configuration.read(iniFile)

    kwargs = {'suffix': SUFFIX}
    kwargs.update(configuration.settings)
    kwargs.update(configuration.options)
    kwargs.update(configuration.templates)

    converter = XtgExporter()
    converter.ui = ui
    converter.run(sourcePath, **kwargs)
    ui.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='XPress tagged text export from yWriter projects',
        epilog='')

    parser.add_argument('sourcePath', metavar='Sourcefile',
                        help='The path of the yWriter project file.')

    parser.add_argument('--silent',
                        action="store_true",
                        help='suppress error messages and the request to confirm the use of default values')

    args = parser.parse_args()

    try:
        installDir = os.getenv('APPDATA').replace('\\', '/') + '/pyWriter/' + APPNAME + '/config/'

    except:
        installDir = ''

    run(args.sourcePath, args.silent, installDir)
