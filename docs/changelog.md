[Project home page](index) > Changelog

------------------------------------------------------------------------

## Changelog

### v0.12.0 Indent paragraphs that begin with "> "

Based on PyWriter v3.32.2

### v0.10.0 Do not indent paragraphs after blank lines

Please note: The entries in the yw2xtg configuration file have changed.
If you use a custom configuration, do update it manually.

Based on PyWriter v3.32.2

### v0.8.7 Support non-Windows OS

- Move installation and configuration to another location (see instructions for use).

Based on PyWriter v3.28.1

### v0.8.6 Enable non-Windows operation 

- Catch an exception that is thrown when evaluating a Windows environment variable under a non-Windows OS.

Based on PyWriter v3.28.1

### v0.8.5 Optional release

Define the priority of the configurations if there are several.

Configuration and template sources:

1. `yw2xtg` subdirectory in the yWriter project directory.
2. `~\AppData\Roaming\PyWriter\yw2xtg\config`
3. Default values.

If a template file or a configuration entry is missing, *yw2xtg* uses the lower priority source as a fallback. 

Based on PyWriter v3.18.0

### v0.8.4 Bugfix release

This release is strongly recommended.
Fix a regression from PyWriter v3.12.5. causing a crash if a scene has an 
hour, but no minute set.

Based on PyWriter v3.16.4

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

