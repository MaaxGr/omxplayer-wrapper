import os
import sys

command = sys.argv[1]

cmd = 'echo -n ' + command + ' > command'
os.system(cmd)
