# -*- coding: utf-8 -*-
"""
IDE: Spyder (Python 3.8)
@author: Kevin Tudor
Course: COT 4400: Design and Analysis of Algorithms
Programming 1: Quicksort Algorithm
Due: March 13, 2023 (Monday), 11:59PM
"""
#include libraries
import random

def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)
        
def partition(a, p, r):
    x = a[r]
    i = p - 1

    for  j in range(p, r): #for j = p to r - 1:
        if a[j] <= x:
            i = i + 1
            #swap
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    #swap    
    temp2 = a[i+1]
    a[i+1] = a[r]
    a[r] = temp2
    return i + 1

def rseq(num):
    return random.sample(range(0, num), num)
        
        
def main():
    #a. 10, 80, 3, 19, 14, 7, 5, 12
    a = [10, 80, 3, 19, 14, 7, 5, 12]
    print("Unsorted - GIVEN sequence:\n", a)
    quicksort(a, 0, len(a)-1)
    print("\nSorted - GIVEN sequence: \n",a)
    
    #b. Choose your sequence with 100 different (random) integer numbers
    b = rseq(100)
    print("\nUnsorted - sequence with", len(b), "different (random) integer numbers: \n", b)
    
    quicksort(b, 0, len(b)-1)
    print("\nSorted - sequence with", len(b), "different (random) integer numbers: \n", b)
    
    #c. Choose your sequence with 1000 different (random) integer numbers
    c = rseq(1000)
    print("\nUnsorted - sequence with", len(c), "different (random) integer numbers: \n", c)
    
    quicksort(c, 0, len(c)-1)
    print("\nSorted - sequence with", len(c), "different (random) integer numbers: \n", c)
    
if __name__ == "__main__":
    main()