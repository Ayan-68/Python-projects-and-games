import random
import time

score = 0

a = "Hello There!"
print("\n", a.center(91, "~"))

def main():
    try: 
        while True:
            print("1 for rock, 2 for paper, 3 for scissors or press 4 to quit")
            num = [1,2,3,4]

            user = int(input("Enter your Character: "))

            if user not in num:
                print("Invalid Input, Please enter the given values")
            else:
                if user == 1:
                    print("You are Rock")
                elif user == 2:
                    print("You are Paper")
                elif user == 3:
                    print("You are Scissors")
                else:
                    print("Thanks for playing!")
                    break

            comp = random.randint(1,3)

            if comp == 1:
                print("Computer is Rock")
            elif comp == 2:
                print("Computer is Paper")
            elif comp == 3:
                print("Computer is Scissors")

            print("\nLets See Who wins!")
            time.sleep(2)




            if user == comp:
                print("Oops!, Its a draw")
                score +=0
                
            elif (user == 1 and comp == 3) or \
                (user == 2 and comp == 1) or \
                (user == 3 and comp == 2):
                print("You Won")
                score += 1

            else:
                print("You lose")


            print(f"\nYour score is : {score}")
    except Exception as e:
        return e
