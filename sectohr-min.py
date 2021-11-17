#Python Program to convert seconds into Hours and Minutes
seconds=int(input("Enter Seconds:"));
hr=seconds/3600
mint=seconds/60
sec=seconds%seconds
print("Hours:",hr,"Minutes:",mint,"Seconds:",sec)
