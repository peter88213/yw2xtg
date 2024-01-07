"""Build a Python script for the novx_xtg distribution.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the novxlib package.

The Pnoveltree project (see see https://github.com/peter88213/Pnoveltree)
must be located on the same directory level as the novx_xtg project. 

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../Pnoveltree/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}novx_xtg_.pyw'
TARGET_FILE = f'{BUILD}novx_xtg.pyw'


def main():
    inliner.run(SOURCE_FILE, TARGET_FILE, 'nvxtglib', '../src/', copyPnoveltree=False)
    inliner.run(TARGET_FILE, TARGET_FILE, 'novxlib', '../../Pnoveltree/src/', copyPnoveltree=False)
    # inliner.run(SOURCE_FILE, TARGET_FILE, 'nvxtglib', '../src/')
    # inliner.run(TARGET_FILE, TARGET_FILE, 'novxlib', '../src/')
    print('Done.')


if __name__ == '__main__':
    main()
