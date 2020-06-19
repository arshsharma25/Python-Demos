import subprocess
import sys


cmd = "dir"

'''
If the cmd is a string, we use shell = True
But if cmd is a list, we use shell = False
eg:
cmd = "dir"
shell = "True"
In the above case, the python will open another shell to execute this process.

cmd = ["dir"]
shell = False --> This is fast due to working in the same shell

In case of windows platform we always need to take shell = True

If we want to work on environment variables then we need to work with shell  = True scenario, otherwise we can work just fine with the other scenario as well.
'''
# We get output in byte if we do not mention the argument universal_newlines = True
sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines = True)

# It is required as the sp will take time, so python adjust itself. The rc will tell us whether the command was successful or unsuccessful
rc = sp.wait()

if rc == 0:
    print("The script is working ... ")
else:
    print(f"The exit status is {rc}. So script was not success")
    sys.exit(rc)

# the output is a tuple of the below command with two arguments
out,err = sp.communicate()

# If we want to get output in list, we use splitlines() function
print(f"The output : \n{out}")
print(f"The error : \n{err}")
