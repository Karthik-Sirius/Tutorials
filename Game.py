#Stone ,Paper and Scissor Game in Python
import random
while True:
    Data = ["Scissors","Paper","Stone"]
    User = None
    Computer = random.choice(Data)
    print("the computer picked is",Computer)
    while User not in Data:
        User = input("Enter either scissors,stone,paper:").capitalize()
        print("You entered is",User)
#Compare with Computer and User
        if User == Computer:
                print("You and me are tied")
        elif User == "Scissors":
            if Computer =="Paper":
                print("You won")
            if Computer == "Stone":
                print("You lose ")
        elif User == "Stone":
            if Computer == "Paper":
                print("you losed")
            if Computer == "Scissors":
                print("You won")
        elif User == "Paper":
            if Computer == "Scissors":
                print("the losed")
            if Computer == "Stone":
                print("the won the match")
    Try = input("Enter either tryagain yes/no").lower()
    if Try != "yes":
        break
#Quiz game in Python :
def newgame():
    guesses = []
    correct = 0
    Questionno=1
    for key in Questions:
        print("----------------------")
        print(key)
        for i in Answer[Questionno-1]:
            print(i)
        Guess = input("Enter one of the following a,b,c,d")
        Guess=Guess.upper()
        guesses.append(Guess)
        correct +=checkanswer(Questions.get(key),Guess)
        Questionno+=1
    display(correct,guesses)
def checkanswer(answer,guess):
    if answer == guess:
        print("Correct")
    else:
        print("Wrong")
def display(correct,guesses):
    print("RESULT")
    print("Answer",end="")
    for i in Questions:
        print(Questions.get(i),end=" ")
    print()

    print("Guesses:",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    score = int((correct/len(Questions))*100)
    print("Your score is "+str(score)+"%")
def playagain():
    response = input("Do you want to play again (yes or no)").upper()
    if response == "YES":
        return True
    else:
        return False

#Dictionary to have the questions and answer
Questions = { #Key are the questions and the values are a answer
    "who is the goat in football": "A",
    "how many days in year":"D",
    "what is the name of goat":"A",
    "who is the founder of amazon":"C"
}
Answer = [["Ronaldo","Messi","Neymar","Suarez"], #-> 1 #2D list to hold the answer of each question
          ["345","366","367","365"],#->2
          ["GreatestOfTheAllTime","Gone","Gate","Goodbye"],#->3
          ["Jeff Bezos","Tesla","Bro","Tata"]] #->4
newgame()
while playagain():
    newgame()
print("Byeeeeeee")