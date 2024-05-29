# # Day - 1
# # Print Function :
# print("Hello World")  # Output -> Hello World
# print("1.Mix 500g of FLour, 10g Yeast and 300ml Water in a bowl.")
# print("2.Knead the dough for 10 minutes.")
# print("3.Add 3g of Salt.")
# print("4.Leave to rise for 2 hours.")
# print("5. Bake at 200 degrees C for 30 minutes.")
# print('Bro is "best" ')
# print("Bro is \"best\" ")
# print(7)
# print("Hello World!\nHello World!\nHello World!")
# print("Hello " + "Kharthik")
# print("Hello" + "Kharthik")
# print("Hello" + " " + "Kharthik")
# # Input Function:
# input("What is Your name: ")
# input("What is Your Age")
# print("Hello " + input("Enter your name"))
# print(len("Kharthik"))
# print(len(input()))
# print(len(input("Enter the name to get it size")))
# # Variable->Name
# Name = input("Enter the name of the person:")
# print(Name + " is my name")
# Age = 12
# print(Age)
# Age = 19
# print(Age)
# User = input("enter the name")
# print(User + " My name")
# Length = len(User)
# print(Length)  # it is my age:
# Mamitha = input()
# Movie = input()
# Third = Mamitha
# Mamitha = Movie
# Movie = Third
# print("Movie is " + Mamitha)
# print("Name is " + Movie)
# # Project-1: Band name generator
# print("Welcome to the Band name generator")
# Band_name = input("Enter the name of a city where you grew up in your early days?\n")
# Pet_name = input("Enter the name of your pet?\n")
# print("Your Band name is " + Band_name + " " + Pet_name)
# # Day-2
# # Datatypes:
# print("Kharthik"[0])  # Subscripts
# Name1 = "Kharthik"
# print(Name[1])
# print("Hello " + "World")
# print("123" + "456")
# print(123 + 456)  # Addition of two integer numbers
# print(123.454 + 456.796)  # Addition of the float point number
# Boolean = True
# Boolean1 = False  # Boolean type of datatypes
# print(len("12345"))
# Name2 = input("Enter your name")
# Answer = len(Name2)
# print("Your name has " + str(Answer) + " Character")  # Type casting
# print(type(Answer))
# print(type(Name2))
# print(str(200) + str(1927))
# #  Mathematical Operator
# print(3 + 5)  # 8
# print(3 - 5)  # -2
# print(3 * 5)  # 15
# print(3 / 5)  # 0.111
# print(3 ** 5)
# print(3 + 3 * 3 / 3 - 3)  # PEDMAS(Parenthesis,Exponent,Division,Multiplication,Addition,Subtraction)
# #  The operation only can execute from left to right
# # Body Mass Index (BMI)
# print("Welcome to my Body mass index calculator")
# Weight = int(input("Enter your weight in kilogram"))
# Height = int(input("Enter your height in centimeter"))
# Bmi_value = Weight / Height * Height
# print("The Body mass index of your body is " + str(Bmi_value) + " values")
# print("Thank For Using @")
# # Number manipulation and f strings:
# print(round(4.3334, 2))  # round of to the 2 decimal places:
# Result = 78 + 33
# Result += 44
# Marks = 100
# Success = 89
# print(Result)
# print(f'Your Values {Result}, Marks is {Marks}, Success rate is {Success}')  # Fstring used to use various continuous
# # type without the type casting
# # Lifetime calculator:
# Person_age = input()
# Years = 90 - int(Person_age)
# Weeks = Years * 52
# print(f"You have {Weeks} weeks left in your life")
# # Project -1 Tip Calculator:
# print("Welcome to Tip calculator.....")
# Amount = input("Enter the total amount of bill\n")
# Amount = float(Amount)
# Tips = input("Choose the percentage of the tip you want 10, 12 or 15\n")
# Tips = int(Tips)
# People = int(input("How many you want o split your bill amount"))
# Bill = Tips / 100 * Amount
# Amount += Bill
# print(Amount)
# Per_Person = Amount / People
# Final = round(Per_Person, 2)
# Final = "{:.2f}".format(Final)  # {:.2f} Meaning 2 Decimal places
# print(f"Your tip amount per person is {Final}")
# # Day-3:
# # If-Else:
# print("Welcome to Rollercoaster checker")
# Height_person = int(input("Enter your height in cm:\n"))
# if Height_person >= 120:
#     print("You can able to ride")
# else:
#     print("Sorry,You can't able to ride")
# # Even or Odd:
# Num1 = int(input("Enter the number you want here"))
# if Num1 % 2 == 0:  # % gives the remainder of any division
#     print("The given number is even...")
# else:
#     print("The given number is odd...")
# # Nested if-else and elif:
# print("Welcome to Rollercoaster checker")
# Height_person = int(input("Enter your height in cm:\n"))
# Age_person = int(input("Enter your age to get start with rollercoaster"))
# if Height_person >= 120:
#     if Age_person < 12:
#         print("Pay only 5$")
#     elif Age_person < 18:
#         print("Pay only 7$")
#     else:
#         print("Pay only 12$")
# else:
#     print("Sorry,You can't able to ride")
# # Project  -2 Upgraded BMI calculator:
# weight_of_person = int(input("enter the weight of the person in kg"))
# height_of_person = int(input("enter the height of the person in cm"))
# bmi_value = weight_of_person / height_of_person * height_of_person
# if bmi_value < 18.5:
#     print(f"You are underweight with {bmi_value} index")
# elif bmi_value < 25:
#     print(f"You are normal weight with {bmi_value} index")
# elif bmi_value < 30:
#     print(f"You are slightly overweight with {bmi_value} index")
# elif bmi_value < 40:
#     print(f"You are obese with {bmi_value} index")
# else:
#     print("Clinically obese")
# # Leap Year:
# Current_year = int(input("Enter the year to check whether it is leap year or not"))
# if Current_year % 4 == 0:
#     if Current_year % 100 == 0:
#         if Current_year % 400 == 0:
#             print("it is the leap year")
#         else:
#             print("It is not a leap year")
#     else:
#         print("It is an leap year")
# else:
#     print("It is not an leap year")
# # Multiple if statements:
# print("Welcome to Rollercoaster checker")
# Height_person = int(input("Enter your height in cm:\n"))
# Age_person = int(input("Enter your age to get start with rollercoaster"))
# Bill_person = 0
# if Height_person >= 120:
#     if Age_person < 12:
#         Bill_person = 5
#         print(" 5$")
#     elif Age_person < 18:
#         Bill_person = 7
#         print(" 7$")
#     else:
#         Bill_person = 12
#         print(" 12$")
#     Photo = input("Did you want the photo Y or N")
#     if Photo == 'Y':
#         Bill_person += 3
#     print(f"Total Bill you need to pay is {Bill_person}")
# else:
#     print("Sorry,You can't able to ride")
# # Automatic Pizza Order Machine:
# print("Welcome to the automatic pizza order machine ")
# size_of_pizza = input("Enter either the following small,medium or large in small letter")
# add_toppings = input("Enter either the following yes or no in small letter")
# extra_cheese = input("Enter either the following yes or no in small letter")
# bill_of_pizza = 0
# if size_of_pizza == "small":
#     bill_of_pizza += 10
# elif size_of_pizza == "medium":
#     bill_of_pizza += 15
# else:
#     bill_of_pizza += 20
# if add_toppings == "yes":
#     if size_of_pizza == "small":
#         bill_of_pizza += 3
#     elif size_of_pizza == "medium":
#         bill_of_pizza += 5
#     else:
#         bill_of_pizza += 7
# if extra_cheese == "yes":
#     bill_of_pizza += 1
# print(f"Total price to pay for the pizza is {bill_of_pizza}")
# # Logical operator:
# print("Welcome to Rollercoaster checker")
# Height_person = int(input("Enter your height in cm:\n"))
# Age_person = int(input("Enter your age to get start with rollercoaster"))
# Bill_person = 0
# if Height_person >= 120:
#     if Age_person < 12:
#         Bill_person = 5
#         print(" 5$")
#     elif Age_person < 18:
#         Bill_person = 7
#         print(" 7$")
#     elif Age >= 45 and Age <= 55:
#         print("Midlife Crisis Have the free ride to enjoy with us")
#     else:
#         Bill_person = 12
#         print(" 12$")
#     Photo = input("Did you want the photo Y or N")
#     if Photo == 'Y':
#         Bill_person += 3
#     print(f"Total Bill you need to pay is {Bill_person}")
# else:
#     print("Sorry,You can't able to ride")
# # Love Calculator:
# print("The Love Calculator calculating your percentage....")
# person_one = input("Enter the person one name")
# person_second = input("Enter the person two name")
# added_names = person_one + person_second
# added_names = added_names.lower()
# t = added_names.count('t')
# r = added_names.count('r')
# u = added_names.count('u')
# e = added_names.count('e')
# first_digit = t + r + u + e
# l = added_names.count('l')
# o = added_names.count('o')
# v = added_names.count('v')
# e = added_names.count('e')
# second_digits = l + o + v + e
# love_percent = first_digit + second_digits
# if (love_percent < 10) or (love_percent > 90):
#     print(f"You score is {love_percent} You go together like the coke and mentos")
# elif (love_percent >= 40) or (love_percent <= 50):
#     print(f"Your score is {love_percent} you are alright together ")
# else:
#     print(f"You score is {love_percent}")
# # Project-3:
# # Treasure Island:
# print("Welcome to te treasure island game:")
# left_right = input("Enter the way you want to go either right side or left side?\n")
# left_right = left_right.lower()
# if left_right == "left":
#     swim_wait = input("Enter you want to swim or wait?\n")
#     swim_wait = swim_wait.lower()
#     if swim_wait == "wait":
#         blue_yellow_red = input("Pick any one of the color blue,yellow or red?\n")
#         blue_yellow_red = blue_yellow_red.lower()
#         if blue_yellow_red == "yellow":
#             print("You won the treasure island")
#         elif blue_yellow_red == "blue":
#             print("The door didn't exist You lose the game")
#         elif blue_yellow_red == "red":
#             print("Red door hav been destroyed You lose the game")
#         else:
#             print("Failed to open the door You lose the game")
#     else:
#         print("Game Over....You are attacked by the angry trout")
# else:
#     print("Game Over.... You felt into the hole")
# print("Thank for playing......")
# # Day-4:
# # Randomization in Python.
# import random
#
# Random_integer = random.randint(100, 180)
# print(f"The random number generated is {Random_integer}")  # Randomly generate the number in the particular range
# Random_float = random.random()  # print the number between the 0.0 to 1.0
# print(Random_float)
# # if we want to generate number from 1 to 5 not including 5
# number_random_float = Random_float * 5  # it will return between the 1 to 5:
# print(number_random_float)
# # Heads or tails:
# rand_int = random.randint(0, 1)
# if rand_int == 1:
#     print("Heads...")
# else:
#     print("Tails...")
# # List:
# States_of_india = ["Tamilnadu", "Kerala", "Delhi", "Haryana"]  # List can have any datatype and it is ordered
# print(States_of_india)
# print(States_of_india[1])  # Kerala
# print(States_of_india[-3])  # Kerala
# States_of_india[0] = "Tamil nadu"
# print(States_of_india)
# # Append -> Add single item to the end of the list:
# States_of_india.append("Karnataka")
# print(States_of_india)
# States_of_india.extend(["Andra pradesh", "Gujarat", "Madhya pradesh"])  # Combine Two list together
# print(States_of_india)
# # Select random name from list by randomization:
# List_of_name = ["Kharthik", "Lokesh", "Ashwin", "Vishwa", "Sriram"]
# print(List_of_name)
# Number_of_person = len(List_of_name)
# Randomize_person = random.randint(0, Number_of_person - 1)
# print(List_of_name[Randomize_person] + " is need to pay for food today")
# # The above program produce the random person from the list :
# # Nested list and Index Errors:
# list_of_fruits = ["Mango", "Apple", "Grapes", "Guava"]  # Existing index is 3
# #  print(list_of_fruits[12]) -> index error (3) -> 12
# # Nested list :
# Even = [2, 4, 6, 8, 10]
# Odd = [1, 3, 5, 7, 9]
# Even_Odd = [Even, Odd]
# print(Even_Odd)  # Nested list or 2D list.....
# # Project -4 Rock, Paper, Scissors Project:
# print("Welcome to Rock, Paper, Scissor Game.....")
# Stone_Scissors_Stone = ["Scissors", "Stone", "Paper"]
# print(Stone_Scissors_Stone)
# User_choice = input("Enter paper,scissor,stone")
# User_choice = User_choice.lower()
# print(f"Yours Choice is {User_choice}")
# Computer_choice = random.choice(Stone_Scissors_Stone)
# Computer_choice = Computer_choice.lower()
# print(f"The computer choice is {Computer_choice}")
# if Computer_choice == User_choice:
#     print("Draw Match between both of you..")
# elif User_choice == "Scissors":
#     if Computer_choice == "Paper":
#         print("You won the match..")
#     else:
#         print("You Lose the match..")
# elif User_choice == "Paper":
#     if Computer_choice == "Scissors":
#         print("You lose the match..")
#     else:
#         print("You won the match..")
# elif User_choice == "Stone":
#     if Computer_choice == "Paper":
#         print("You lose the match..")
#     else:
#         print("You won the match..")
# print("End of the game....")
# # Day-5:
# # For Loop in Python:
# fruits = ["Pear", "Apple", "Banana"]  # for loop for the list
# for i in fruits:
#     print("The Fruit is ", i)  # Traversal throughout the list fruits from start to end
# for j in "Kharthik":
#     print(j)  # traversal  each and every letter in the word Kharthik :)
#     print("Kharthik as K,h,a,r,t,h,i,k")
# print(fruits)  # ["Pear", "Apple", "Banana"]
# # Find the Highest Element in the list
# Values = input().split()  # Input List elements from the user:)
# for i in range(0, len(Values)):
#     Values[i] = int(Values[i])
# High = 0
# for j in Values:
#     if j > High:
#         High = j
# print(f"The Highest element in the list is {High}")
# # Another Version:
# list_elements = [12, 212, 12212, 33, 12, 121334]
# Highest = 0
# for y in list_elements:
#     if y > Highest:
#         Highest = y
# print(Highest)
# # For Loop for various purpose:
# for p in range(1, 11):  # the End must be n-1
#     print(f"The number is {p}")
# for o in range(11, 3):
#     print(f"The number is {o}")
# sums = 0
# for g in range(1, 11):
#     sum += g
# print(f"The Sum is {sum}")
# # Adding the even numbers:
# Target = int(input("Enter the even number..."))
# total = 0
# for s in range(0, Target + 1, 2):
#     total += s
#     print(f"The total at each of the loop execute {total}")
# print(f"The total  of the even number is {total}")
# # FizzBuzz Job Question:
# end_values = int(input("Enter the number to get the game start..."))
# for l in range(0, end_values + 1):
#     if l % 3 == 0 and l % 5 == 0:
#         print("FizzBuzz...")
#     elif l % 3 == 0:
#         print("Fizz...")
#     elif l % 5 == 0:
#         print("Buzz...")
#     else:
#         print("Sorry That is Wrong...")
# # Project - 6 Password Generator.....
# # Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
# #              'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
# #              's', 't', 'u', 'v', 'w', 'x', 'y',
# #              'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
# #              'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
# #              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# # Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '_']
# # print("Welcome to password generator...")
# # user_letter = int(input("Enter how much letter you need for password:\n"))
# # user_number = int(input("Enter how much numbers you need for password:\n"))
# # user_symbols = int(input("Enter how much symbols you need for password:\n"))
# # Password = ""
# # for bro in range(1, user_letter + 1):
# #     place = random.choice(Alphabets)
# #     Password += place
# # for boys in range(1, user_number + 1):
# #     system = random.choice(Numbers)
# #     Password += system
# # for boys in range(1, user_symbols + 1):
# #     vehicle = random.choice(Symbols)
# #     Password += vehicle
# # Another method:
# Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#              'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#              's', 't', 'u', 'v', 'w', 'x', 'y',
#              'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#              'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
#              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '_']
# print("Welcome to password generator...")
# user_letter = int(input("Enter how much letter you need for password:\n"))
# user_number = int(input("Enter how much numbers you need for password:\n"))
# user_symbols = int(input("Enter how much symbols you need for password:\n"))
# Password = []
# for bro in range(1, user_letter + 1):
#     place = random.choice(Alphabets)
#     Password += place
# for boys in range(1, user_number + 1):
#     system = random.choice(Numbers)
#     Password += system
# for boys in range(1, user_symbols + 1):
#     vehicle = random.choice(Symbols)
#     Password += vehicle
# print(Password)
# random.shuffle(Password)
# print(Password)
# # Use the auditorium Website to practice the challenges and quiz for each and every-lessons ~~~~~~~~~~~~~~~~~~
#
# strong = ""
# for character in Password:
#     strong += character
# print("Password is {strong}")
# # Day-6
# # Functions:
# print("Hello")  # Print() -> Builtin function in python
# length = len("Hello")  # len() -> Length function
# print(len)
#
#
# # Create the user defined function in python:
# def display():  # <Declaration and definition of function>
#     print("Kharthik")
#     print("Code-Chef")
#     print("Leet-code")
#
#
# display()  # <Calling the function>
# # Reeborg World Practice Session
# # Practice Through the website for project~~~~~~~~~~~~~~~~~~~~~~~
#
# # Day-7:
# # Project -7 Hangman Game:

import random
stages = ['''
  |
  0
 /|\
  /\
----------- ''', '''
 |
 0
/|\
 /
''', '''-----------


 |
 0
/|\
''', '''-----------
 |
 0
/|
''', '''------------
 |
 0
 |
''', '''-----------
 |
 0
''', '''-------------
|
''']
List_of_element = ["Race", "Bike", "Car", "Ronaldo"]  # The set of datas that are need to be tested
Chosen_word = random.choice(List_of_element)
Display = []
for _ in range(len(Chosen_word)):  # If we not use the loop variable then we cant need to display that variable
    Display += "_"
print(Display)
end_of_game = False
lives = 6
while not end_of_game:
    Guess = input("Predict the letter?")
    Guess += Guess.lower()
    for position in range(len(Chosen_word)):
        letter = Chosen_word[position]
        if Guess == letter:
            Display[position] = letter
    if Guess not in Chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose....")
    print(Display)
    if "_" not in Display:
        end_of_game = True
        print("You win the game..")
# Use the Software called Thonny Which help us to know the execution of each line of code ~~~~~~~~~~~
# Day 8:
# Functions With Inputs:


def addition(something):  # something is the parameter and Good Afternoon is the argument
    print(str(something) + "Brothers and Sisters")


addition("Good Afternoon")  # Welcome and 100 are also the argument for the function addition
addition("Welcome")
addition(100)
# Positional and keyword argument:


def hangout(lowest, highest):
    print(f"the highest score by rcb is {highest}, and the lowest score is {lowest}")


hangout(highest=262, lowest=49)  # Keyword arguments.


def marks(computer_science, maths, physics):
    print(f"Marks scored in computer science is {computer_science}")
    print(f"Marks scored in maths is {maths}")
    print(f"Marks scored in physics is {physics}")


marks(97, 72, 87)  # Positional arguments -> Sequentially arrange the argument in the function call area.

# Paint area calculator:


def paint_cost(height_of_room, width_of_room, cover):
    total_cans = (height_of_room * width_of_room) / cover
    print(f"Total number of cans need is equal to {total_cans} ")


print("Welcome to Paint Area Calculator...")
Height_of_the_room = int(input("Enter the height of  the room..."))
Width_of_the_room = int(input("Enter the width of the room..."))
Coverage = 5
paint_cost(height_of_room=Height_of_the_room, cover=Coverage, width_of_room=Width_of_the_room)
# Prime Number Checker:


def prime_checker(number_prime):
    is_prime = True
    for i in range(2, number_prime):
        if number_prime % i == 0:
            is_prime = False
    if is_prime:  # It means is_prime == True..
        print(f"The given number {number_prime} is prime number")
    else:
        print(f"The given number {number_prime} is not prime number")


Checking = int(input("Enter the number to test whether it is prime or not..."))
prime_checker(number_prime=Checking)
# Project -8 (Caesar Cipher)
print("Welcome Caesar cipher encryption and decryption.......")
Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']
Decode_encode = input("Enter either decode or encode...")
text_for_decode = input("Type your message").lower()
shift = int(input("Enter the shift number as your wish.."))


def encrypt(plain, shift_number, alphabet):
    cipher_text = ""
    for letter_for_encode in plain:
        positions = alphabet.index(letter_for_encode)  # to find the letter in the list called Alphabets
        new_position = positions + shift_number  # Add the index and the shift number
        new_letter = alphabet[new_position]  # find that letter in the list alphabets
        cipher_text = cipher_text + new_letter  # Cipher text contains the addition of all the new letter
    print(cipher_text)


def decrypt(alphabet, cipher_word, shift_number):
    plainly = ""
    for plainform in cipher_word:
        pose = alphabet.index(plainform)
        new_form = pose - shift_number
        plain_word = alphabet[new_form]
        plainly = plainly + plain_word
    print(plainly)


Loop = True
while Loop:
    # user_favorite = input("Enter you want to continue or not by say yes or no").lower()
    if Decode_encode == "encode":
        encrypt(plain=text_for_decode, shift_number=shift, alphabet=Alphabets)
    else:
        decrypt(alphabet=Alphabets, cipher_word=text_for_decode, shift_number=shift)
    user_favorite = input("Do you want to continue or not by say yes or no").lower()
    if user_favorite == "yes":
        Loop = True
    else:
        Loop = False
# Day- 9 :
# Dictionaries in python:
dict1 = {
    "Age": 12,
    "Name": "Kharthik",
    "Course": "Computer Science",
    "Favourite": "Watching Football"
}
print(dict1["Age"])  # The inside of Square Brackets contains the key of the values
print(dict["Course"])  # The key must be spells correct
# print(dict["age"])  # Return out the key error in the console.
print(dict1.values())
dict1["Interest"] = "Ethical Hacker"
print(dict1.items())
print(dict1.keys())
# If we use for loop to transversal throughout the dictionary then we can get only the key of that certain dictionary
# Nested Lists and the dictionary:
listed_dictionary = {
    "India": {"Visited": ["New Delhi", "Tamil nadu", "Karnataka", "Kerala"], "Population": [12, 121212, 34343]},
    "USA": ["Washington", "Los Angeles", "Nevada"],
    "Russia": "Moscow",
    }
lists_dictionary = [
    {
        "Name": "Kharthik",
        "Age": 13,
        "Place": "USA",
        "Subject": ["Cs", "Math", "Science"],
        "Marks": [122, 233232, 24456, 76787]
    },
]
print(listed_dictionary)
print(lists_dictionary)
print(listed_dictionary.items())
# Project - 9 (Secret Auction Program)
print("Welcome to the Secret Auction Program.....")
print('''
⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡟⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠏⠀⠀⠀⢀⣾⢿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠀⠀⠀⢠⡿⠃⠀⠉⠛⠿⣧⣀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠃⠀⠀⠀⣠⡿⠁⠀⠀⠀⠀⠀⠈⠙⠻⣶⣄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠁⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⡀⢀⣼⣏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⡟⠀⠈⠙⢿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠟⠀⠀⠀⢠⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⠙⠻⣦⣄⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⢠⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠷⣦⣄⠉⣻⣶⣤⣀⠀⢀⣾⠃⠀⠀⠀⣠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⣰⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠁⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')


def highest_bid(record):
    highest_bidder = 0
    for i in record:
        bid_amount = record[i]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = i
    print(f"The winner is {winner} with the bid of {highest_bid}")

bidding = {}
true_or_false = False
while not true_or_false:
    input_name = input("Enter your name...")
    input_bid = int(input("Enter your bidding price"))
    bidding["input_name"] = input_bid
    choices = input("Enter you need a new bidder for the auction say yes/or").lower()
    if choices == "no":
        true_or_false = True
        highest_bid(bidding)
    elif choices == "yes":
        break
# Or using the prebuilt dictionary
# bidding = {"Karthik":121,"Virat":424,"Cristine":457,"Strange":123} an pass  into function instead of lots of lines:
# Day-10:
# Functions With Outputs (return type functions):


def my_function():
    result = 3 * 2
    return result


output = my_function()
print(output)

# Another function for the function with output:


def add(firstname, lastname):
    formly = firstname.title()
    formly1 = lastname.title()
    return f"The firstname is {formly} and the lastname is {formly1}"  '''the return statement used to return the values instead of the values '''


added = add("kharthik", "kumarasamy")
print(added + " is the full name of the person")


def counts(input_string):
    counter = len(input_string)
    return counter


inputs = counts("Karthik")
print(inputs)

# Multiple return keywords in the function :


def multiple_return(surname, mid_name):
    if surname == "" or mid_name == "":
        return "You entered the space character instead of words or letters"
    return "{surname.title()} and {mid_name.title()}"


print(multiple_return(input("Enter your surname:"), input("Enter your middel name:")))
# DocStrings in python:


def runs():
    """
    This program will display the text called Nile is
    the largest river in the entire world
    :return:
    """
    print("Nile is the largest river in the entire world....")


runs()
# Project-10 (Calculator):


def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


choices = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division"
}


def calculation():
    num_1 = float(input("Enter the number one?\n"))
    num_2 = float(input("Enter the number second?\n"))
    for operation in choices:
        print(operation)
    vale = True
    while vale:
        pick = input("Pick anyone of the following operation? \n")
        calculations = choices[pick]
        answer_1 = calculations
        resultant = answer_1(num_1, num_2)
        print(f"{num_1} {calculations} {num_2} = {resultant}")
        again = input("enter  y or no to continue or not")
        if again == 'y':
            num_1 = resultant
        else:
            vale = False
            calculation()


calculation()







