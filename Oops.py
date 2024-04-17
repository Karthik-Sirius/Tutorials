#Object Oriented Programming Python Creation of Object and Class Variable:
class  Football: #Oops.py and Oopys2.py
    Goals = 24 #class variable
    def __init__(self,player,age,country,club): #constructor
        self.player = player
        self.age = age
        self.country = country
        self.club = club
    def goat(self):
        print("The Football is the goat sport:"+self.player)
    def best(self):
        print("The best Football played country: "+self.club)
#Inheritance:
class Animal:
    alive = True #Class variable
    def eat(self):
        print("The animal is eating and enjoying")
    def sleep(self):
        print("The animal is sleeping")
class Tiger(Animal):
    def run(self):
        print("The Tiger is Hungry")
class Lion(Animal):
    def chew(self):
        print("The lion is smart")
class Elephant(Animal):
    def weight(self):
        print("the elephant is good")

#Now it time  to  create the objects
animal = Animal() #assign the value of class to the variable animal
tiger  =Tiger()
lion=Lion()
elephant = Elephant()
tiger.eat() #we can access the methods and variable which are present in the animal class that is the power of the inheritance
lion.sleep()
elephant.weight()
print(elephant.alive)

#Multilevel inheritance:
class Choco: #grand parent class of Veggie,Masala,Total
    variable = "lunch"
    def retail(self):
        print("The retail value is 30 rupees")
class Veggie(Choco): #parent of Masala,Total
    def price(self):
        print("the price of veggie is 50 rupees")
class Masala(Veggie): #parent of Toatal
    def mrp(self):
        print("the mrp is 240 rupees")
class Total(Masala):#child class
    def money(self):
        print("The money is 400 rupees")

#now its time to create the object
choco = Choco()
veggie = Veggie()
masala = Masala()
total = Total()
print(choco.variable)
veggie.retail()
masala.price()
total.mrp()

#Multiple inheritance in Python:
class Virat:
    def test(self):
        print("king")
class Dhoni:
    def t20(self):
        print("cool captain")
class Odi(Virat): #Single Inheritance
    def attitude(self):
        print("Aggression")
class Chennai(Dhoni):
    def ipl(self):
        print("CSK")
class Wc(Virat,Dhoni): #Multiple inheritance
    def cup(self):
        print("The world cup is here for us")
#Its time to create the object:
virat = Virat()
dhoni = Dhoni()
odi = Odi()
chennai = Chennai()
wc = Wc()
virat.test()
dhoni.t20()
odi.attitude()
chennai.ipl()
wc.t20()
wc.cup()


