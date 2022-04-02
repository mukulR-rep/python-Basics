'''Write a Python program to reverse the order of the items in the array'''
from array import *
array = [1,5,9,7,8]
array = array[::-1]
print(array)

from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))
