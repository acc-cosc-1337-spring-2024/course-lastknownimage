from decisions import get_options_ratio, get_faculty_rating
def main():
    options = int(input("how many options are there?  "))
    total = int(input("what's the total?  "))

    result = get_options_ratio(options, total)
    print("faculty rating:", get_faculty_rating(result))
          
if __name__ == "__main__":
    main()

# I did my best and can't make it work :-(
# I'm out of time for this assignment. I don't know why it isn't working correctly and the error messages are really vague and non-referential.
# Will be trying to come to office hours again.