#!/usr/bin/python3

import sys 
import os 
import pathlib
import shutil
import smtplib
from backupcfg import jobs, backupDir, backupLog, smtp
from datetime import datetime

def writeLogMessage(logMessage, dateTimeStamp, isSuccess):
   
    try:
        file = open(backupLog, "a")
        
           # write success or failure message depending upon job outcome
        if isSuccess:
            file.write(f"SUCCESS {dateTimeStamp} {logMessage}\n")
        else:
            file.write(f"FAILURE {dateTimeStamp} {logMessage}\n")
            
        file.close()
        
    except:
        print("ERROR: File.")

def errorHandler(errorMessage, dateTimeStamp):
    print(errorMessage)
    writeLogMessage(errorMessage, dateTimeStamp, False)
    sendEmail(errorMessage)
    
# append all error messages to email and send
def sendEmail(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")
    
    # 
def main():

    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # check for number of CLI arguments
    argCount = len(sys.argv)
    if not argCount == 2:
        #print(f"ERROR: job not specified.")
        errorHandler(f"ERROR: job not specified", dateTimeStamp)
    else:
        # loop through all CLI arguments (jobs)
        for job in sys.argv[1:]:
            # check job is valid i.e. in jobs dictionary
            if not job in jobs:
                errorHandler(f"ERROR: job {job} does not exist", dateTimeStamp)
        else:
            # check job refers to a vaild file or directory
            source =jobs[job]
            if not os.path.exists(source):
                errorHandler(f"ERROR: source {source} does not exist", dateTimeStamp)
            else:
                # check backup location is a valid directory
                destination = backupDir
                if not os.path.exists(destination):
                    print(f"ERROR: destination {destination} does not exist")
                else:
                    srcPath = pathlib.PurePath(source)
                    dstLoc = destination + "/" + srcPath.name + "-" + dateTimeStamp
                    # backup directory or file as required
                    if pathlib.Path(source).is_dir():
                         shutil.copytree(source, dstLoc)
                    else:
                        shutil.copy2(source, dstLoc)
                    
                    
                    #write success to log file
                    writeLogMessage(f"Backed up {source} to {dstLoc}", dateTimeStamp, True)

if __name__ == "__main__":
    main()
    