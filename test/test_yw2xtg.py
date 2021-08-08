""" Python unit tests for the yw2xtg project.

Test suite for yw2xtg.pyw.

For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from shutil import copyfile
import os
import unittest
import yw2xtg


# Test environment

# The paths are relative to the "test" directory,
# where this script is placed and executed

TEST_PATH = os.getcwd() + '/../test'
TEST_DATA_PATH = TEST_PATH + '/data/'
TEST_EXEC_PATH = TEST_PATH + '/yw7/'
TEMPLATES = 'yw2xtg/'

# To be placed in TEST_DATA_PATH:
REFERENCE_YW7 = TEST_DATA_PATH + 'normal.yw7'
REFERENCE_XTG_TEMPLATES = TEST_DATA_PATH + 'normal.XTG'
REFERENCE_XTG_DEFAULTS = TEST_DATA_PATH + 'defaults.XTG'

# Test data
TEST_YW7 = TEST_EXEC_PATH + 'yw7 Sample Project.yw7'
TEST_XTG = TEST_EXEC_PATH + 'yw7 Sample Project.XTG'


def read_file(inputFile):
    try:
        with open(inputFile, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        # HTML files exported by a word processor may be ANSI encoded.
        with open(inputFile, 'r') as f:
            return f.read()


def remove_all_testfiles():

    try:
        os.remove(TEST_YW7)
    except:
        pass
    try:
        os.remove(TEST_XTG)
    except:
        pass

    for f in os.listdir(TEST_EXEC_PATH + TEMPLATES):
        os.remove(TEST_EXEC_PATH + TEMPLATES + f)


class NormalOperation(unittest.TestCase):
    """Test case: Normal operation."""

    def setUp(self):

        try:
            os.mkdir(TEST_EXEC_PATH)

        except:
            pass

        try:
            os.mkdir(TEST_EXEC_PATH + TEMPLATES)

        except:
            pass

        remove_all_testfiles()
        copyfile(REFERENCE_YW7, TEST_YW7)

    def test_templates(self):

        for f in os.listdir(TEST_DATA_PATH + TEMPLATES):
            copyfile(TEST_DATA_PATH + TEMPLATES + f,
                     TEST_EXEC_PATH + TEMPLATES + f)

        os.chdir(TEST_EXEC_PATH)

        yw2xtg.run(TEST_YW7, silentMode=True)

        self.assertEqual(read_file(TEST_XTG),
                         read_file(REFERENCE_XTG_TEMPLATES))

    def test_defaults(self):
        copyfile(TEST_DATA_PATH + TEMPLATES + 'yw2xtg.ini',
                 TEST_EXEC_PATH + TEMPLATES + 'yw2xtg.ini')
        os.chdir(TEST_EXEC_PATH)

        yw2xtg.run(TEST_YW7, silentMode=True)

        self.assertEqual(read_file(TEST_XTG),
                         read_file(REFERENCE_XTG_DEFAULTS))

    def tearDown(self):
        remove_all_testfiles()


def main():
    unittest.main()


if __name__ == '__main__':
    main()
