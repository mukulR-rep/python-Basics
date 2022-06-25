"""
def bark():
   print("Woof woof!")
   print("I am a dog")

for i in range(20):
   bark()    
def hello():
    print("Hello Nick")


for x in range(5):
    hello()


#parameters
def hello(name):
    print(f"Hello {name}!")
hello("Mukul")

def add_numbers(num1,num2):
    print(num1 +num2)
add_numbers(7,5)   


def dog_info(age, name):
    print(f"Hi my name is {name} and i am {age} years old")

dog_info(5,"jack")  
"""

#Return
'''
def double(number):
    return number * 2

x = double(9)
print(x)

def uppercase(text):
    return text.upper()
print(uppercase("mukul raghuwanshi"))

names = ['mukul','malay','madhuri','mukesh']
for name in names:
    print(uppercase(name))
'''

#Inputs
'''
user_text = input('enter some text:')
print(user_text.upper())
user_number = input("what do you want to double?")
print(int(user_number) * 2 )
'''
text = input('Enter a text:')
print(text)
user = input("Enter your preffered option:")
if user == "1":
   print(text.upper())
else:
   print(text.lower())