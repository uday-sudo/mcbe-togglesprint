from subprocess import run, PIPE
from time import sleep
from pynput import keyboard

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

#From here starts the listening part
current = set()  #detecting the currently active modifiers
dwon= False
combinations=[
    {keyboard.KeyCode(char='6')},
    {keyboard.KeyCode(char='^')}
]
def on_press(key):
    if key==keyboard.KeyCode(char='6'):
        current.add(key)
        if any(all(k in current for k in i)for i in combinations):
            execute()

def  on_release(key):
    if key==keyboard.KeyCode(char='6'):
        current.remove(key)

def execute():
    global dwon
    if dwon:
        up(winkey)
        print("lifted ctrl")
        dwon = False
    else:
        dn(winkey)
        print("Pressed Ctrl")
        dwon=True

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() #to join listener thread to main thread

