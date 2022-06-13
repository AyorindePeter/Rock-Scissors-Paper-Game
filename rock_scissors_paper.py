import random



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

game =[rock, paper, scissors]
game_choice = random.randint(0,2)

choice = int(input('Type (0) for Rock, (1) for paper and (2) for scissors'))
print('You Chose:')
print(game[choice])

game_choice = random.randint(0,2)
print('Computer Choose:')
print(game[game_choice])




if choice >= 3 or choice < 0: 
    print("You typed an invalid number, you lose!") 
elif choice == 0 and game_choice == 2:
    print("You win!")
elif game_choice == 0 and choice == 2:
    print("You lose")
elif game_choice > choice:
    print("You lose")
elif choice > game_choice:
    print("You win!")
elif game_choice == choice:
    print("It's a draw")