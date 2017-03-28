#!/usr/bin/env python3
# compares the neural net predicted values with the actual scroll times
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

predicted = [0 for i in range(1000)]
actual = [0 for i in range(1000)]
difference = [0 for i in range(1000)]

i=0
with open('../data_files/neural_net_actual.txt', mode='r') as READ_FILE:
    for line in READ_FILE:
        actual[i] = float(line)
        i+=1
READ_FILE.close()

j=0
with open('../data_files/neural_net_predictions.txt', mode='r') as READ_FILE:
    for line in READ_FILE:
        line_str = str(line)
        line_str = re.sub("\]", '', line_str)
        line_str = re.sub("\[", '', line_str)
        line_str = re.sub("\n", "", line_str)
        predicted[j] = float(line_str)
        j+=1
READ_FILE.close()

# print(actual)
# print(predicted)

for i in range(1000):
    difference[i] = round(actual[i] - predicted[i],8)

print(np.mean(difference))
print(np.std(difference))

bins = np.arange(-3000,3000,50)
plt.xlim([min(difference)-400, max(difference)+200])
plt.hist(difference, bins=bins, color='red')
plt.xlabel('difference in predicted and actual')
plt.ylabel('probablility')
plt.title('neural net accuracy distribution')
plt.grid(True)
plt.show()
