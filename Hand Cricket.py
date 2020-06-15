"""
A simple hand cricket game using python
"""
import random

def score_func(player, prev_score):
    score = 0
    while score <= prev_score:
        num = int(input())
        if num <= 6 and num > 0:
            user = num
        else:
            print("Enter a number between 1 and 6")
            continue
        computer = random.randrange(1,7)
        print("User puts - ", user, "Computer puts - ", computer)
        if user == computer:
            if player == 1:
                print("User Out!")
            else:
                print("Computer Out!")
            break

        if player == 1:
            num = int(input())
            score += user
        else:
            score += computer
    return score


print("***Hand Cricket - User Vs Computer***")

bat_or_bowl = random.choice([1, 2])

if bat_or_bowl == 1:
    print("User Bat's first!")
    user_score = score_func(bat_or_bowl, 0)
    comp_score = score_func(2, user_score)
else:
    print("Computer Bat's first!")
    comp_score = score_func(bat_or_bowl, 0)
    user_score = score_func(1, comp_score)

if user_score == comp_score:
    print("Draw!")
    print("User Score", user_score)
    print("Computer Score", comp_score)
elif user_score > comp_score:
    print("User Wins!")
    print("User Score", user_score)
    print("Computer Score", comp_score)
else:
    print("Computer Wins!")
    print("User Score", user_score)
    print("Computer Score", comp_score)


