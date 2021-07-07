""" Python unit tests for the yw2xtg project.

Test suite for yw2xtg.pyw.

For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
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

# Test data
YW7 = 'normal.yw7'
XTG_FILE = 'normal.XTG'
XTG_FILE_DEFAULTS = 'defaults.XTG'


def read_file(inputFile):
    try:
        with open(inputFile, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        # HTML files exported by a word processor may be ANSI encoded.
        with open(inputFile, 'r') as f:
            return f.read()


def copy_file(inputFile, outputFile):
    with open(inputFile, 'rb') as f:
        myData = f.read()
    with open(outputFile, 'wb') as f:
        f.write(myData)
    return()


def remove_all_testfiles():

    try:
        os.remove(TEST_EXEC_PATH + YW7)
    except:
        pass
    try:
        os.remove(TEST_EXEC_PATH + XTG_FILE)
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
        copy_file(TEST_DATA_PATH + YW7, TEST_EXEC_PATH + YW7)

    def test_templates(self):

        for f in os.listdir(TEST_DATA_PATH + TEMPLATES):
            copy_file(TEST_DATA_PATH + TEMPLATES + f,
                      TEST_EXEC_PATH + TEMPLATES + f)

        os.chdir(TEST_EXEC_PATH)

        yw2xtg.run(TEST_EXEC_PATH + YW7, True)

        self.assertEqual(read_file(TEST_EXEC_PATH + XTG_FILE),
                         read_file(TEST_DATA_PATH + XTG_FILE))

    def test_defaults(self):
        os.chdir(TEST_EXEC_PATH)

        yw2xtg.run(TEST_EXEC_PATH + YW7, True)

        self.assertEqual(read_file(TEST_EXEC_PATH + XTG_FILE),
                         read_file(TEST_DATA_PATH + XTG_FILE_DEFAULTS))

    def tearDown(self):
        remove_all_testfiles()


def main():
    unittest.main()


if __name__ == '__main__':
    main()
