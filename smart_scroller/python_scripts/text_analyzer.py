#!/usr/bin/env python3
import sys
import os
import re
import csv
import numpy as np

#---------------------------------------------------------------
#                Data to be collected per section
# (1-3) number of phrases
# (4-6) number of total words
# (7-9) words per phrase (2/1)
# (10-12) number of non-function words
# (13-15) non-function words per phrase (4/1)
# (16-18) mean of total words
# (19-21) std. dev. of total words
# (22-24) mean of non-function words
# (25-27) std. dev. of non-function words
# (28-30) mean of ln(word frequency) (total words)
# (31-33) std. dev. of ln(word frequency) (total words)
# (34-36) mean of ln(word frequency) (non-function words)
# (37-39) std. dev. of ln(word frequency) (non-function words)
# (40) constant term = 1
# (41) scroll time for the current page based on a gamma dist.
#---------------------------------------------------------------


# checking that a file is being passed from command line
if(len(sys.argv) != 2):
    print ("improper usage, please use the following command")
    print("./text_analyzer.py file.txt")
    quit()

# checking file path
if (not os.path.isfile(sys.argv[1])):
    print("this is not right, please use a valid file")
    quit()

# reading file into memory
with open(sys.argv[1], mode = 'r') as READ_FILE:
    file_text = READ_FILE.read()
    word_file_text = READ_FILE.read()
READ_FILE.close()

# this will store all the values we want to retain
results = []

# parsing text for Mr., Mrs., Dr., Sr. to remove the periods
# also taking out punctuation that we dont care about (,-'")
file_text = file_text.lower()
file_text = re.sub("mr\.", "mr", file_text)
file_text = re.sub("mrs\.", "mrs", file_text)
file_text = re.sub("dr\.", "dr", file_text)
file_text = re.sub("sr\.", "sr", file_text)
file_text = re.sub(",", "", file_text)
file_text = re.sub("\"", "", file_text)
file_text = re.sub("-", "", file_text)
file_text = re.sub("\'", "", file_text)
file_text = re.sub("\s+", ' ', file_text)
# probably more abreviations and punctuation would be useful here

# break file into words (default delimitor for split is space)
file_text = file_text.split()

# getting the number of phrases (words ending in .:;?!)
phrase_counter = 0
for word in file_text:
    if ('.' in word or ';' in word or ':' in word or "?" in word or "!" in word):
        phrase_counter+=1
# print(phrase_co?unter, 'phrases')

# using the total number of phrases we will break the text into sections
phrase_divider_remainder = phrase_counter % 3
phrase_divider = phrase_counter // 3

# initialize sections
section1 = ''
section2 = ''
section3 = ''

#this loop iterates through the text and divides it into 3
phrase_index = 0
for word in file_text:
    if ('.' in word or ';' in word or ':' in word or "?" in word or "!" in word):
        phrase_index+=1
    if(phrase_index <= phrase_divider):
        section1 += word
        section1 += ' '
    # i chose to add the remainder phrases to the middle section
    elif(phrase_index > phrase_divider and
         phrase_index <= 2*phrase_divider + phrase_divider_remainder):
        section2 += word
        section2 += ' '
    else:
        section3 += word
        section3 += ' '

# number of phrases in each section --- data points (1-3)
results.append(phrase_divider)
results.append(phrase_divider + phrase_divider_remainder)
results.append(phrase_divider)

# parsing out the remaining punctuation (.:;!?)
section1 = re.sub("\.", "", section1)
section1 = re.sub("\;", "", section1)
section1 = re.sub("\:", "", section1)
section1 = re.sub("\?", "", section1)
section1 = re.sub("!", "", section1)
section2 = re.sub("\.", "", section2)
section2 = re.sub("\;", "", section2)
section2 = re.sub("\:", "", section2)
section2 = re.sub("\?", "", section2)
section2 = re.sub("!", "", section2)
section3 = re.sub("\.", "", section3)
section3 = re.sub("\;", "", section3)
section3 = re.sub("\:", "", section3)
section3 = re.sub("\?", "", section3)
section3 = re.sub("!", "", section3)

# changing from letters to words
section1 = section1.split()
section2 = section2.split()
section3 = section3.split()

# number of words in each section --- data points (4-6)
results.append(len(section1))
results.append(len(section2))
results.append(len(section3))

# number of words per phrase --- data points (7-9)
results.append(round(results[3]/results[0],4))
results.append(round(results[4]/results[1],4))
results.append(round(results[5]/results[2],4))

# counting non function words
non_function_section1 = 0
non_function_section2 = 0
non_function_section3 = 0

# storing non-function words in a list (for data points (22-27, 34-39))
non_function_list_section1 = []
non_function_list_section2 = []
non_function_list_section3 = []

# ignoring [the, and, a, of, or, in, so ...] more function words probably
for word in section1:
    if(word =='the' or word == 'and' or word =='a' or word =='of' or
        word =='or' or word =='in' or word =='so'):
        pass
    else:
        non_function_section1+=1
        non_function_list_section1.append(word)
for word in section2:
    if(word =='the' or word == 'and' or word =='a' or word =='of' or
        word =='or' or word =='in' or word =='so'):
        pass
    else:
        non_function_section2+=1
        non_function_list_section2.append(word)
for word in section3:
    if(word =='the' or word == 'and' or word =='a' or word =='of' or
        word =='or' or word =='in' or word =='so'):
        pass
    else:
        non_function_section3+=1
        non_function_list_section3.append(word)

# number of non function words --- data points (10-12)
results.append(non_function_section1)
results.append(non_function_section2)
results.append(non_function_section3)

# number of non-function words per phrase --- data points (13-15)
results.append(round(results[9]/results[0],4))
results.append(round(results[10]/results[1],4))
results.append(round(results[11]/results[2],4))

# putting word length into a list to calc mean and std. dev
word_length_s1 = []
word_length_s2 = []
word_length_s3 = []

# word length stored in list
for word in section1:
    word_length_s1.append(len(word))
for word in section2:
    word_length_s2.append(len(word))
for word in section3:
    word_length_s3.append(len(word))

# average length of word --- data points (16-18)
results.append(float("%.4f" % round(np.mean(word_length_s1),4)))
results.append(float("%.4f" % round(np.mean(word_length_s2),4)))
results.append(float("%.4f" % round(np.mean(word_length_s3),4)))

# std. dev. of word length --- data points(19-21)
results.append(float("%.4f" % round(np.std(word_length_s1),4)))
results.append(float("%.4f" % round(np.std(word_length_s2),4)))
results.append(float("%.4f" % round(np.std(word_length_s3),4)))

#putting non function words lengths into a list
non_func_word_length_s1 = []
non_func_word_length_s2 = []
non_func_word_length_s3 = []

# putting non-fucntion words length into a list to calc mean and std. dev
for word in non_function_list_section1:
    non_func_word_length_s1.append(len(word))
for word in non_function_list_section2:
    non_func_word_length_s2.append(len(word))
for word in non_function_list_section3:
    non_func_word_length_s3.append(len(word))

# average length of non func word --- data points (22-24)
results.append(float("%.4f" % round(np.mean(non_func_word_length_s1),4)))
results.append(float("%.4f" % round(np.mean(non_func_word_length_s2),4)))
results.append(float("%.4f" % round(np.mean(non_func_word_length_s3),4)))

# std. dev. of non func word length --- data points(25-27)
results.append(float("%.4f" % round(np.std(non_func_word_length_s1),4)))
results.append(float("%.4f" % round(np.std(non_func_word_length_s2),4)))
results.append(float("%.4f" % round(np.std(non_func_word_length_s3),4)))

# this is where we will store word freq data
word_freq_list = [[0 for i in range(3)] for i in range(2500)]

# reading in data from file
i = 0
with open('../data_files/word_freq.csv', mode='r') as READ_FILE:
    reader = csv.reader(READ_FILE)
    for line in reader:
        word_freq_list[i][0] = line[0]
        word_freq_list[i][1] = line[1]
        word_freq_list[i][2] = line[2]
        i+=1
READ_FILE.close()

# making a list of the word frequencies
word_freq_list_s1 = []
word_freq_list_s2 = []
word_freq_list_s3 = []

# adding the frequencies
for word in section1:
    for i in word_freq_list:
        if(word == i[1]):
            word_freq_list_s1.append(int(i[2]))
for word in section2:
    for i in word_freq_list:
        if(word == i[1]):
            word_freq_list_s2.append(int(i[2]))
for word in section3:
    for i in word_freq_list:
        if(word == i[1]):
            word_freq_list_s3.append(int(i[2]))

# filling in the words that werent found with small frequencies
while(len(section1) != len(word_freq_list_s1)):
    word_freq_list_s1.append(10000)
while(len(section2) != len(word_freq_list_s2)):
    word_freq_list_s2.append(10000)
while(len(section3) != len(word_freq_list_s3)):
    word_freq_list_s3.append(10000)

# changing the list from frequeny to ln(frequency)
for i in range(len(word_freq_list_s1)):
    word_freq_list_s1[i] = float("%.4f" % np.log(word_freq_list_s1[i]))
for i in range(len(word_freq_list_s2)):
    word_freq_list_s2[i] = float("%.4f" % np.log(word_freq_list_s2[i]))
for i in range(len(word_freq_list_s3)):
    word_freq_list_s3[i] = float("%.4f" % np.log(word_freq_list_s3[i]))

# average ln(word freq) --- data points (28-30)
results.append(float("%.4f" % round(np.mean(word_freq_list_s1),4)))
results.append(float("%.4f" % round(np.mean(word_freq_list_s2),4)))
results.append(float("%.4f" % round(np.mean(word_freq_list_s3),4)))

# std. dev. of ln(word freq) --- data points(31-33)
results.append(float("%.4f" % round(np.std(word_freq_list_s1),4)))
results.append(float("%.4f" % round(np.std(word_freq_list_s2),4)))
results.append(float("%.4f" % round(np.std(word_freq_list_s3),4)))

# making a list of the word frequencies
word_freq_list_nonf_s1 = []
word_freq_list_nonf_s2 = []
word_freq_list_nonf_s3 = []

# adding the frequencies
for word in non_function_list_section1:
    for i in word_freq_list:
        if(word == i[1]):
            word_freq_list_nonf_s1.append(int(i[2]))
for word in non_function_list_section2:
    for i in word_freq_list:
        if(word == i[1]):
            word_freq_list_nonf_s2.append(int(i[2]))
for word in non_function_list_section3:
    for i in word_freq_list:
        if(word == i[1]):
            word_freq_list_nonf_s3.append(int(i[2]))

# filling in the words that werent found with small frequencies
while(len(non_function_list_section1) != len(word_freq_list_nonf_s1)):
    word_freq_list_nonf_s1.append(10000)
while(len(non_function_list_section2) != len(word_freq_list_nonf_s2)):
    word_freq_list_nonf_s2.append(10000)
while(len(non_function_list_section3) != len(word_freq_list_nonf_s3)):
    word_freq_list_nonf_s3.append(10000)

# changing the list from frequeny to ln(frequency)
for i in range(len(word_freq_list_nonf_s1)):
    word_freq_list_nonf_s1[i] = float("%.4f" % np.log(word_freq_list_nonf_s1[i]))
for i in range(len(word_freq_list_nonf_s2)):
    word_freq_list_nonf_s2[i] = float("%.4f" % np.log(word_freq_list_nonf_s2[i]))
for i in range(len(word_freq_list_nonf_s3)):
    word_freq_list_nonf_s3[i] = float("%.4f" % np.log(word_freq_list_nonf_s3[i]))

# average ln(word freq- non f words) --- data points (34-36)
results.append(float("%.4f" % round(np.mean(word_freq_list_nonf_s1),4)))
results.append(float("%.4f" % round(np.mean(word_freq_list_nonf_s2),4)))
results.append(float("%.4f" % round(np.mean(word_freq_list_nonf_s3),4)))

# std. dev. of ln(word freq non f words) --- data points(37-39)
results.append(float("%.4f" % round(np.std(word_freq_list_nonf_s1),4)))
results.append(float("%.4f" % round(np.std(word_freq_list_nonf_s2),4)))
results.append(float("%.4f" % round(np.std(word_freq_list_nonf_s3),4)))

# print(results)
data_labels = ['num. phrases', 'num. words', 'word per phrase', 'num. non func. words',
                'non func. words per phrase', 'mean word length', 'std. dev. word length',
                'mean non func. word length', 'std. dev. non func. word length', 'mean log word freq.',
                'std. dev. log word freq', 'mean log non func. word freq', 'std. dev. log non func. word freq.']

print("---------------------------------------------------------------------------------------------")
print("----------------------------------- file being analyzed -------------------------------------")
print("---------------------------------------------------------------------------------------------")
print("---------------------------------------- results --------------------------------------------")
print("---------------------------------------------------------------------------------------------")
for i in range(13):
    print("| {3:<35} | {0:<15} | {1:<15} | {2:<15} |".format(results[i*3], results[i*3+1],
     results[i*3+2], data_labels[i]))

print("---------------------------------------------------------------------------------------------")
