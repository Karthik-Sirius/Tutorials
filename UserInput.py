#Getting user inputs
name = input("Enter the name of the person?") #Always the the input() used to give  the string type data
print(name)
print(type(name))
Age= int(input("Enter the Age of the person?")) #default type is string so typecast it for required one
print(Age)
print(type(Age))
Weight = float(input("Enter the weight of the person of the person ?"))
print(Weight)
print(type(Weight))
print("Hi my name is",name,"and i'm" ,Age,"old"," with Weight of",Weight)
#math function from the math package
number = 2
number1 = 2.433
number2 = 4
number3 = -14
print(min(number,number1,number2))
print(max(number,number1,number2))
print(round(number1))
print(pow(number,number2))
print(abs(number3))
import math #math is the package which has the n number of functions to perform various mathematical operations
print(math.ceil(number1))
print(math.floor(number1))
print(math.sqrt(number2))
#Sting slicing (used to get the substring from the main string)
Name = input("Enter the name to get the substring from the mainstring")
print(Name)
print(Name[0]) #index to access the string literal
length=len(Name)
print(Name[0:length+1:1])
print(Name[::-1])
print(Name[0:])
print(Name[:length+1])
print(Name[::2])
#slice() function
Foods = "RoyalChallengersBengaluru"
Finally = slice(17,-3)
print(Foods[Finally])
#if,elif and else statements
User_amount = int(input("The amount you have in your packet rightnow :"))
print(User_amount)
if User_amount>100:
    print("You can buy things in the shop as your wish")
elif User_amount>50:
    print("You can buy the things that may cost morethan 50 ")
elif User_amount<50:
    print("You can buy the things that cost less than 50")
else:
    print("You are having less than the least amount sorry")

climate = "summer"
if climate == "summer":
    print("it is summmer so go out and enjoy")
elif climate =="rain":
    print("blow and beatiful season to live in chennai")
elif climate =="thunderstorm":
    print("be calm and safe")
else:
    print("not to say nothing about the temperature")
#logical operator (and,or,not)
#and - both the statement need to be true to get the input as true
#or - one of the statement is true then we will get the input as true
#not - complements of the statement
Stuff = 199
if Stuff>0 and Stuff<25:
    print("the number must be in the range about 0 to 24")
elif Stuff>0 or Stuff<30:
    print("it is either be the number greater than 0 or the number less than 30")
elif not(Stuff>100):
    print("the number must be not greater than 100 i can tell it truly")
else:
    print("the number is doubted for the range and also for the not equal to 100 and greater than 0 and less than 30")