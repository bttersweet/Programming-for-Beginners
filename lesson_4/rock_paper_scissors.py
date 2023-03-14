import random

def new_game():
	moves = ["rock", "paper", "scissors"]

	user_choice = input("Choose your move, rock, paper, or scissors: ")
	computer_choice = random.choice(moves)

	print(f"Computer chose: {computer_choice}")

	if user_choice == computer_choice:
		print("It's a tie!")
	elif (user_choice == "rock" and computer_choice == "scissors") or \
		(user_choice == "paper" and computer_choice == "rock") or \
		(user_choice == "scissors" and computer_choice == "paper"):
		print("You won!")
	else:
		print("You lost!")

def start_games(num_of_times):
	# for i in range(num_of_times):
	# 	new_game()
	num_of_times_left = num_of_times
	while num_of_times_left > 0:
		new_game()
		num_of_times_left -= 1

start_games(3)