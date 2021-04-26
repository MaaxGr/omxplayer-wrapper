import subprocess
from subprocess import Popen, PIPE
import os
import time
import signal

file_path = "command"

p = None

active = False

while True:
  if not os.path.exists(file_path):
      print("Wait for command...")
      if active:
        time.sleep(0.25)
      else:
        time.sleep(1)
  else:
    file_content = open(file_path, 'r').read()

    if "play" in file_content:
      song = file_content.split(':')[1]
      p = subprocess.Popen(["omxplayer", song],stdin=PIPE,stdout=PIPE,preexec_fn=os.setpgrp)
      os.remove(file_path)
      active = True
    elif file_content == 'stop':
      print('kill')
      os.remove(file_path)
      os.killpg(os.getpgid(p.pid), signal.SIGTERM)
      active = False
    else:
      output = p.stdin.write(file_content.encode())
      p.stdin.flush()
      print('Command:' + file_content )
      os.remove(file_path)
~