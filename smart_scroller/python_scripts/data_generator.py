#!/usr/bin/env python3

## random data generation for self scroller
import random
from math import sqrt
import numpy

#---------------------------------------------------------------
#                     Data to be generated
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

def generate_page_data():
    #initialize array for storing data
    num_data_points = 41
    data =[0 for x in range(num_data_points)]

    # generating (1-3) --- using range of 1-4 --- E(X) = 2.5
    data[0] = random.randint(1,4)
    data[1] = random.randint(1,4)
    data[2] = random.randint(1,4)

    # generating (4-6) --- using range of 30-50 --- E(X) = 40
    data[3] = random.randint(30,50)
    data[4] = random.randint(30,50)
    data[5] = random.randint(30,50)

    # generating (7-9) --- dividing (2)/(1) --- E(X) = 16
    data[6] = round((data[3]/data[0]),4)
    data[7] = round((data[4]/data[1]),4)
    data[8] = round((data[5]/data[2]),4)
    #print_data(data_section1, data_section2, data_section3)

    # generating (10-12) --- using range of 15-25 --- E(X) = 20
    data[9] = random.randint(15,25)
    data[10] = random.randint(15,25)
    data[11] = random.randint(15,25)

    # generating (13-15) --- dividing (4)/(1) --- E(X) = 8
    data[12] = round((data[9]/data[0]),4)
    data[13] = round((data[10]/data[1]),4)
    data[14] = round((data[11]/data[2]),4)

    # generating (16-18) --- using range of 3-8 --- E(X) = 5.5
    data[15] = random.randint(3,8)
    data[16] = random.randint(3,8)
    data[17] = random.randint(3,8)

    # generating (19-21) --- using range of 1.5-2.5 --- E(X) = 2
    data[18] = round(random.uniform(1.5,2.5),4)
    data[19] = round(random.uniform(1.5,2.5),4)
    data[20] = round(random.uniform(1.5,2.5),4)

    # generating (22-24) --- using range of 4-9 --- E(X) = 6.5
    data[21] = random.randint(4,9)
    data[22] = random.randint(4,9)
    data[23] = random.randint(4,9)

    # generating (25-27) --- using range of 2-3 --- E(X) = 2.5
    data[24] = round(random.uniform(2.0,3.0),4)
    data[25] = round(random.uniform(2.0,3.0),4)
    data[26] = round(random.uniform(2.0,3.0),4)

    # generating (28-30) --- using range of 11.2-16.6 --- E(X) = 13.9
    data[27] = round(random.uniform(11.2,16.6),4)
    data[28] = round(random.uniform(11.2,16.6),4)
    data[29] = round(random.uniform(11.2,16.6),4)

    # generating (31-33) --- using range of 1.0-2.0 --- E(X) = 1.5
    data[30] = round(random.uniform(1.0,2.0),4)
    data[31] = round(random.uniform(1.0,2.0),4)
    data[32] = round(random.uniform(1.0,2.0),4)

    # generating (34-36) --- using range of 11.2-15.0 --- E(X) = 13.1
    data[33] = round(random.uniform(11.2,15.0),4)
    data[34] = round(random.uniform(11.2,15.0),4)
    data[35] = round(random.uniform(11.2,15.0),4)

    # generating (37-39) --- using range of 1.0-2.0 --- E(X) = 1.5
    data[36] = round(random.uniform(1.0,2.0),4)
    data[37] = round(random.uniform(1.0,2.0),4)
    data[38] = round(random.uniform(1.0,2.0),4)

    # generating(40) = 1
    data[39]=1

    # generating (41) --- in milliseconds
    mean = ((data[0]+data[1]+data[2])*700 # estimating .7 seconds per sentence
    +(data[3]+data[4]+data[5])
    +(data[6]+data[7]+data[8])
    +(data[9]+data[10]+data[11])
    +(data[12]+data[13]+data[14])
    +(data[15]+data[16]+data[17])
    +(data[18]+data[19]+data[20])
    +(data[21]+data[22]+data[23])
    +(data[24]+data[25]+data[26])
    +(data[27]+data[28]+data[29])
    +(data[30]+data[31]+data[32])
    +(data[33]+data[34]+data[35])
    +(data[36]+data[37]+data[38]))

    shape, scale = sqrt(mean), sqrt(mean)
    random_sample = numpy.random.gamma(shape, scale)

    data[40] = round(random_sample,4)

    return data

def main():
    with open("../data_files/synthetic_data2.csv", mode='w') as WRITE_FILE:
        num_iterations = int(input("enter the number of iterations: "))
        i=0
        while(i<num_iterations):
            current_data = generate_page_data()
            current_data_str = ','.join(str(elements) for elements in current_data)
            print(current_data_str)
            # WRITE_FILE.write(current_data_str + "\n")
            i+=1
    WRITE_FILE.close()

    new_data = generate_page_data()
    for i in range(len(new_data)):
        pass
    print("---------------------------------------------------------")
    print("number of iterations producted", str(num_iterations))
    print("number of data points generated per iteration:", str(i+1))
    print("---------------------------------------------------------")

if (__name__ == '__main__'):
    main()
