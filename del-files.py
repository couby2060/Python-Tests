## NOT FINISHED

import os

filelist = [ f for f in os.listdir("read-write-folder/files-to-write/") if f.endswith(".") ]
for f in filelist:
    os.remove(f)