import os
import platform

operation = platform.system()
operversion = platform.release()
if operation == 'Windows':
    cmd = 'mode 100,35'
    os.system(cmd)
elif operation == 'Linux':
    print("Youre on linux")
print(operation + " " + operversion)
print("GPL v3 anarchy-artichokey lonestar84")
