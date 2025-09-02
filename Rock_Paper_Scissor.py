#Rock,Paper,Scossor game.

import random
moves = ["Rock","Paper","Scissor"]
user_wins = comp_wins = ties = 0
round_no = 0

while True:
    user_input = input("Enter your move (rock,paper,scissor) or 'quit' to exit = ").capitalize()
    if user_input == ("quit").capitalize():
        print("Thank You for playing")
        break
    if user_input not in moves:
        print("Please enter 'rock','paper' or 'scissor' to play or 'quit' to exit ")
        continue

    comp_input = random.choice(moves)
    round_no += 1
    print(f"Your move is {user_input}.")
    print(f"Computer move is {comp_input}.")

    
    if user_input == comp_input:
        print("Both are same:- Match tied. ")
        ties +=1
    elif user_input == "Rock":
        if comp_input == "Paper":
            print(f"Paper covers the rock so computer won.")
            comp_wins += 1
        else:
            print("Scissor cannot cut rock so You won.")
            user_wins +=1
    elif user_input == "Paper":
        if comp_input == "Rock":
            print("Paper covers the rock so You won")  
            user_wins += 1  
        else:
            print("Scissor can cut paper so Computer wins") 
            comp_wins +=1
    elif user_input == "Scissor":
        if comp_input == "Paper":
            print("Scissor can cut paper so You won")
            user_wins +=1
        else:
            print("Scissor cannot cut rock so computer won")
            comp_wins += 1

print("🏁 Final Score:")
print(f" You: {user_wins} | Computer: {comp_wins} | Ties: {ties}")
if user_wins > comp_wins:
    print(" Overall: You win the match! 🏆")
elif comp_wins > user_wins:
    print(" Overall: Computer wins the match! 🤖")
else:
    print(" Overall: It’s a draw. Well played! 🤝")        




