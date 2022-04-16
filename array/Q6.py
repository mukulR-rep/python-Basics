'''
Write a Python program to get the number of occurrences of a specified element in an array.
'''
from array import *
array_num = array('i', [1,2,3,4,5,6,3,4,3,8,3])
print("Original array: "+str(array_num))
print("Number of occurances of the number 3 in the array: "+str(array_num.count(3)))
