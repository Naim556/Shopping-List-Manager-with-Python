def view_list(shopping_list):
    if shopping_list:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("\nYour shopping list is empty.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def add_item(shopping_list):
    while True:
        item = input("Enter the item to add: ")
        if item:
            if item in shopping_list:
                print(f"'{item}' is already in the shopping list.")
            else:
                shopping_list.append(item)
                print(f"{item} has been added shopping list.")
        else:
            print("Item cannot be empty!")
        break

def choice_action(prompt):
    while True:
        try:
            choice = int(input(prompt))
            return choice
        except ValueError:
            print("Please enter the number between 1 ... 4")

def display_menu():
    print("Shopping list manager: \n")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. exit")

def main():
    shopping_list = []
    print("Hi, Wellcome to my shop.\n")
    while True:
        display_menu()
        choice = choice_action("choice the action(1-4): ")

        if 1 <= choice <= 4:
            if choice == 1:
                print("Adding item to the shopping list.")
                add_item(shopping_list)
            elif choice == 2:
                print("Removing item to the shopping list.")
                remove_item(shopping_list)
            elif choice == 3:
                print("Viewing list to the shopping list.")
                view_list(shopping_list)
            elif choice == 4:
                print("Exiting the Shopping List Manager. Goodbye!")
                break
        else:
            print("Invalid choice! Please select a valid option.")



if __name__ == "__main__":
    main()