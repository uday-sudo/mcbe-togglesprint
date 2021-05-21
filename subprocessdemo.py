import subprocess

# this runs pwd in terminal(in background i think) and returns an object called CompletedProcess
out=subprocess.run(['pwd'],stdout=subprocess.PIPE)

# this shows format and type the object
print(out , type(out))

# this is how to get output of the command you executed it's in binary format
result=out.stdout
print(result , type(result))

# this is how to convert it to str
str_res=result.decode('utf-8')
print(str_res , type(str_res))

# with the help of power of objects you can turn this into one liner like this
## this returns str in utf-8 format
out=subprocess.run(['pwd'],stdout=subprocess.PIPE).stdout.decode('utf-8')
## this proves it
print(out , type(out))