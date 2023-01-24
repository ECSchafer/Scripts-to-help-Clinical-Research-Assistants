# Scripts to help Clinical Research Assistants

*This is just to showcase some of my code*

A couple example scripts I wrote to help save time for the clinical research assistants in my lab

# Clinical Notes Reformatting Script

The Clinical Research Assistants requested the clinical notes for a list of individuals. They got back a single .txt file that included all the clinical notes for every individual requested. The file was in a horrondous format that they could not easily import to excel. The format looked something like:

[report start] 
Header 

Note 

[report end]

[report start]
Header

Note

[report end]

I wrote a script to reformat each header and note into a '`' separated line that could be imported into excel.


# pQCT Script

This script generates a new spreadsheet with visit data for each patient and visit date by pulling values from up to 5 spreadsheets. The 5 spreadsheets have very similar columns but we only want specific values from each spreadsheet. The script will pull the relevant values from each spreadsheet and merge them by patient and visit date. The clinical research assistants used to manually do this.  
