import random

num_rounds = 5

def play_game():
    print("Welcome to the game!")
    print("-------------------------")

    your_score = 0
    for i in range(num_rounds):
        print("Round", i + 1)
        print("---------")
        com_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("your number:", your_num)

        choice = input("Do you think your number is higher than computer or lower? (h/l): ")
        while choice not in ['h', 'l']:
            print("Invalid input. Please enter 'h' for higher or 'l' for lower.")
            
        higher = choice == 'h'
        if (higher and your_num > com_num) or (not higher and your_num < com_num):
            print("Correct! Computer number was:", com_num)
            your_score += 1
        else:
            print("That's Incorrect! the computer number was:" , com_num)
        print("Your score is:", your_score)
        print()

    print("Your final score is", your_score)

    if your_score == num_rounds:
        print("Wow! You played perfectly!")
    elif your_score > num_rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play_game()
            