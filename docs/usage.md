[Project homepage](https://peter88213.github.io/yw2xtg)


The yw2xtg Python script runs through all chapters and scenes of a yWriter 7 project and fills XTG templates.

## Usage

It is recommended to create a link on the desktop.

You can either

- launch the program on the command line passing the yWriter project file as an argument, or
- launch the program by dragging a yWriter project file and dropping it on the program/link icon.


## List of templates

### Project level templates

- **html_header.html** 

- **character_template.html** (applied to characters)
- **location_template.html** (applied to locations)
- **item_template.html** (applied to items)

- **html_footer.html** 

### Chapter level templates

- **part_template.html** (chapter header; applied to chapters marked "section beginning")
- **chapter_template.html** (chapter header; applied to all "used" and "normal" chapters unless a "part template" exists)
- **unused_chapter_template.html** (chapter header; applied to chapters marked "unused" or "do not export")
- **notes_chapter_template.html** (chapter header; applied to chapters marked "notes")
- **todo_chapter_template.html** (chapter header; applied to chapters marked "todo")

- **chapter_end_template.html** (chapter footer; applied to all "used" and "normal" chapters)
- **unused_chapter_end_template.html** (chapter footer; applied to chapters marked "unused" or "do not export")
- **notes_chapter_end_template.html** (chapter footer; applied to chapters marked "notes")
- **todo_chapter_end_template.html** (chapter footer; applied to chapters marked "todo")


### Scene level templates

- **scene_template.html** (applied to "used" scenes within "normal" chapters)
- **first_scene_template.html** (applied  to scenes at the beginning of the chapter)
- **unused_scene_template.html** (applied to "unused" scenes)
- **notes_scene_template.html** (applied to scenes marked "notes")
- **todo_scene_template.html** (applied to scenes marked "todo")
- **scene_divider.html** (lead scenes, beginning from the second in chapter)




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


