import random
options=['rock','paper','scissors']
user_choice=input('rock,paper or scissors').lower()
computer_choice=random.choice(options)
print('computer choose:',computer_choice)
if user_choice==computer_choice:
    print('''it's a tie''')
elif user_choice =='rock':
    if computer_choice =='scissors':
        print('you win')
    else:
        print('you lose')
elif user_choice =='paper':
    if computer_choice =='rock':
        print('you win')
    else:
        print('you lose')
elif user_choice =='scissors':
    if computer_choice =='paper':
        print('you win')
    else:
        print('you lose')
else:
    print('invalid choice')