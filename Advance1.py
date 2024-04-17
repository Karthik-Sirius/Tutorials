#ASSIGN THE FUNCTION TO VARIABLE:
def close():
    print("The shop will closed around 10 PM")
close() #Function call
print(close)
Kharthik = close
Kharthik()
#Another example:
Why = print
Why("Hello World!")

#Higher Order Functions:
def run(t):
    return t.upper()
def ran(t):
    return t.lower()
def result(func):
    test = func("Hello")
    print(test)
result(run)