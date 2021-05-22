import subprocess
from time import sleep

def run_out(command_list):
    a=subprocess.run(command_list,stdout=subprocess.PIPE,).stdout.decode('utf-8')
    return a

def k_down():

#getting window id for minecraft
x=input("after pressing enter open minecraft within 5 seconds")
time.sleep(5)
winkey=run_out(["xdotool","getactivewindow"])
print("the window id for minecraft is:",winkey)

