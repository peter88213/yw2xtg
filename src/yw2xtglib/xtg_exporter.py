"""Provide an XTG exporter class for yWriter.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.converter.yw_cnv_ff import YwCnvFf
from pywriter.yw.yw7_file import Yw7File
from yw2xtglib.xtg_file import XtgFile


class XtgExporter(YwCnvFf):
    """A converter class for XPress tagged file export.

    Class constants:
        EXPORT_SOURCE_CLASSES -- List of YwFile subclasses from which can be exported.
        EXPORT_TARGET_CLASSES -- List of FileExport subclasses to which export is possible.
    """
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [XtgFile]

    def _confirm_overwrite(self, filePath):
        """Overrides the superclass method."""
        return True
