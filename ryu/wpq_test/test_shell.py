import os
import commands

# val = os.system("ls")

status, output = commands.getstatusoutput('sudo whoami')

print status
print output