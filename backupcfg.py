#!/usr/bin/python3

jobs = {"job1" : "/home/ec2-user/environment/ictpng302-vedtss-Luka-Baudewyns/test/file1",
        "job2" : "/home/ec2-user/environment/ictpng302-vedtss-Luka-Baudewyns/test/dir1"}
        
backupDir = "/home/ec2-user/environment/ictpng302-vedtss-Luka-Baudewyns/backups"

backupLog = "/home/ec2-user/environment/ictpng302-vedtss-Luka-Baudewyns/backup.log"

smtp = {"sender": "baudewynsluka@gmail.com",
        "recipient": "baudewynsluka@gmail.com",
        "server": "smtp.gmail.com",
        "port": 587,
        "user": "baudewynsluka@gmail.com", # need to specify a gmail email address with an app password
        "password": ""} # need a gmail app password