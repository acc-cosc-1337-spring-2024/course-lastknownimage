from src.homework.j_classes.class_a import Die

def main():
    die = Die()
    while True:
        input("Hit enter to roll.")
        die.roll()
        print(die)
        choice = input("Continue? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()