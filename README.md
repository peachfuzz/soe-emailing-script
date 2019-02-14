# soe-emailing-script
A script to automate email sending

This script should be placed in a directory. In that directory, the script will find all the files in that directory and send them to the appropriate person. 
The file names should be formatted like so:
<username>_<date the file was changed>_<file contents>
Example: bob_1-1-19_financial-document
Note: The <username>, <date the file was changed>, and <file contents> must be separated by an underscore ("_"). This script will not work if the format is not correctly done. 

For example, a person places the script in documents/email-files. In that directory, there are the following files: bob_1-2-19_file, bill_1-3-19, betty_1-1-19_file. The script will send bob_1-2-19_file to bob@spu.edu with the subject "file 1-2-19" and the master message. This happens for all the files within the directory.

Double click to run will be enabled soon. 

Any questions, please direct them to Hector. 
