# Metadata-Error-Reporter
Finds errors in the metadata section of the FreePN blog post markdown files

## How to run:
### Place the file in the same folder as the .md files. There can be more than 1 .md file. Double-Tap and it will run and produce three files


The script works is that all the blog articles are stored as .md files in a folder

The script is run and produces three outputs

One is a list of all the files that passed all the tests  (csv file)

One is the list of files that failed at least one test (csv file)

One is a txt file containing the logs for each file, including which tests were failed for which file

There are a total of 11 tests

 1. the first checks that the first line is ''---' 
 2. checks for 'TITLE: '
 3. checks for 'DESCRIPTION: '
 4. checks if the length of description is between 120 and 158 characters
 5. checks for 'AUTHOR: '
 6. checks for 'DATE: '
 7. checks for the data format and if it is all correct in the format yyyy-mm-dd
 8. checks for 'IMAGE: '
 9. checks for '---' in the last line
 10. checks for the blank line between metadata and start of article
 11. checks if heading and title match

