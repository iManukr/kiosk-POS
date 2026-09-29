def clean_text(prompt):
    """
    Gets text from the user and cleans it.
    Example:
    "  bread " becomes "Bread"
    """
    return input(prompt).strip().title()


def get_positive_int(prompt):
    """
    Keeps asking until the user enters a positive whole number.
    """
    while True:
        value = input(prompt).strip()

        if value.isdigit():
            number = int(value)

            if number > 0:
                return number
            else:
                print("Please enter a number greater than zero.")
        else:
            print("Invalid input. Please enter a whole number.")