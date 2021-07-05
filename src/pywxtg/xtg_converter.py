"""Provide a XPress tagged file converter class for yWriter projects. 

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.converter.yw_cnv_ui import YwCnvUi

from pywriter.yw.yw7_file import Yw7File
from pywxtg.xtg_file import XtgFile


class XtgConverter(YwCnvUi):
    """A converter class for XPress tagged file export."""
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [XtgFile]
