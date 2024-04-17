#Random Generate of number and choices etc;
import random
x= random.randint(1,6) #random integer between  1 and 6 randint() (Whole number)
print(x) #return the random number between 1 and 6
y=random.random() #allow decimal number not support arguments
print(y) #return random number either 0 or 1 random()
myList = ["Rock","Paper","Scissors"]
Result = random.choice(myList) #randomly display the values in the list named myList
print(Result)
Cards = [0,1,2,3,4,5,6,7,8,9,'K','Q','J']
random.shuffle(Cards) #shuffle() dont need the variable to display list variable is enough
print(Cards)
#Exception Handling in Python with example
#try: block -> used to keep the vulnerability part inside this block
#except : block -> used as the incidator for error occuring in your program
#if there is no error occurs then execute the else part
try:
    Number1 = int(input("Enter the number to get divided"))
    Number2 = int(input("Enter the divisor number to get divide the above number"))
    Final = Number1/Number2
except TypeError as a:
    print("You encounter the following error called as",a)
    print("You entered the different type in the console")
except ZeroDivisionError as b:
    print("You encounter the following error called as",b)
    print("Zero cannot divide any number sorry enter different number")
except Exception as e :
    print("name ->",e)
    print("Sorry something went wrong")
else:
    print("The Result of the {} / {}".format(Number1,Number2)," "," is",Final)
#OS Module in Python Simple File Detection
"""""
*os.path.exists() -> return there is is the existance of path
*os.path.isfile() ->return there is the file if true
*os.path.isdir() ->return it is folder not the file
"""""
import os
Location = "C:\\Users\\Khart\\Downloads"
if os.path.exists(Location):
    print("there is the path is still existing")
    if os.path.isfile(Location):
        print("that is the file")
    elif os.path.isdir(Location):
        print("it is not the file that is a folder")
else:
    print("No directory or no location in this name is exists")
# Reading the data from the file in python
with open("name.txt") as File: #this with open() is very crucial line in reading a file
    print(File.read())
#incase if there is no file found use the exception handling to avoid the error
try:
    with open("name.txt") as Good:
        print(Good.read())
except FileNotFoundError as y:
    print("The eror is called as",y)
    print("Still file is not found bro")#Same program but the different is EXCEPTION HANDLING
#Write the content in file
Content = "Kharthik Omkar \n My Favorite footballer is Ronaldo and \nFavorite Cricketer is Virat kohli"
with open("name.txt",'w') as Great: # also w->write and a->append
    Great.write(Content) #this can be also use the exception method or way
#Copy the file to another
import shutil
shutil.copyfile("name.txt","copied.txt") #copy the source to destination file that (source,destination)
#copyfile()^
shutil.copy("name.txt","copy.txt")
shutil.copy2("name.txt","coffee.txt")
#Move the file in python
source = "name.txt"
destination = "C:\\Users\\Khart"
try:
    if  os.path.exists(destination):
        print("There is already the file here")
    else:
        os.replace(source,destination)
        print("Successfully moved")
except FileNotFoundError as a:
    print(a)
    print("The denoted File is not found Sorry Bro")
#Delete the file
import os
#the name of the file is based on the two thing
#1->file is present in the folder itself then only name enough
#2->if the file is present in the system then only path is needed
#Just add the exception to avoid the error
try:
    os.remove("nam.txt") #i enter the name.txt then the file must delete
except FileNotFoundError as p:
    print("The file is found that is",p)
    print("file is not found sorry")
else:
    print("the file is deleted ")
#Module usage: here i create the file in the same directory and the module is used in there
import BasicS #we can also rename the module name by using "as" and then we can also do from module import function
BasicS.Run()
BasicS.Display() #BasicS denoted the module and the Run()and Display() denoted the function
help("modules") #used to know the sets of modules available in python

