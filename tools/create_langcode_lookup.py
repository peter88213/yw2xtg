"""Helper script for creating a lookup table containing QXP language codes.

The table is a JSON file.
File location is the yw2xtg configuration directory in the user's home directory.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import json
from pathlib import Path

APPNAME = 'yw2xtg'

languageCodes = {
            'en-US':0,
            'fr-FR':1,
            'en-GB':2,
            'es-ES':8,
            'de-CH':69,
            'de-DE':70,
            'zzx':254,
            }


def main(installDir='.'):
    filePath = f'{installDir}/language_codes.json'
    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(languageCodes, f, indent=4)
    print(f'File written: "{filePath}"')


if __name__ == '__main__':
    try:
        homeDir = str(Path.home()).replace('\\', '/')
        installDir = f'{homeDir}/.pywriter/{APPNAME}/config'
    except:
        installDir = '.'
main(installDir)
