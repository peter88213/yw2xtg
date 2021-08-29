#!/usr/bin/env python3
"""Helper file for yw2xtg test.

Create config file and template files for German QX document.

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
import os

from pywxtg.xtg_config import XtgConfig
from yw2xtg_ import APPNAME

SCENE_DIVIDER = ''


TEMPLATES = dict(fileHeader='<v11.10><e9>\n',
                 partTemplate='@Überschrift 1:${Title}\n',
                 chapterTemplate='@Überschrift 1:${Title}\n',
                 firstSceneTemplate='@Textkörper:$SceneContent\n',
                 sceneTemplate='@Textkörper:$SceneContent\n',
                 appendedSceneTemplate='$SceneContent\n',
                 sceneDivider='@Überschrift 3:' + SCENE_DIVIDER + '\n',
                 )
STYLES = dict(
    textBody='@Textkörper Einzug:',
    italic='<@Betont>',
    italic0='<@$>',
    bold='<@Stark betont>',
    bold0='<@$>',
    acronym='<t4z9>',
    acronym0='<tz$>',
    figure='<f"Adobe Garamond Small Caps & Old">',
    figure0='<f$>',
)
OPTIONS = dict(
    adjust_digits='Yes',
    space_points='Yes',
    per_chapter='Yes',
)


def run(iniFile):
    iniDir = os.path.dirname(iniFile)

    if not os.path.isdir(iniDir):
        os.makedirs(iniDir)

    configuration = XtgConfig(STYLES, OPTIONS, TEMPLATES)
    configuration.write(iniFile)

    print(iniFile + ' written.')


if __name__ == '__main__':

    try:
        iniFile = sys.argv[1]

    except:
        iniFile = './yw2xtg/' + APPNAME + '.ini'

    run(iniFile)