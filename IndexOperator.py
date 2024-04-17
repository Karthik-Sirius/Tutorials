#Index Operator -> []
Full_Name = "kharthik Omkar"
if Full_Name[0].islower():
    Full_Name = Full_Name.upper()
print(Full_Name)
First_name = Full_Name[:8].lower()
Last_name = Full_Name[9:].lower()
Last_character = Full_Name[-1]
print(First_name)
print(Last_name)
print(Last_character)
print(Full_Name[9])
print(Full_Name[5])

#FUNCTIONS
def display():
    print("My name is Kharthik")
display()
display()
#ANother Function
def add():
    a=10
    b=18
    print(f"the additon is {a+b}")
add()
#Parameterized Function
#Create the function where the variables are used from the argument that are get in the function call
def Biography(name,age,weight,height):
    print("I self "+" "+name+"\ni am "+" "+str(age))
    print("The sum of weigth and the height is : ")
    print(f"{weight+height}")
Biography("Kharthik",19,48,178.3) # return the sum as float type data
Biography("Lokesh",20,53,166.9)
#Return statement in function
#define the function as usual inside it dont use the print() instead use return keyword
def DateandTime(date,time):
    Display = date,time
    return Display
Data1 = int(input("Enter the date alone not the month and year"))
Data2 = int(input("Enter the exact hour without the am or pm"))
Result=DateandTime(Data1,Data2)
print("The date and time now is ",Result)
#another example for return statement
def Main(CGPTA):
    if CGPTA == 9.5:
        return "Great"
    else:
        return "Ok"
Show=Main(9.5)
print(Show)
#Positional Argument -> used to put the data in whereever we want
#Create the function and call then pass the argument with the variable specified
def Food(Breakfast,Lunch,Dinner):
    print("My Breakfast is",Breakfast)
    print("My Lunch is ",Lunch)
    print("My Dinner is",Dinner)
Food(Lunch="Biryani",Dinner="Parotta",Breakfast="Poori")
Food(Dinner="Fried Rice",Breakfast="Idly",Lunch="Meal")
#Nested Fuction call
def runner():
    return 12+9
runner() #It is the normal function call where only one function is used for calling
#let us see the nested function call for inbuilt function it is also applicable for user defined function
print(round(abs(float(input("Enter the number to be calculated the value for bunch of function ")))))


