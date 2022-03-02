#!/usr/bin/env python3
"""Helper file for yw2xtg test.

Create config file.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
import os
from yw2xtglib.xtg_config import XtgConfig
from yw2xtg_ import STYLES
from yw2xtg_ import OPTIONS
from yw2xtg_ import TEMPLATES
from yw2xtg_ import APPNAME


def run(iniFile):
    iniDir = os.path.dirname(iniFile)
    if not os.path.isdir(iniDir):
        os.makedirs(iniDir)
    configuration = XtgConfig(STYLES, OPTIONS, TEMPLATES)
    configuration.write(iniFile)
    print(f'{iniFile} written.')


if __name__ == '__main__':
    try:
        iniFile = sys.argv[1]
    except:
        iniFile = f'./yw2xtg/{APPNAME}.ini'
    run(iniFile)
