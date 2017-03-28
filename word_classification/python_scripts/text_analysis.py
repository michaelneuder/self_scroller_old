#!/usr/bin/env python3
import sys
import os
import re
import csv
import numpy as np

#---------------------------------------------------------------
#  Data to be collected
# --------------------------------------------------------------
# (1) mean length of total words
# (2) std. dev. of length of total words
# (3) mean length of non-function words
# (4) std. dev. of length of non-function words
# (5) mean of ln(word frequency) (total words)
# (6) std. dev. of ln(word frequency) (total words)
# (7) mean of ln(word frequency) (non-function words)
# (8) std. dev. of ln(word frequency) (non-function words)
#---------------------------------------------------------------


# # checking that a file is being passed from command line
# if(len(sys.argv) != 2):
#     print ("improper usage, please use the following command")
#     print("./text_analysis.py file.txt")
#     quit()
#
# # checking file path
# if (not os.path.isfile(sys.argv[1])):
#     print("this is not right, please use a valid file")
#     quit()
#
# # reading file into memory
# with open(sys.argv[1], mode = 'r') as READ_FILE:
#     file_text = READ_FILE.read()
#     word_file_text = READ_FILE.read()
# READ_FILE.close()

def analyze(text):
    # this will store all the values we want to retain
    results = []

    # parsing text for Mr., Mrs., Dr., Sr. to remove the periods
    # also taking out punctuation that we dont care about (,-'")
    text = text.lower()
    text = re.sub("mr\.", "mr", text)
    text = re.sub("mrs\.", "mrs", text)
    text = re.sub("dr\.", "dr", text)
    text = re.sub("sr\.", "sr", text)
    text = re.sub(",", "", text)
    text = re.sub("\"", "", text)
    text = re.sub("-", "", text)
    text = re.sub("\'", "", text)
    text = re.sub("\s+", ' ', text)
    text = re.sub("\.", "", text)
    text = re.sub("\;", "", text)
    text = re.sub("\:", "", text)
    text = re.sub("\?", "", text)
    text = re.sub("!", "", text)
    # probably more abreviations and punctuation would be useful here

    # break file into words (default delimitor for split is space)
    text = text.split()

    # storing non-function words in a list (for data points (22-27, 34-39))
    non_function_list = []
    non_function_count = 0


    # ignoring [the, and, a, of, or, in, so ...] more function words probably
    for word in text:
        if(word =='the' or word == 'and' or word =='a' or word =='of' or
            word =='or' or word =='in' or word =='so'):
            pass
        else:
            non_function_count+=1
            non_function_list.append(word)

    # putting word length into a list to calc mean and std. dev
    word_length = []

    # word length stored in list
    for word in text:
        word_length.append(len(word))

    # average length of word --- data points (16-18)
    results.append(float("%.4f" % round(np.mean(word_length),4)))

    # std. dev. of word length --- data points(19-21)
    results.append(float("%.4f" % round(np.std(word_length),4)))

    #putting non function words lengths into a list
    non_func_word_length = []

    # putting non-fucntion words length into a list to calc mean and std. dev
    for word in non_function_list:
        non_func_word_length.append(len(word))

    # average length of non func word --- data points (22-24)
    results.append(float("%.4f" % round(np.mean(non_func_word_length),4)))

    # std. dev. of non func word length --- data points(25-27)
    results.append(float("%.4f" % round(np.std(non_func_word_length),4)))

    # this is where we will store word freq data
    word_freq_list = [[0 for i in range(3)] for i in range(2500)]

    # reading in data from file
    i = 0
    with open('../../smart_scroller/data_files/word_freq.csv', mode='r') as READ_FILE:
        reader = csv.reader(READ_FILE)
        for line in reader:
            word_freq_list[i][0] = line[0]
            word_freq_list[i][1] = line[1]
            word_freq_list[i][2] = line[2]
            i+=1
    READ_FILE.close()

    # making a list of the word frequencies
    word_freq_list_on_page = []

    # adding the frequencies
    for word in text:
        for i in word_freq_list:
            if(word == i[1]):
                word_freq_list_on_page.append(int(i[2]))

    # filling in the words that werent found with small frequencies
    if(len(text) > len(word_freq_list_on_page)):
        while(len(text) != len(word_freq_list_on_page)):
            word_freq_list_on_page.append(10000)

    # changing the list from frequeny to ln(frequency)
    for i in range(len(word_freq_list_on_page)):
        word_freq_list_on_page[i] = float("%.4f" % np.log(word_freq_list_on_page[i]))

    # average ln(word freq) --- data points (28-30)
    results.append(float("%.4f" % round(np.mean(word_freq_list_on_page),4)))

    # std. dev. of ln(word freq) --- data points(31-33)
    results.append(float("%.4f" % round(np.std(word_freq_list_on_page),4)))

    # making a list of the word frequencies
    word_freq_list_nonf = []

    # adding the frequencies
    for word in non_function_list:
        for i in word_freq_list:
            if(word == i[1]):
                word_freq_list_nonf.append(int(i[2]))

    # filling in the words that werent found with small frequencies
    if(len(non_function_list) > len(word_freq_list_nonf)):
        while(len(non_function_list) != len(word_freq_list_nonf)):
            word_freq_list_nonf.append(10000)

    # changing the list from frequeny to ln(frequency)
    for i in range(len(word_freq_list_nonf)):
        word_freq_list_nonf[i] = float("%.4f" % np.log(word_freq_list_nonf[i]))

    # average ln(word freq- non f words) --- data points (34-36)
    results.append(float("%.4f" % round(np.mean(word_freq_list_nonf),4)))

    # std. dev. of ln(word freq non f words) --- data points(37-39)
    results.append(float("%.4f" % round(np.std(word_freq_list_nonf),4)))

    # print(results)
    # data_labels = ['mean word length', 'std. dev. word length',
    #                 'mean non func. word length', 'std. dev. non func. word length',
    #                 'mean log word freq.', 'std. dev. log word freq',
    #                 'mean log non func. word freq', 'std. dev. log non func. word freq.']
    #
    # print("---------------------------------------------------------")
    # print("--------------- file being analyzed ---------------------")
    # print("---------------------------------------------------------")
    # print("-------------------- results ----------------------------")
    # print("---------------------------------------------------------")
    # for i in range(8):
    #     print("| {1:<35} | {0:<15} |".format(results[i], data_labels[i]))
    #
    # print("---------------------------------------------------------")
    return(results)

# analyze(file_text)
