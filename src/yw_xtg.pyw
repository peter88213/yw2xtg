#!/usr/bin/env python3
"""Export yWriter project to XPress tagged text.

Version @release

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys

from pywriter.converter.yw_cnv_ui import YwCnvUi
from pywriter.ui.ui_tk import UiTk
from pywriter.yw.yw7_file import Yw7File
from pywxtg.xtg_file import XtgFile


class Exporter(YwCnvUi):
    """A converter class for XPress tagged file export."""
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [XtgFile]


def run(sourcePath):
    converter = Exporter()
    converter.ui = UiTk('Export XTG from yWriter @release')
    kwargs = dict(
        suffix='',
        HEADING_1='@Überschrift 1:',
        HEADING_2='@Überschrift 1:',
        HEADING_3='@Überschrift 3:',
        TEXT_BODY='@Textkörper:',
        SCENE_DIVIDER='',
        textBody='@Textkörper Einzug:',
        italic='<@Betont>',
        italic0='<@$>',
        bold='<@Stark betont>',
        bold0='<@$>',
        acronym='<y095.0>',
        acronym0='<y$>',
        figure='<f"Adobe Garamond Small Caps & Old">',
        figure0='<f$>',
    )
    converter.run(sourcePath, **kwargs)
    converter.ui.start()


if __name__ == '__main__':

    try:
        sourcePath = sys.argv[1]

    except:
        sourcePath = ''

    run(sourcePath)
