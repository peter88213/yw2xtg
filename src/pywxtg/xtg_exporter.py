"""Provide an XTG exporter class for yWriter.

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.converter.yw_cnv_ui import YwCnvUi
from pywriter.yw.yw7_file import Yw7File

from pywxtg.xtg_file import XtgFile


class XtgExporter(YwCnvUi):
    """A converter class for XPress tagged file export."""
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [XtgFile]

    def confirm_overwrite(self, filePath):
        """Override the superclass method."""
        return True
