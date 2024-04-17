#It is the combination of different datatype variable that are allow the duplicate and unordered sequences
Marvels = ["Captain America","Doctor Strange","Moon knight","Loki","Doctor Doom"]
print(Marvels[1]) #accessing the members of the list
print(Marvels[3])
print("The elements of the list are")
for display in Marvels: #dispaly all the elements by using the for loop for sequence
    print(display)
print()
Marvels.append("Thor") #append->add the new member at the end of the list
Marvels.append("Iron man") #if the statement are enclosed with print() then it return None
for display in Marvels:
    print(display)
Marvels.remove("Loki")
Marvels.remove("Doctor Doom") #remove() used to remove the particular member from the list
for display in Marvels:
    print(display)
Marvels.pop() #the pop() is used to remove the last member of a list like the stack
for display in Marvels:
    print(display)
Marvels.insert(4,"Shang chi") #the insert() is used to insert the particular member at the particular index
Marvels.insert(5,"Hulk")
for display in Marvels:
    print(display)
Marvels.sort() #the sort() is used to arrange the member from ascending order
for display in Marvels:
    print(display)
Marvels.clear() #clear() is used to  clear the entire list
for display in Marvels:
    print(display)
#2D Lists - combination of lists
Player = ['Ronaldo','Virat','dhoni']
Sports = ['football','cricket','cricket']
Age = [39,36,43]
Total = [Player,Sports,Age]
print(Total[2][2])

#Tuple -> contains different datatype elements that are ordered and it wont be changeable
Place = ('Denver','Tokyo','Rio','Rio')
print(Place.count("Rio"))
print(Place.index("Tokyo"))
for show in Place:
    print(show)
if 'Rio' in Place:
    print("The element Rio is present in the list called Place ")

#Set ->morelike than a combination that are unordered ,no duplicate elements and unindexed no index accessing are allowed
Utensils = {'Fork','Spoon','Knife'}
for Answer in Utensils:
    print(Answer)
Utensils.add('Plate')
Utensils.add('Cooker')
for Answer in Utensils:
    print(Answer)
Utensils.remove('Fork')
Utensils.remove('Spoon')
for Answer in Utensils:
    print(Answer)
Utensils.clear()
for Answer in Utensils:
    print(Answer)
Dishes = {'Rice','Meat','Salad'}
Utensils.update(Dishes)
Lunch = {'Rice','Gravy','SideDish'}
print(Utensils.union(Lunch))
print(Utensils.difference(Lunch))
print(Utensils.intersection(Lunch))
for Answer in Utensils:
    print(Answer)

#Dictionary -> contains the value key pair there is no index
Data = {
    'Python': 123,
    'Golang':7643,
    'Dart':2221,
    'Rust':2265
}
for Results in Data:
    print(Results) #it print only the key not the values
print(Data.values())
print(Data.keys())
print(Data.items())
print(Data['Python'])
print(Data['Rust'])
print(Data.get('Golang'))
Data.update({'Cloud':'Azure'}) #Normal like the Dictionary
Data.update({'Flutter':'Dart'})
Data.pop('Rust')
print(Data.items())
Data.clear()
print(Data.items())

