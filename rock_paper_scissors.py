rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = ['rock', 'paper', 'scissors']
import random
computer = choices[random.randint(0,2)]

def printer(choice):
  if choice == "rock":
    print(rock)
  elif choice == 'scissors':
    print(scissors)
  else:
    print(paper)

player = input("What do you want to choose? > ")

print(f"You chose {player}")
printer(player)

print(f"Well now, the computer chose {computer}")
printer(computer)

if computer == player:
  print("It's a tie!")
elif computer == 'rock' and player == 'scissors':
  print('You lose!')
elif computer == 'paper' and player == 'rock':
  print('You lose!')
elif computer == 'scissors' and player == 'paper':
  print("You lose!")
else:
  print("You win!")
