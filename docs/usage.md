[Project homepage](https://peter88213.github.io/yw2xtg)


The yw2xtg Python script runs through all chapters and scenes of a yWriter 7 project and fills XTG templates.

## Usage

It is recommended to create a link on the desktop.

You can either

- launch the program on the command line passing the yWriter project file as an argument, or
- launch the program by dragging a yWriter project file and dropping it on the program/link icon.

## General

### About XTG

The XTG file format uses the *XPress Tags* language, the knowledge of which is assumed. There is a comprehensive [online documentation](https://www.quark.com/documentation/quarkxpress/2019/english/A%20Guide%20to%20XPress%20Tags%202019/) for this. 

### yWriter text markup

Bold and italics are supported. Other highlighting such as underline and strikethrough are lost.

### Quotation marks and punctuation

It is assumed that quotation marks and punctuation marks are already set correctly; this is best done in advance with a word processor, e.g. via yWriter's "proof read" function. 

## Configuration

Place a subfolder named **yw2xtg** in the yWriter project folder. It contains the configuration file
and all template files as listed below to be applied to this project. The best way is to copy the provided sample folder and customize the contained files with a text editor according to your needs. 

If a file is missing, or the configuration file is corrupted, *yw2xtg* asks for permission
to use default values. 

### Configuration file

This is an exapmle configuration file containing the default values mentioned above:

```
[STYLES]
textbody = @First line indent:
italic = <@Emphasis>
italic0 = <@$>
bold = <@Small caps>
bold0 = <@$>
acronym = 
acronym0 = 
figure = 
figure0 = 
```

- **textbody** - The QX paragraph style applied to all paragraphs in a scene, except the first. The first paragraph's style can be set in the scene level templates.
- **italic** - The opening tag to replace yWriter's *italic* formatting.
- **italic0** - The closing tag to replace yWriter's *italic* formatting.
- **bold** - The opening tag to replace yWriter's *bold* formatting.
- **bold0** - The closing tag to replace yWriter's *bold* formatting.
- **acronym** - The opening tag to format sequences of uppercase characters (e.g. set a slightly smaller font size).
- **acronym0** - The closing tag to format sequences of uppercase characters.
- **figure** - The opening tag to format figures (e.g. switch the font to get "osf" text figures).
- **figure0** - The closing tag to format figures.

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


### "HTML header" placeholders

- **$Title** - Project title
- **$Desc** - Project description, html-formatted
- **$AuthorName** - Author's name


- **$FieldTitle1** - Rating names: field 1
- **$FieldTitle2** - Rating names: field 2
- **$FieldTitle3** - Rating names: field 3
- **$FieldTitle4** - Rating names: field 4

### "Chapter template" placeholders

- **$ID** - Chapter ID,
- **$ChapterNumber** - Chapter number (in sort order),
- **$ChNumberEnglish** - Chapter number written out in English (capitalized),
- **$ChNumberRoman** - Chapter number in Roman numbers (uppercase),

- **$Title** - Chapter title
- **$Desc** - Chapter description, html-formatted

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

- **$Date** - Specific scene date
- **$Time** - Specific scene time
- **$Day** - Time scene begins: day
- **$Hour** - Time scene begins: hour
- **$Minute** - Time scene begins: minute
- **$LastsDays** - Amount of time scene lasts: days
- **$LastsHours** - Amount of time scene lasts: hours
- **$LastsMinutes** - Amount of time scene lasts: minutes

- **$ReactionScene** - A(ction) or R(eaction)
- **$Goal** - The scene protagonist's goal, html-formatted
- **$Conflict** - The scene conflict, html-formatted
- **$Outcome** - The scene outcome, html-formatted
- **$Tags** - Comma-separated list of scene tags

- **$Characters** - Comma-separated list of characters assigned to the scene
- **$Viewpoint** - Viewpoint character
- **$Locations** - Comma-separated list of locations assigned to the scene
- **$Items** - Comma-separated list of items assigned to the scene

- **$Notes** - Scene notes, html-formatted


