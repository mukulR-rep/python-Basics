'''
Write a Python program to append items from inerrable to the end of the array.
'''
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
array_num.extend(array_num)
print("Extended array: "+str(array_num))

