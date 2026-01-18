# UCL Timetable Parser

## Motivation

The UCL Timetable can be directly imported via URL as a private calendar. However, if you want to make it public (to let other people know your availability), some inappropriate information such as specific location and people involved (professors, TAs, etc.) are also disclosed.

This script removes these by automatically deleting all location and description lines from the .ics file provided.

## How to use

Run the script in the same directory as your icalendar.ics file and **ensure the file name is exactly like this**.

Your filtered calendar will be written into a file named filtered_calendar.ics. You can then simply import this file into your preferred calendar service.

Note that importing a .ics file instead of linking the URL, the calendar will not automatically update. If your timetable changes, you will have to repeat this process with the new .ics file.

## Next steps

- [] Include menu to select which fields will be removed 