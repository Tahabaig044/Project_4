
my_list = ["apple", "banana", "cherry", "orange", "kiwi"]

def access_list_elements(my_list, index):
    """"Returns the element at the specified index from the list, or an error message if the index is out of range."""
    if 0 <= index < len(my_list):
        return f"The element at index {index} is: {my_list[index]}"
    return "Index out of range. Please enter a valid index."

def modify_list(my_list, index, new_value):
    """Modifies the element at the specified index in the list."""
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"The list after modification: {my_list}"
    return "Index out of range. Please enter a valid index."

def slice_list(my_list, start, end):
    """Returns a sliced portion of the list."""
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list):
        return f"The sliced portion of the list from index {start} to {end} is: {my_list[start:end]}"
    return "Invalid slice indices. Please enter valid indices."

def list_game():
    print("\nWelcome to the List maniputlation!")
    my_list = ["apple", "banana", "cherry", "orange", "kiwi"]
    while True:
        print("\nCurrent list:", my_list)
        print("Choose an option:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            index = int(input("Enter the index of the element you want to access: "))
            print(access_list_elements(my_list, index))
            
        elif choice == '2':
            index = int(input("Enter the index of the element you want to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_list(my_list, index, new_value))
            
        elif choice == '3':
            start = int(input("Enter the starting index for slicing: "))
            end = int(input("Enter the ending index for slicing: "))
            print(slice_list(my_list, start, end))
            
        elif choice == '4':
            print("Exiting the game.")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    list_game()

    




