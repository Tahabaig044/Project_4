#03_guess_my_number
import random

def main():
  secret_number: int = random.randint(0, 99)
  print("I am thinking of a number between 0  and 99")
  user_input = int(input("Guess the secret number: "))
  while user_input != secret_number:
    if user_input < secret_number:
      print("Too low")
    else:
      print("Too high")
    print()
    user_input: int = int(input("Guess the new secret number: "))
  print("Congrats 🎉 the number was :" + str(secret_number))

if __name__ == "__main__":
  main()