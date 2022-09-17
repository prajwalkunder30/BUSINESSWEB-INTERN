import random
while True:
    my_answer=input("Chose: rock,paper or scissors:")
    if my_answer !="rock" and my_answer!="paper" and my_answer!="scissors":
        print("Please chose a correct answer")  
        continue
    computer_answer=random.choice(["rock","paper","scissors"])
    print(f"Computer chose:{computer_answer}")
    if my_answer==computer_answer:
        print("You tied")
        continue
    elif my_answer=="paper" and computer_answer=="rock":
        print("You Win")
        break
    elif my_answer=="rock" and computer_answer=="scissor":
        print("You Win")
        break
    elif my_answer=="scissor" and computer_answer=="paper":
        print("You Win")
        break
    else:
        print("You lose.Try Again")    
        

