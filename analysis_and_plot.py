#node20.it.leap.com
time=[]
connections=[]
cpu_use=[]
mem_use=[]

import re
from dateutil.parser import parse

with open('test.txt') as f:
    lines=f.readlines();
    add=False
    for line in lines:
        #print(line);
        if 'Date' in line:
            #print line
            #m = re.match(r'.*(\d{2}:\d{2}:\d{2}).*', line)
            m = re.match(r'Date : (.*)', line)
            ttp = parse(m.group(1))
            if ttp >= parse('Mon Sep 4 10:18:19 CST 2017'):
                time.append(ttp);
                add=True
            else:
                add=False
            #print(type(m.group(1)))
        elif 'allconnect' in line and add:
            #print line
            m = re.match(r'.*:(.*)', line);
            connections.append(m.group(1));
        elif 'java' in line and add:
            m = re.split('\s+',line.strip())
            cpu_use.append(m[5])
            mem_use.append(m[11])
print len(time)
print len(connections)
print len(cpu_use)
print len(mem_use)

import matplotlib.dates as mdates
import matplotlib.pylab as plt
fig = plt.figure(figsize=(20,15))

ax1 = fig.add_subplot(111)
ax1.set_title('Node20 MetaStore Connection Status')
con_line = ax1.plot_date(time, connections,'b-', label='connections')
ax1.set_ylabel('Connections')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('Sep%d %H:%m'))
plt.legend()

ax2 = ax1.twinx()  # this is the important function
cpu_line = ax2.plot_date(time, cpu_use, 'g-', label='cpu_usage_percent')
mem_line = ax2.plot_date(time, mem_use, 'r-', label='mem_usage_percent')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('Sep%d %H:%m'))
ax2.set_ylim([0,100])
ax2.set_ylabel('Cpu/Mem Usage')
fig.autofmt_xdate()
plt.legend(loc='upper left')
plt.show()