print("-Guessing Game!")
print("")
import random
x=random.randrange(1,100)
y=int(input("Enter any number:"))
if x>y:
    print("Computer guess is:",x)
    print("Your guess number is too low:",y)
elif x<y:
    print("Computer guess is:",x)
    print("Your entered number is too high:",y)
else:
    print("Computer guess is:",x)
    print("Your number is equal!")
