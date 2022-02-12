##################################################
##################################################
##################################################
##################################################
##################################################
################# Start of Read_File Script
################# 
##################################################
##################################################
##################################################
##################################################

# Import pandas to read CSV to Dataframe
# Import sys for a system exit
# Import datetime for a record of file
# Import smtplib for sending the email

import pandas as pd
import sys
import datetime
import smtplib

###############################################
###############################################
########### Reads a CSV file and filters based
########### on specific email address ending.
########### Then it sends the result to 
########### outgoing folder in the temp folder.
###############################################
###############################################
###############################################
###############################################



# Email Sending Function
def send_email(email, email_info):
    # Start of email curation and connection 
    gmail_user = 'smtp_server' # server location for smtp
    gmail_password = 'password'# authentication


    # Formatting the Message
    sent_from = gmail_user
    to = email
    subject = 'CSV Summary Data'
    body = """
           Job-run Date: %s
           Job-run Time: %s
           Total number of entries in the file: %i
           Number of entries moved to c:/temp/outgoing: %i
           """ % (email_info["date"], email_info["time"], email_info["start_entry"], email_info["end_entry"])

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), 'CSV Summary Data', body)

    # Tries to econnect to the smtp server and send from the 
    # email made.
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email Sent to ", email)
    except Exception as ex:
        print ("Something went wrong….",ex)

# Main function runs
if __name__ == '__main__':

    email = sys.argv[1:]
    # It tries to read csv and if it fails it 
    # exits gracefully
    try: 
        df = pd.read_csv("temp/incoming/users.csv")
    except FileNotFoundError:
        print("There is no file to process")
        sys.exit(0)

    # Filters with the dataframe functions based on if
    # it has @abc.edu
    dff = df[df['emailaddress'].str.contains("@abc.edu")]

    # Checks if dataframe is empty from filtering so
    # exits gracefully
    if dff.empty:
        print('Nothing to move')
        sys.exit(0)
    
    # Gets current datetime and formats it for file
    # record
    x = datetime.datetime.now()
    date_time = x.strftime("%Y%d%m%H%M%S")

    email_info = {}

    email_info["date"] = x.strftime("%m/%d/%Y")
    email_info["time"] = x.strftime("%H:%M:%S")
    email_info["start_entry"] = len(df)
    email_info["end_entry"] = len(dff)

    #Pushes out the csv to the outgoing folder
    out_csv = "temp/outgoing/users"+ date_time +".csv"
    dff.to_csv(out_csv, index=False)
    print("CSV is sent to temp/outgoing folder")

    send_email(email, email_info)

##################################################
##################################################
##################################################
##################################################
##################################################
################# End of Read_File Script
################# 
##################################################
##################################################
##################################################
##################################################
