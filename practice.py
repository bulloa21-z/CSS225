print("Welcome to chapter: 2")
answer = "the cat is late"

knowsAnswer = False

while(knowsAnswer == False):
    print("What is the secret code?")
    userCode = input()
    if(answer == userCode):
        print("You may enter.")
        Chapter 2()
    knowsAnswer= True

def chapter2():
    print("Welcome to Chapter 2")