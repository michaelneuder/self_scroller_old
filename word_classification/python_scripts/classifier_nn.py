#!/usr/bin/env python3

# ----------------------------------------------------------------------
# trains a neural net with the results from the first half of each text
# uses the second half of the book to test the neural net prediction
# writes the prediction to a text file
# ----------------------------------------------------------------------

from sklearn.neural_network import MLPClassifier
import csv
import numpy as np

# initialize number of iteration counter and feature list
num_iteration_text1 = 0
features = []

# reads in resutls and stores into feature list
with open('../data_files/origin/origin_p1_results.csv', mode='r') as READ_FILE:
    reader = csv.reader(READ_FILE)
    for line in reader:
        if(num_iteration_text1 < 175):
            line_features = [0 for i in range(8)]
            for i in range(8):
                line_features[i] = float(line[i])
            features.append(line_features)
            num_iteration_text1+=1
READ_FILE.close()

# reads in results and stores into feature list
num_iteration_text2 = 0
with open('../data_files/jungle_book/jungle_book_p1_results.csv', mode='r') as READ_FILE:
    reader = csv.reader(READ_FILE)
    for line in reader:
        line_features = [0 for i in range(8)]
        for i in range(8):
            line_features[i] = float(line[i])
        features.append(line_features)
        num_iteration_text2+=1
READ_FILE.close()

# creating a results list
results = []
for i in range(num_iteration_text1):
    results.append(0)
for i in range(num_iteration_text2):
    results.append(1)

# print(features)
# print(num_iteration_text1)
# print(num_iteration_text2)
# print(results)
# print(len(results))

# neural network that seeks to classify which source a passage comes from
clf = MLPClassifier()
print(clf.fit(features, results))
with open("../data_files/jungle_book/jungle_book_p2_results.csv", mode='r') as READ_FILE:
    with open("../results/jungle_book_p2_predictions.txt", mode='w') as WRITE_FILE:
        reader = csv.reader(READ_FILE)
        for line in reader:
            WRITE_FILE.write(str(clf.predict([float(line[0]),float(line[1]),float(line[2]),
            float(line[3]),float(line[4]),float(line[5]),float(line[6]),
            float(line[7])])))
            WRITE_FILE.write("\n")
READ_FILE.close()

with open("../data_files/origin/origin_p2_results.csv", mode='r') as READ_FILE:
    with open("../results/origin_p2_predictions.txt", mode='w') as WRITE_FILE:
        reader = csv.reader(READ_FILE)
        for line in reader:
            WRITE_FILE.write(str(clf.predict([float(line[0]),float(line[1]),float(line[2]),
            float(line[3]),float(line[4]),float(line[5]),float(line[6]),
            float(line[7])])))
            WRITE_FILE.write("\n")
READ_FILE.close()

print(num_iteration_text1)
print(num_iteration_text2)
print(clf.get_params())
