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
import argparse

from pywriter.converter.yw_cnv_ui import YwCnvUi
from pywriter.ui.ui_tk import UiTk
from pywriter.ui.ui import Ui
from pywriter.yw.yw7_file import Yw7File
from pywxtg.xtg_file import XtgFile


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

OPTIONS = ['adjust_digits',
           'space_points',
           ]


def set_defaults(iniPath, ui):

    if ui.ask_yes_no('No valid initialization data found at "' + os.path.normpath(iniPath) + '".\nUse default settings?'):

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
            acronym='',
            acronym0='',
            figure='',
            figure0='',

            adjust_digits=True,
            space_points=True,
        )

    else:
        return None


def decode_option(option):
    """Return a boolean value, if necessary."""

    try:
        if option.lower() == 'yes':
            option = True

        elif option.lower() == 'no':
            option = False

    except:
        pass

    return option


def run(sourcePath, silentMode):
    converter = Exporter()

    if silentMode:
        converter.ui = Ui('Export XTG from yWriter @release')

    else:
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

            for option in OPTIONS:
                kwargs[option] = decode_option(config.get('OPTIONS', option))

            for template in TEMPLATES:

                with open(iniPath + '/' + template + '.XTG', 'r', encoding='utf-8') as f:
                    kwargs[template] = f.read()

        else:
            kwargs = set_defaults(iniPath, converter.ui)

    except:
        kwargs = set_defaults(iniPath, converter.ui)

    if kwargs is not None:
        converter.run(sourcePath, **kwargs)

    else:
        converter.ui.set_info_how('ERROR: Action canceled by user.')

    converter.ui.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='XPress tagged text export from yWriter projects',
        epilog='')
    parser.add_argument('sourcePath', metavar='Sourcefile',
                        help='The path of the yWriter project file.')

    parser.add_argument('--silent',
                        action="store_true",
                        help='suppress error messages and the request to confirm overwriting or using defaults')
    args = parser.parse_args()

    if args.silent:
        silentMode = True

    else:
        silentMode = False

    if os.path.isfile(args.sourcePath):
        sourcePath = args.sourcePath

    else:
        sourcePath = None

    run(sourcePath, silentMode)
