import random
rock='''
    _______
____'   ____)
     (_______)
     (_______)
     (______)
----,__(___)
'''
paper='''
    _______
____'   ____)____
     ____________)
     _____________)
     ___________)
----,_________)
'''
scissor='''
    _______
___'   ____)_____
     ____________)
     ____________)
     (______)
---,__(___)
'''
game_image=[rock,paper,scissor]
user_choice=int(input("Enter your choice :0 for rock,1 for paper,2 for scissors :"))
if user_choice>2 or user_choice<0:
    print("Yoy entered invalid number,You lose.")
else:
    print(game_image[user_choice])
    com_choice=random.randint(0,2)
    print("Computer choice:")
    print(game_image[com_choice])
    if com_choice==user_choice:
        print("It's Draw.")
    elif user_choice==0 and com_choice==2:
        print("You Win.")
    elif com_choice==0 and user_choice==2:
        print("You Lose.")
    elif com_choice>user_choice:
        print("You Lose.")
    elif user_choice>com_choice:
        print("You Win.")
