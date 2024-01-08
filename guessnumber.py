import random
upper_limit=int(input("Enter the upper limit"))
lowe_limit=int(input("Enter the lower limit"))
random_number=random.randint(lowe_limit,upper_limit)
print("you have to chose number between",upper_limit,"and",lowe_limit)
chances=0
while chances<3:
    chances+=1
    guess=int(input("Enter you guess"))
    if random_number==guess:
     print("Congratulation,you did it.The number was",random_number)
     break
    elif guess<random_number:
        print("you guessed a small nuumber.")  
    elif guess<random_number:
        print("you guessed a large nuumber.")  
    if chances==7:
        print("\n you've run out of chances")
        print("\n The number was",random_number)
        print("Better luck next time")
        break
    print("\n")
    break