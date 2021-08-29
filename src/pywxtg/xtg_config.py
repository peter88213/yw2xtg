"""Provide a Configuration class for reading and writing INI files.

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
from pywriter.config.configuration import Configuration


class XtgConfig(Configuration):
    """Read/write the program configuration.
    """

    def __init__(self, settings={}, options={}, templates={}):
        """Override the superclass constructor, redefining sLabel.
        """
        self.sLabel = 'STYLES'
        self.oLabel = 'OPTIONS'
        self.set(settings, options, templates)

    def set(self, settings=None, options=None, templates=None):

        if settings is not None:
            self.settings = settings.copy()

        if options is not None:
            self.options = options.copy()

        if templates is not None:
            self.templates = templates.copy()

    def read(self, iniFile):
        """Read a configuration file.
        Settings and options that can not be read in, remain unchanged.
        """
        Configuration.read(self, iniFile)
        iniPath = os.path.dirname(iniFile)

        for template in self.templates:

            try:

                with open(iniPath + '/' + template + '.XTG', 'r', encoding='utf-8') as f:
                    self.templates[template] = f.read()

            except:
                pass

    def write(self, iniFile):
        """Save the configuration to iniFile.
        """
        Configuration.write(self, iniFile)
        iniPath = os.path.dirname(iniFile)

        for template in self.templates:

            with open(iniPath + '/' + template + '.XTG', 'w', encoding='utf-8') as f:
                f.write(self.templates[template])
