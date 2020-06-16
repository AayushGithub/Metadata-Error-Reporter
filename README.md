# Metadata-Error-Reporter
Finds errors in the metadata section of the FreePN blog post markdown files

The script works is that all the blog articles are stored as .md files in a folder
the script is run and produces three outputs
one is a list of all the files that passed all the tests  (csv file)
one is the list of files that failed atleast one test (csv file)
one is a txt file containing the logs for each file, including which tests were failed for which file

there are a total of 11 tests
the first checks that the first line is ''---'
next, checks for 'TITLE: '
next checks for 'DESCRIPTION: '
next checks for the length of description is between 120 and 158 characters (a few failed this test)
next checks for 'AUTHOR: '
next checks for 'DATE: '
next checks for the data format and if it is all correct in the format yyyy-mm-dd (some failed this)
next checks for 'IMAGE: '
next checks for '---' in the last line
next checks for the blank line between metadata and start of article
finally it checks if heading and title match

