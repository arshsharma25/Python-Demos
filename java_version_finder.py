import subprocess
cmd = "java --version"


sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()


if rc == 0:
    for each_line in out.splitlines():
        if "openjdk" in each_line:
            print(each_line.split()[1])
else:
    print(err)







