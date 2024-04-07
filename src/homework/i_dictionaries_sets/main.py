import sets

def main():
    prog1 = {'Student_1', 'Student_2', 'Student_3'}
    prog2 = {'Student_3', 'Student_4', 'Student_5'}
    while True:
        print("Inventory menu\n")
        print("1: Took prog1 and prog2")
        print("2: Took prog2 only")
        print("3: Took prog1 not prog2")
        print("4: Took prog2 not prog1")
        print("5: Exit\n")
        
        choice = input("Please enter a number: ")
        if choice == '1':
            print("Took prog1 and prog2:", sets.get_students_who_took_prog1_and_prog2(prog1, prog2))
        elif choice == '2':
            print("Took prog2 only:", sets.get_students_who_took_prog2_only(prog1, prog2))
        elif choice == '3':
            print("Took prog1 and not prog2:", sets.get_students_who_took_prog1_not_prog_2(prog1, prog2))
        elif choice == '4':
            print("Took prog2 and not prog1:", sets.get_students_who_took_prog2_not_prog_1(prog1, prog2))
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("I don't recognize this choice and I won't act on it.")

if __name__ == "__main__":
    main()