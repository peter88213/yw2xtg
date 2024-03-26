[Project homepage](https://peter88213.github.io/yw2xtg) > Instructions for use

---

The yw2xtg Python script runs through all chapters and scenes of a yWriter 7 project and fills XTG templates.

## Instructions for use

### Intended usage

The included installation script prompts you to create a shortcut on the desktop. You can launch the program by dragging a yWriter project file and dropping it on the shortcut icon. 

### Command line usage

Alternatively, you can

- launch the program on the command line passing the yWriter project file as an argument, or
- launch the program via a batch file.

usage: `yw2xtg.pyw [--silent] Sourcefile`

#### positional arguments:

`Sourcefile` 

The path of the yWriter project file.

#### optional arguments:

`--silent`  suppress error messages and the request to confirm the use of default values

---

## General

### About XTG

The XTG file format uses the *XPress Tags* language, the knowledge of which is assumed. You can 
download the manual *A Guide to XPress Tags* for your program version from the *Quark* web site.

### yWriter text markup

Bold and italics are supported. Other highlighting such as underline and strikethrough are lost.

### Quotation marks and punctuation

It is assumed that quotation marks and punctuation marks are already set correctly; this is best done in advance with a word processor, e.g. via yWriter's "proof read" function. 

## Configuration

- Place a subfolder named **yw2xtg** in the yWriter project folder. It contains the configuration file
and all template files as listed below to be applied to this project. The best way is to copy the provided sample folder and customize the contained files with a text editor according to your needs. 

- If there is no configuration data in the project file, data stored in `c:\Users\<user name>\.pywriter\yw2xtg\config` is used prior to the script's default configuration data.

- If a template file or a configuration entry is missing, *yw2xtg* uses the lower priority source as a fallback. 


### Configuration file

This is an exapmle configuration file containing the default values mentioned above:

```ini
[STYLES]
first_paragraph = @Text body:

# XPress tag for paragraphs preceded by a heading or a blank line.

indented_paragraph = @Text body indent:

# XPress tag for indented paragraphs.

other_paragraph = @First line indent:

# XPress tag for regular paragraphs.

italic = <@Emphasis>

# XPress tag opening italic sections. 

italic0 = <@$p>

# XPress tag closing italic sections.

bold = <@Strong emphasis>

# XPress tag opening bold sections.

bold0 = <@$p>

# XPress tag closing bold sections.

acronym =

# XPress tag opening acronyms.
 
acronym0 = 

# XPress tag closing acronyms.

figure =

# XPress tag opening figure groups.

figure0 = 

# XPress tag closing figure groups.

[OPTIONS]

adjust_digits = Yes

# If True, adjust digit-separating blanks.

space_points = Yes

# If True, space digit-separating points.

per_chapter = No

# If True, create one XTG file for each chapter.
# If False, create one XTG file for the entire document.

```

#### Style tags

- **textbody** - The QX paragraph style applied to all paragraphs in a scene, except the first. The first paragraph's style can be set in the scene level templates.
- **italic** - The opening tag to replace yWriter's *italic* formatting.
- **italic0** - The closing tag to replace yWriter's *italic* formatting.
- **bold** - The opening tag to replace yWriter's *bold* formatting.
- **bold0** - The closing tag to replace yWriter's *bold* formatting.
- **acronym** - The opening tag to format sequences of uppercase characters (e.g. set a slightly smaller font size).
- **acronym0** - The closing tag to format sequences of uppercase characters.
- **figure** - The opening tag to format figures (e.g. switch the font to get "osf" text figures).
- **figure0** - The closing tag to format figures.

#### Options

- **adjust_digits** - Replace regular spaces between digits with thin spaces.
- **space_points** - Insert a thin space after each point that separates digits.
- **per_chapter** - Generate one XTG file per chapter. The file names consist of the chapter's number and title. the files are written to the XTG_Chapters subdirectory.

You can define styles in *fileHeader.XTG*, but it is preferable to use the names of styles that already exist in the QX book project instead.

## List of templates

### Project level templates

- **fileHeader.XTG** - This template must contain at least the version code and encoding indication.

### Chapter level templates

- **partTemplate.XTG** - Chapter header; applied to chapters marked "section beginning".
- **chapterTemplate.XTG** - Chapter header; applied to all "used" and "normal" chapters unless a "part template" exists.


### Scene level templates

- **firstSceneTemplate.XTG** - Applied  to scenes at the beginning of the chapter.
- **sceneTemplate.XTG** - Applied to "used" scenes within "normal" chapters.
- **sceneDivider.XTG** - Scene divider placed between scenes.
- **appendedSceneTemplate.XTG** - Applied to scenes to be appended to the previous scene.


## Placeholders

### Syntax

There are two options:

1. $Placeholder
2. ${Placeholder}


### "Project template" placeholders

- **$Title** - Project title
- **$Desc** - Project description, html-formatted
- **$AuthorName** - Author's name
- **$AuthorBio** - Information about the author


- **$FieldTitle1** - Rating names: field 1
- **$FieldTitle2** - Rating names: field 2
- **$FieldTitle3** - Rating names: field 3
- **$FieldTitle4** - Rating names: field 4

- **$Language** - Language code acc. to ISO 639-1
- **$Country** - Country code acc. to ISO 3166-2

### "Chapter template" placeholders

- **$ID** - Chapter ID,
- **$ChapterNumber** - Chapter number (in sort order),

- **$Title** - Chapter title
- **$Desc** - Chapter description, html-formatted

- **$Language** - Language code acc. to ISO 639-1
- **$Country** - Country code acc. to ISO 3166-2

### "Scene template" placeholders

- **$ID** - Scene ID,
- **$SceneNumber** - Scene number (in sort order),

- **$Title** - Scene title
- **$Desc** - Scene description, html-formatted

- **$WordCount** - Scene word count
- **$WordsTotal** - Accumulated word count including the current scene
- **$LetterCount** - Scene letter count
- **$LettersTotal** - Accumulated letter count including the current scene

- **$Status** - Scene status (Outline, Draft etc.)
- **$SceneContent** - Scene content, html-formatted

- **$FieldTitle1** - Rating names: field 1
- **$FieldTitle2** - Rating names: field 2
- **$FieldTitle3** - Rating names: field 3
- **$FieldTitle4** - Rating names: field 4
- **$Field1** - Scene rating: field 1
- **$Field2** - Scene rating: field 2
- **$Field3** - Scene rating: field 3
- **$Field4** - Scene rating: field 4

- **$Date** - Specific scene date (yyyy-mm-dd)
- **$Time** - Time scene begins: (hh:mm)
- **$Day** - Day scene begins 
- 
- **$ScDate** - Date or day

- **$LastsDays** - Amount of time scene lasts: days
- **$LastsHours** - Amount of time scene lasts: hours
- **$LastsMinutes** - Amount of time scene lasts: minutes

- **Duration** - Combination of days and hours and minutes

- **$ReactionScene** - A(ction) or R(eaction)
- **$Goal** - The scene protagonist's goal, html-formatted
- **$Conflict** - The scene conflict, html-formatted
- **$Outcome** - The scene outcome, html-formatted
- **$Tags** - Comma-separated list of scene tags
- **$Image** - Image filename

- **$Characters** - Comma-separated list of characters assigned to the scene
- **$Viewpoint** - Viewpoint character
- **$Locations** - Comma-separated list of locations assigned to the scene
- **$Items** - Comma-separated list of items assigned to the scene

- **$Notes** - Scene notes

- **$Language** - Language code acc. to ISO 639-1
- **$Country** - Country code acc. to ISO 3166-2

## Installation path

The setup script installs *yw2xtg.pyw* in the user profile. This is the installation path on Windows: 

`c:\Users\<user name>\.pywriter\yw2xtg`
