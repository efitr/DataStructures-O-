import random
import sys


def histogram(source_text):
    histogram = {}
    for word in source_text:
        for word not in histogram:
            histogram[word] += 1
    return histogram

def unique_words(histogram):
    unique_word = []
    for key,value in items():
        print("The key is {} and val is {}".format(key,val))
    return True  

if __name__ == '__main__':
    source= ['one','fish','two', 'fish','red', 'fish','blue','fish']
    histo= histogram(source)
    print(histo)