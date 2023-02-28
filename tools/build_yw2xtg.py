""" Build a python script for the yw2xtg distribution.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the pywriter package.

The PyWriter project (see see https://github.com/peter88213/PyWriter)
must be located on the same directory level as the yw2xtg project. 

For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../PyWriter/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}yw2xtg_.pyw'
TARGET_FILE = f'{BUILD}yw2xtg.pyw'


def main():
    inliner.run(SOURCE_FILE, TARGET_FILE, 'yw2xtglib', '../src/', copyPyWriter=False)
    inliner.run(TARGET_FILE, TARGET_FILE, 'pywriter', '../../PyWriter/src/', copyPyWriter=False)
    # inliner.run(SOURCE_FILE, TARGET_FILE, 'yw2xtglib', '../src/')
    # inliner.run(TARGET_FILE, TARGET_FILE, 'pywriter', '../src/')
    print('Done.')


if __name__ == '__main__':
    main()
