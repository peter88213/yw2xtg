[Project home page](index) > Changelog

------------------------------------------------------------------------

## Changelog

### Planned features

See the [GitHub "Features" project](https://github.com/users/peter88213/projects/4/views/1).

### v1.2.3

- Library update.

Based on PyWriter v12.4.1

### v1.2.2

- Reduce the memory use by discarding the docstrings on building.

Based on PyWriter v12.1.2

### v1.2.1

- Remove "shebang" lines to make the scripts run with Python 3.11 under Windows.

Based on PyWriter v9.0.5

### v1.2.0

- Code optimization and library update. 

Based on PyWriter v9.0.4

### v1.1.2

- Library upgrade.
- Convert language codes.
- Error handling via exceptions instead of returned messages.

Based on PyWriter v8.0.8

### v1.0.10

- Update the PyWriter library for future Python versions.

Based on PyWriter v7.14.2

### v1.0.9

- Update the icon set.
- Refactor the code.

Based on PyWriter v7.4.1

### v1.0.8

- Set own window icon.

Based on PyWriter v7.4.1

### v1.0.7 Optional release

- Code refactoring and library update.

Based on PyWriter v7.2.1

### v1.0.6 Update setup script

- Change the working dir to the script dir on startup in order to avoid "file not found" error.

Based on PyWriter v5.18.0

### v1.0.5 Improved setup

- Catch exceptions in the setup script.

Based on PyWriter v5.18.0

### v1.0.4 Bugfix release

- Fix and refactor inline code removal.

Based on PyWriter v5.16.1

### v1.0.3 Consider inline code

- Remove inline code when exporting.

Based on PyWriter v5.12.5

### v1.0.2

- Improve code and documentation quality.

Based on PyWriter v5.6.1

### v1.0.1

- Improve code and documentation quality.

Based on PyWriter v5.0.2

### v1.0.0

- Fix a regression from v0.12.2 where paragraph indenting doesn't work when exporting to chapters.
- Fix a bug where "To do" chapters cause an exception.
- Process non-ASCII characters in the configuration file. 
- Change the default character style closing tag.
- Add $AuthorBio placeholder.
- Improve the overall code quality.

Based on PyWriter v5.0.0

### v0.12.2 Optional update

Refactor the code.

Based on PyWriter v3.32.2

### v0.12.1 Optional update

Refactor the code.

Based on PyWriter v3.32.2

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

