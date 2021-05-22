import subprocess
from time import sleep

def run_out(command_list):
    a=subprocess.run(command_list,stdout=subprocess.PIPE,).stdout.decode('utf-8')
    return a

def dn(a):
    subprocess.run(['xdotool', 'keyup', '--window', a, 'ctrl'])  #this line prevents ctrl from bugging out if u switch windows
    subprocess.run(['xdotool', 'keydown', '--window', a, 'ctrl'])

def up(a):
    subprocess.run(['xdotool', 'keyup', '--window', a, 'ctrl'])

#getting window id for minecraft
x=input("after pressing enter open minecraft within 5 seconds")
time.sleep(5)
winkey=run_out(["xdotool","getactivewindow"])
print("the window id for minecraft is:",winkey)

