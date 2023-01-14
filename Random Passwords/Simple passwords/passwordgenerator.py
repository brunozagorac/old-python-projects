from art import tprint
import random
import string

print(" ")
print(" ")
tprint("Made by Bruno")
print(" ")
print("Welcome to the password generator. The generated passwords aren't stored anywhere and you can generate as many as you want. ")
print(" ")

#input the desired password length
length = int(input("Enter a length for your password (the API supports lengths below 63): "))

#define what the password consists of
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
number = string.digits

#combine the data
all = lowercase + uppercase + number

#use random
temp = random.sample(all, length)

#compile the password
password = "".join(temp)

#print the password and warnings

print(" ")
print(" ")
print("Your randomly generated password is printed below:")
print(" ")
print(password)
print(" ")
print("Copy the password and close this window immediately. Don't forget to empty your clipboard!")
print(" ")