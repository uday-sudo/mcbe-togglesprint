from subprocess import run, PIPE
from time import sleep

def run_out(command_list):
    a=run(command_list,stdout=PIPE,).stdout.decode('utf-8')
    return a

def dn(winid):
    run(['xdotool', 'keyup', '--window', winid, 'ctrl'])  #this line prevents ctrl from bugging out if u switch windows
    run(['xdotool', 'keydown', '--window', winid, 'ctrl'])

def up(winid):
    run(['xdotool', 'keyup', '--window', winid, 'ctrl'])

#getting window id for minecraft
x=input("after pressing enter open minecraft within 5 seconds")
sleep(5)
winkey=run_out(["xdotool","getactivewindow"])
print("the window id for minecraft is:",winkey)

