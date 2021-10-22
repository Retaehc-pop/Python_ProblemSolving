import random

running = True
while running:
    length = int(input("input range from 0-n(0 to quit):"))
    if length == 0:
        running = False
    else:
        randnum = random.randint(0, length)
        print("you have 10 guesses")
        guesses = 10
        while guesses >= 0:
            guess = int(input())
            if guess < randnum:
                print("Too low")
            elif guess > randnum:
                print("Too high")
            else:
                print(f"correct the number is : {randnum}")
                break
            print(f"you have {guesses} left")
            guesses -= 1
