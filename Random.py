import random
n=random.randint(0,21)
print("You have 4 attempts")
gn=int(input("Guess the number between 1 to 20 : "))
attempt=0
f=True
while n!=gn:
    attempt+=1
    print(str(4-attempt)+" left!")
    if(4-attempt==0):
        break
    if(n>gn):
        print("Try some greater number")
    else:
        print("Try some lesser number")

    gn=int(input("Guess the number:"))

else:
    print("{:^20}".format("You Won!!!"))
    f=False
if(f):
    print("You Lost")