import random


x = input("Pick a number from 1 to 100: ")



x = int(x)
    

y = random.randint(1,100)

g_count = 0

while x != y:
    x = int(x)
    if x == y:
        print("you guessed correctly, it took you " + str(g_count) + " guesses")
        g_count+=1

    elif x < y:
        print("you guessed too low, try again")
        x = input("Pick a number from 1 to 100: ")
        g_count+=1
    elif x > y:
        print("you guessed too high, try again")
        x = input("Pick a number from 1 to 100: ")
        g_count+=1
