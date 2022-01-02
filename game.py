import os
import platform
import time
import sys

operation = platform.system()
operversion = platform.release()

if operation == 'Windows':
    cmd = 'mode 100,35'
    os.system(cmd)
elif operation == 'Linux':
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=100, cols=35))
else:
    print("You are on an unsupported operating system.\nMake sure the window is at least 100x35.")
    time.sleep(10)

print(operation + " " + operversion)
print("GPL-v3.0 anarchy-artichokey lonestar84")
time.sleep(3)
