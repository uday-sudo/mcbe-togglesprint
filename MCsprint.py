import subprocess


def run_out(command_list):
    a=subprocess.run(command_list,stdout=subprocess.PIPE,).stdout.decode('utf-8')
    return a
name=input("Enter title of app:")


doit= run_out(["ls"])
print('''------------------------------------------------------
------------------------------------------------------''')
print(doit)