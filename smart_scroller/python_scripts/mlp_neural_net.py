#!/usr/bin/env python3
from sklearn.neural_network import MLPClassifier
import csv
import numpy as np

X = [[0 for i in range(39)] for i in range(1000)]
X = np.array(X)
X.reshape(1,-1)
y = []
actual_scroll_times = [0 for i in range(1000)]

i=0
with open('../data_files/synthetic_data1.csv', mode='r') as READ_FILE:
    reader = csv.reader(READ_FILE)
    for line in reader:
        y.append(int(float(line[40])))
        for j in range(39):
            X[i][j] = float(line[j])
        i+=1
READ_FILE.close()

print(X)
print(y)
j=0
clf = MLPClassifier()
print(clf.fit(X, y))
with open('../data_files/synthetic_data2.csv', mode='r') as READ_FILE:
    with open('../data_files/neural_net_predictions.txt', mode='w') as WRITE_FILE:
        reader = csv.reader(READ_FILE)
        for line in reader:
            actual_scroll_times[j] = line[40]
            WRITE_FILE.write(str(clf.predict([float(line[0]),float(line[1]),float(line[2]),
            float(line[3]),float(line[4]),float(line[5]),float(line[6]),
            float(line[7]),float(line[8]),float(line[9]),float(line[10]),
            float(line[11]),float(line[12]),float(line[13]),float(line[14]),
            float(line[15]),float(line[16]),float(line[17]),float(line[18]),
            float(line[19]),float(line[20]),float(line[21]),float(line[22]),
            float(line[23]),float(line[24]),float(line[25]),float(line[26]),
            float(line[27]),float(line[28]),float(line[29]),float(line[30]),
            float(line[31]),float(line[32]),float(line[33]),float(line[34]),
            float(line[35]),float(line[36]),float(line[37]),float(line[38])])))
            WRITE_FILE.write("\n")
            j+=1
    WRITE_FILE.close()
READ_FILE.close()

with open('../data_files/neural_net_actual.txt', mode='w') as WRITE_FILE:
    for i in range(1000):
        WRITE_FILE.write(str(actual_scroll_times[i]))
        WRITE_FILE.write("\n")
WRITE_FILE.close()


# print(X)
# print(y)

# X = [[0., 0.], [1., 1.]]
# y = [0, 1]
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
# print(clf.fit(X, y))
# print(clf.predict([[2., 2.], [-1., -2.]]))
