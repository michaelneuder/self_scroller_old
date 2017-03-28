#!/usr/bin/env python3
# reads in and analyzes data from csv
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

scroll_times = [0 for x in range(10000)]

i=0
with open('../data_files/synthetic_data.csv', mode='r') as READ_FILE:
    reader = csv.reader(READ_FILE)
    for line in reader:
        scroll_times[i] = float(line[40])
        i+=1
READ_FILE.close()

bins = np.arange(0,10000,10)
plt.xlim([min(scroll_times)-400, max(scroll_times)+200])
plt.hist(scroll_times, bins=bins)
plt.xlabel('scroll time')
plt.ylabel('probablility')
plt.title('scroll time distribution')
plt.grid(True)
plt.show()
