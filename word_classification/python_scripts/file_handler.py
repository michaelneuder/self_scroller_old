#!/usr/bin/env python3

# ---------------------------------------------------------------------
# breaks large text files into chunks of even size (20 lines)
# the text in these chunks are then analyzed and written to a csv file
# ---------------------------------------------------------------------

from text_analysis import analyze
import re

# initialize variables
text_sections = []
index_sections = -1
current_line = 0

# read in text file and break into pieces of 20 lines
with open('../text_files/jungle_book/jungle_book_p2.txt', mode='r') as READ_FILE:
    for line in READ_FILE:
        line = re.sub("\n", '', line)
        if(current_line % 20 == 0):
            index_sections+=1
            text_sections.append(line)
        else:
            text_sections[index_sections] += line
        current_line+=1
READ_FILE.close()

# write numeric results to csv file
with open('../data_files/jungle_book/jungle_book_p2_results.csv', mode='w') as WRITE_FILE:
    for i in range(len(text_sections)):
        results = analyze(text_sections[i])
        results_str = ','.join(str(result) for result in results)
        print(results_str)
        WRITE_FILE.write(results_str + "\n")
WRITE_FILE.close()
