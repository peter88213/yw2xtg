#!/usr/bin/env python3
"""Helper file for yw2xtg test.

Create config file and template files.

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
import os
from configparser import ConfigParser


EXTENSION = 'XTG'
SCENE_DIVIDER = ''


def run(sourcePath):
    iniPath = os.path.dirname(sourcePath)

    if iniPath == '':
        iniPath = './yw2xtg'

    else:
        iniPath += '/yw2xtg'

    if not os.path.isdir(iniPath):
        os.makedirs(iniPath)

    iniFile = iniPath + '/yw2xtg.ini'
    config = ConfigParser()

    templates = {
        iniPath + '/fileHeader.' + EXTENSION: '<v11.10><e9>\n',
        iniPath + '/partTemplate.' + EXTENSION: '@Überschrift 1:${Title}\n',
        iniPath + '/chapterTemplate.' + EXTENSION: '@Überschrift 1:${Title}\n',
        iniPath + '/firstSceneTemplate.' + EXTENSION: '@Textkörper:$SceneContent\n',
        iniPath + '/sceneTemplate.' + EXTENSION: '@Textkörper:$SceneContent\n',
        iniPath + '/appendedSceneTemplate.' + EXTENSION: '$SceneContent\n',
        iniPath + '/sceneDivider.' + EXTENSION: '@Überschrift 3:' + SCENE_DIVIDER + '\n',
    }

    for template in templates:
        with open(template, 'w', encoding='utf-8') as f:
            f.write(templates[template])

    styles = dict(
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
    if not config.has_section('STYLES'):
        config.add_section('STYLES')

    for style in styles:
        config.set('STYLES', style, styles[style])

    options = dict(
        adjust_digits='yes',
        space_points='yes',
        per_chapter='yes',
    )

    if not config.has_section('OPTIONS'):
        config.add_section('OPTIONS')

    for option in options:
        config.set('OPTIONS', option, options[option])

    with open(iniFile, 'w') as f:
        config.write(f)


if __name__ == '__main__':

    try:
        sourcePath = sys.argv[1]

    except:
        sourcePath = None

    run(sourcePath)
