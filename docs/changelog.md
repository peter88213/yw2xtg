[Project home page](index) > Changelog

------------------------------------------------------------------------

## Changelog

### v0.8.3 No automatic shortcut creation

- Due to sporadic security warnings, the automatic shortcut creation during installation is removed. The user is now guided to create the application shortcut manually. 
- Refactor: Use standard function for reading boolean values from the INI file.

Based on PyWriter v3.16.0

### v0.8.2 Use backup configuration

If there is no configuration data in the project file, 
data stored in the installation folder is used prior to 
the script's default configuration data.

Based on PyWriter v3.12.7

### v0.8.1 Include installation script

**install.bat** installs the script for the local user and creates a 
shortcut on the desktop.

Based on PyWriter v3.12.7

### v0.8.0 Extend configuration

Move the "ope file per chapter" option from the command line arguments 
to the configuration file.
The chapter files are written to the XTG_chapters subdirectory.

**Note:**

When updating from v0.6, the per_chapter line must be added to existing 
configuration files.

Based on PyWriter v3.12.7

### v0.6.0 Create chapter files

Optionally, one file per chapter is created.

Based on PyWriter v3.12.7

### v0.4.1 Implement a silent mode

Based on PyWriter v3.12.6.

### v0.4.0 Extend the configuration file

- Add OPTIONS section to the configuration.
- Make some text processing steps optional.
- Escape XPress Tags code-specific characters.

Based on PyWriter v3.12.6.

### v0.2.1 Modify default values

Based on PyWriter v3.12.6.

### v0.2.0 Beta test release 

Based on PyWriter v3.12.6.

