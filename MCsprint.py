import subprocess
import time

def run_out(command_list):
    a=subprocess.run(command_list,stdout=subprocess.PIPE,).stdout.decode('utf-8')
    return a

#name=input("Enter title of app:")

time.sleep(6)
doit= run_out(["xdotool","key","r"])
print('''------------------------------------------------------
------------------------------------------------------''')
print(doit)