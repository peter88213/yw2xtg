The yw2xtg Python script exports [yWriter](http://spacejock.com/yWriter7.html) projects as a whole in the [XPress Tags](https://www.quark.com/documentation/quarkxpress/2019/english/A%20Guide%20to%20XPress%20Tags%202019/) format for the Quark XPress DTP software. It generates an XTG file ready for import into a QX book project. This is done based on template files for chapters and scenes, so you can be quite flexible with the program output. In addition, the exporter script can take some routine work off your hands, for example, formatting figures and acronyms in a special way, if desired. Formatting codes and paragraph/character style tags are read from a configuration file.
Optionally, one XTG file per chapter can be generated.

## Requirements

- [Python 3.6+](https://www.python.org).

## Download and install

[Download the latest release (version 1.0.5)](https://raw.githubusercontent.com/peter88213/yw2xtg/main/dist/yw2xtg_v1.0.5.zip)

- Unzip the downloaded zipfile "yw2xtg_v1.0.5.zip" into a new folder.
- Move into this new folder and launch **setup.pyw**. This installs the script for the local user.
- Create a shortcut on the desktop when asked.
- Open "README.md" for usage instructions.

### Note for Linux users

Please make sure that your Python3 installation has the *tkinter* module. On Ubuntu, for example, it is not available out of the box and must be installed via a separate package. 

------------------------------------------------------------------

[Changelog](changelog)

## Usage

See the [instructions for use](usage)

## Credits

- User *Hunter_71* presented the number to English conversion algorithm on [stack overflow](https://stackoverflow.com/a/51849443).
- User *Aristide* presented the integer to roman numeral conversion on [stack overflow](https://stackoverflow.com/a/47713392).

## License

yw2xtg is distributed under the [MIT
License](http://www.opensource.org/licenses/mit-license.php).
