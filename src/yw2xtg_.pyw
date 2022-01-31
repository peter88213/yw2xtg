#!/usr/bin/env python3
"""Export yWriter project to XPress tagged text.

Python 3.7+
Version @release

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import argparse
from pathlib import Path

from pywriter.ui.ui_tk import UiTk
from pywriter.ui.ui import Ui
from pywxtg.xtg_config import XtgConfig
from pywxtg.xtg_exporter import XtgExporter


SUFFIX = ''
APPNAME = 'yw2xtg'

SCENE_DIVIDER = ''

STYLES = dict(first_paragraph='@Text body:',
              indented_paragraph='@Text body indent:',
              other_paragraph='@First line indent:',
              italic='<@Emphasis>',
              italic0='<@$>',
              bold='<@Small caps>',
              bold0='<@$>',
              acronym='',
              acronym0='',
              figure='',
              figure0='',

              )

TEMPLATES = dict(file_header='<v11.10><e9>\n',
                 part_template='@Heading 1:${Title}\n',
                 chapter_template='@Heading 1:${Title}\n',
                 first_scene_template='@Text body:$SceneContent\n',
                 scene_template='@Text body:$SceneContent\n',
                 appended_scene_template='$SceneContent\n',
                 scene_divider=f'@Heading 3:{SCENE_DIVIDER}\n',
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
        sourceDir = f'./{APPNAME}/'

    else:
        sourceDir = f'{sourceDir}/{APPNAME}/'

    iniFileName = f'{APPNAME}.ini'
    iniFiles = [f'{installDir}{iniFileName}', f'{sourceDir}{iniFileName}']

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
        homeDir = str(Path.home()).replace('\\', '/')
        installDir = f'{homeDir}/.pywriter/{APPNAME}/config/'

    except:
        installDir = ''

    run(args.sourcePath, args.silent, installDir)
