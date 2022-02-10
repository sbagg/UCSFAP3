This is a program in which uses powershell to schedule the task
and run the python script, which will check if:
- There is a CSV file in temp/incoming/ folder
- Parse CSV to exclude particular emailaddress
- Create a new csv with said filters with datetime added
- Send Email of Summary for this Process

Installation:
- Python 3 (This was made with 3.9 in mind)
    - Go to Python Documentation to install in Windows
    - Make sure to install on environment path to use properly
- Pip for easy install
    - python3 -m ensurepip --default-pip
- Pandas Tool
    - py -m pip install pandas



Copy this directory into your powershell workspace and if not 
already done add the CSV file to the temp/incoming folder. 

To start, type the following command: 

.\run_task.ps1

From there a prompt will ask you for your email address for 
later runs.  This will ensure that the scheduled tasks are sent
to the email of choice as well as the for the initial run of 
program.

