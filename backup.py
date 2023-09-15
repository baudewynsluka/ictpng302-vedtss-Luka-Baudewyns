#!/usr/bin/python3

import sys 
import os 
import pathlib
import shutil
from backupcfg import jobs, backupDir
from datetime import datetime

def main():
    argCount = len(sys.argv)
    if not argCount == 2:
        print("ERROR: job not specified")
    else:
        job = sys.argv[1]
        if not job in jobs:
            print(f"ERROR: job {job} does not exist")
        else:
            source =jobs[job]
            if not os.path.exists(source):
                print(f"ERROR: source {source} does not exist")
            else:
                destination = backupDir
                if not os.path.exists(destination):
                    print(f"ERROR: destination {destination} does not exist")
                else:
                    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                    srcPath = pathlib.PurePath(source)
                    dstLoc = destination + "/" + srcPath.name + "-" + dateTimeStamp
                    if pathlib.Path(source).is_dir():
                         shutil.copytree(source, dstLoc)
                    else:
                        shutil.copy2(source, dstLoc)
                    pass

if __name__ == "__main__":
    main()
    