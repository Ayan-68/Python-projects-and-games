import random

a = "Hello! Welcome the the Dice game."
print("\n", a.center(91, "*"))

rules = '''
1. Each player rolls a standard six-sided dice (1–6).
2. On each player's turn, they roll the dice once.
3. The player with the most points in 10 turns will win.
4. Each win will give you 100 points, Loosing doesn't effect your score. 
'''
print(rules)

def check_player():
    try:
        player = int(input("How many players are playing? Press '1' for One and '2' for Two: "))
        return player
    except:
        return "Try again, Only type 1 or 2 to get the game played."
    
    
def get_num():
    a = random.randint(1, 6)
    return a

def main():
    score1 = 0
    score2 = 0
    try:
        if check_player() == 1:
            player1_name = input("Enter the name of first player: ")
            i = 0
            while i < 10:
                i += 1 
                print("\n \n You are playing against computer")
                input("\n Press Enter to start: ")
                player1 = get_num()
                print(f"\n {player1_name} got the Dice number of: {player1}")
                computer = get_num()
                print(f"\n Computer got the Dice number of: {computer}")
                
                if player1 > computer:
                    score1 +=100
                    print(f"\n {player1_name} won the {i} round")
                    print(f"\n scores: \n {player1_name} score: {score1} \n Computer score: {score2} ")
                    
                elif player1 < computer:
                    score2 +=100
                    print(f"\n computer won the {i} round")
                    print(f"\n scores: \n {player1_name} score: {score1} \n Computer score: {score2} ")
                    
                elif player1 == computer:
                    print(f"\n Ops!, It's a draw")
                    print(f"\n scores: \n {player1_name} score: {score1} \n Computer score: {score2} ")
        else:
            player1_name = input("Enter the name of first player: ")
            player2_name = input("Enter the name of second player (if no second player, Just leave it blank and press 'Enter'): ")
            i = 0
            while i < 10:
                i += 1 
                print(f"\n {player1_name} Vs {player2_name}")
                input(f"\n {player1_name} Turn, Press Enter to start: ")
                player1 = get_num()
                print(f"\n {player1_name} got the Dice number of: {player1}")
                input(f"\n {player2_name} Turn, Press Enter to start: ")
                player2 = get_num()
                print(f"\n {player2_name} got the Dice number of: {player2}")
                
                if player1 > player2:
                    score1 +=100
                    print(f"\n {player1_name} won the {i} round")
                    print(f"\n scores: \n {player1_name} score: {score1} \n {player2_name} score: {score2} ")
                    
                elif player1 < player2:
                    score2 +=100
                    print(f"\n {player2_name} won the {i} round")
                    print(f"\n scores: \n {player1_name} score: {score1} \n {player2_name} score: {score2} ")
                elif player1 == player2:
                    print(f"\n Ops!, It's a draw")
                    print(f"\n scores: \n {player1_name} score: {score1} \n {player2_name} score: {score2} ")
    except Exception as e:
        return "Please Try Again, e"
    
main()
