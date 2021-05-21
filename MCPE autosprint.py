import subprocess

a=subprocess.run(['xdotool','search'],stdout=subprocess.PIPE)
print(a, type(a))