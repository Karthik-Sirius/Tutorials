#while loop(high chance to get the infinite loop)
condition = 1
while condition<100:
    condition+=1
    print(condition)
Entry = 1
while Entry<10:
    print("hi bro"+ str(Entry))
    Entry+=1
#for loop
for i in range(12):
    print(i)
for  j in range(0,10,2):
    print(j)
sum=0
for k in range(20):
    sum=sum+k
print(sum)
for l in "kharthik":
    print(l,end="")
name =['karthik','cricket','football','badminton']
for i in name:
    print(i)
#nested loops (combination of the much more for loop) to display the square shaped symbol design
Rows = int(input("Enter the number of rows"))
Column = int(input("Enter the number of columns"))
Design = input("Enter the symbol or the design to be print")
#Outer loop
for Outer in range(Rows):
    #Inner loop
    for Inner in range(Column):
        print(Design,end="")
    print()
#Loop control statement
#Break statement
num = int(input("Enter the value of the number"))
for i in range(num):
    if i==5:
        break #terminate after the i==5
    print(i)
#Pass statement
for i in range(0,num):
    if i==5:
        pass #nothinng will happens
    print(i)
#Continue statement
for i in range(0,num):
    if i==5:
        continue #the i==5 only not print other are printed
    print(i)
