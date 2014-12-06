"""python script to backup particular directories to dropbox"""
#!/usr/bin/env python
import os
import time

sources = ["/home/vish/pyfiles"]          # list of source directories
target_dir = "/home/vish/Dropbox/backups"       # target directory where backup is going to stored
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")
target = today + os.sep + now + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

zip_command = "zip -r {0} {1}".format(target, ' '.join(sources))

print "Zip command is:",
print zip_command
print "Running:"
if os.system(zip_command) == 0:
    print "Successful backup to", target
else:
    print "Backup FAILED"