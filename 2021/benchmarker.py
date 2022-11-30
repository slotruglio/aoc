import time
import os
from datetime import datetime
import subprocess 

start_path = '.' # current directory
options = []
for path,dirs,files in os.walk(start_path):
    for filename in files:
        if filename.count("py") > 0  and filename.count("day") > 0 and path.count("bench") == 0:
            options.append(os.path.join(path,filename))

options.sort()
for i in range(0, len(options)):
    toPrint = ""
    if i < 10:
        toPrint = "{})  {}".format(i, options[i])
    else: toPrint = "{}) {}".format(i, options[i])
    print(toPrint)

choice = int(input("What py do you want to execute? "))
program = options[choice].split('/')[2]
folder = options[choice].split('/')[1]

timex = datetime.now()
print("Execution of:", program)
text = ""
times = []
for i in range(0, 10):
    start = time.time()

    os.chdir(folder)
    tmp = subprocess.check_output(["python", program]).decode("utf-8")
    text += tmp
    os.chdir("..")
    stop = time.time() - start
    times.append(stop)
    print(tmp)
    print("Time of execution[{}]: {}".format(i, stop))

f = open("bench/{}{}.txt".format(program, timex), "a")
f.write(text)
f.write("Average time of execution:{}".format(sum(times)/len(times)))
f.close()
print("Average time of execution: ", sum(times)/len(times))