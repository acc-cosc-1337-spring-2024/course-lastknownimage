from repetition import get_factorial
from repetition import sum_odd_numbers

def display_menu():
    print("Homework menu")
    print("1: Factorial")
    print("2: Sum odd numbers")
    print("3: Quit")
def get_valid_number(prompt):
    while True:
        num = input(prompt)
        try:
            num = int(num)
            return num
        except ValueError:
            print("I need a valid number.")
def main():
    while True:
        display_menu()
        choice = get_valid_number("Enter a number between 1 and 3: ")

        if choice == 1:
            num = get_valid_number("Enter a number value: ")
            if num >= 0:
                print(f"Factorial of {num} is {get_factorial(num)}")
            else:
                print("I need a positive number under 10.")

        elif choice == 2:
            num = get_valid_number("Enter a number value: ")
            if num >= 0:
                print(f"Sum of the odd numbers up to {num} is {sum_odd_numbers(num)}")
            else:
                print("I need a positive number under 10.")

        elif choice == 3:
            exit_choice = input("Are you good to quit? (y/n): ")
            if exit_choice.lower() == "y":
                print("Quitting.")
                break
    else:
        print("I don't understand your input.")

if __name__ == "__main__":
    main()