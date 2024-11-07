import random

user_input = int(input("scissor(0), rock(1), paper(2) : "))
com_input = random.randint(0,2)

if user_input == 0 and com_input == 1:
    print("The computer is rock. You are scissor. You won.")
elif user_input == 0 and com_input == 2:
    print("The computer is paper. You are scissor. You lose.")
elif user_input == 0 and com_input == 0:
    print("The computer is scissor. You are scissor. Its a draw.")
    
elif user_input == 1 and com_input == 0:
    print("The computer is scissor. You are rock. You won.")
elif user_input == 1 and com_input == 2:
    print("The computer is paper. You are rock. You lose.")
elif user_input == 1 and com_input == 1:
    print("The computer is rock. You are rock. Its a draw.")
    
elif user_input == 2 and com_input == 1:
    print("The computer is rock. You are paper. You won.")
elif user_input == 2 and com_input == 0:
    print("The computer is scissor. You are paper. You lose.")
elif user_input == 2 and com_input == 2:
    print("The computer is paper. You are paper. Its a draw.")
    
