name = "Kharthik Omkar"


def DisplayName():
    name = "Karthik"
    print("My name is", name)


DisplayName()  # The output must be Karthik


def DisplayName():
    # name = "Karthik"
    print("My name is", name)


DisplayName()  # The output must be Kharthik Omkar


# Global variable can be access anywhere in the program either inside or outside
# Local varaible can be access only in the local space not in the function rather there is no variable  left

# *args ->argument it is normally used in place where argument are much more then parameter
def Sum(*args):  # List may contain the tuple so not assignment are allowed
    sum = 0  # but we can change it to list and modify it
    for i in args:
        args = list(args)  # Now the Tuple is converted into list to modify the data
        args[0] = 9
        sum = sum + i
    print(sum)


Sum(1, 2, 2, 33, 44)


# Kwargs -> Same like a args but it return dictionary rather then tuple
def Print(**kwargs):
    print("Hello I am", kwargs["Name"], kwargs["Class"], kwargs["Designation"])
    for key, value in kwargs.items():  # This for loop is used to print only the values by iteration
        print(value, end=" ")


Print(Name="Kharthik", Class="BE CSE", Designation="Flutter,Go,Python Developer")
# here Name is the key and Kharthik is the value we need to pass two variable in for loop because it is the dictionary
# String Formatting :
# Just create the variable to show of the str.format() it is just like c language printf and scanf
Cricket = "Virat Kohli"
FootBall = "Cristiano Ronaldo"
print("My favorite cricketer is {} and the footballer is {}".format(Cricket,FootBall))
print("My favorite cricketer is {1} and the footballer is {0}".format(Cricket,FootBall)) #where the 0 and 1 denotes the positional argument
print("My favorite footballer is {AlNassr} and the footballer is {AlHilal}".format(AlNassr = "CR7",AlHilal = "Neymar")) #keywoed argument
#we can also execute like this :
name = "Hi bro i am {} and age is {}"
print(name.format("kharthik",12)) #without initialization of variable like no variable name
#Padding Bro
Letter = "Dude"
print("Hello {:10}".format("Dude"))
print("Hello bro {:>10},Nice to meet you".format(Letter))
print("Hello bro {:<10},Nice to meet you".format(Letter))
print("Hello bro {:^10},Nice to meet you".format(Letter))
number = 1.29192
number1 = 200000
print("the number is {:.3f}".format(number))
print("the number is {:,}".format(number1))
print("the number is {:b}".format(number1))
print("the number is {:X}".format(number1))
print("the number is {:E}".format(number1))
print("the number is {:o}".format(number1))




