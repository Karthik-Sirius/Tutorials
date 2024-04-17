print("Welcome to the quiz game")
User = input("Would you like to play the game:")
if User.lower() != "yes":
    quit()
print("OK LETS PLAY IT")
Score = 0
Answer = input("Who is the founder of spacex and tesla?")
if Answer.lower() == "elon musk":
    print("Correct")
    Score=Score+1
else:
    print("Incorrect")
Answer = input("Who is the goat of football?")
if Answer.lower() == "cristiano ronaldo":
    print("Correct")
    Score=Score+1
else:
    print("Incorrect")
Answer = input("What is the rover that was went to mars?")
if Answer.lower() == "curiosity":
    print("Correct")
    Score=Score+1
else:
    print("Incorrect")
Answer = input("what is the name of the spacecraft produced by spacex for mars mission")
if Answer.lower() == "star ship":
    print("Correct")
    Score=Score+1
else:
    print("Incorrect")
Answer = input("Most common element in mars")
if Answer.lower() == "carbon dioxide":
    print("Correct")
    Score=Score+1
else:
    print("Incorrect")
Answer = input("what is the name of the moon mission that was aimed to launch at 2025?")
if Answer.lower() == "artemis":
    print("Correct")
    Score = Score + 1
else:
    print("Incorrect")
print("Your result for test")
print("You have got "+str(Score)+" Marks")
print("Your Percentage "+str((Score/6)*100)+" Percentage")