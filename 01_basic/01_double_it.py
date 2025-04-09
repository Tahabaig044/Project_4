#01_double_it

def main():
  curr_value = 1
  while curr_value <= 100:
    next_value = curr_value * 2
    print(next_value, end=" ")
    curr_value = next_value


if __name__ == "__main__":
  main()