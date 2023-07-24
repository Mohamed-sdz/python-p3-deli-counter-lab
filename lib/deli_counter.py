 # deli_counter.py

# Function to display the current line
def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_msg = "The line is currently:"
        for idx, person in enumerate(katz_deli, start=1):
            line_msg += f" {idx}. {person}"
        print(line_msg)

# Function to add a new customer to the line
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

# Function to serve the next person in line
def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving = katz_deli.pop(0)
        print(f"Currently serving {serving}.")

# Test cases
if __name__ == "__main__":
    KATZ_DELI = []
    OTHER_DELI = ["Logan", "Avi", "Spencer"]
    ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]

    line(KATZ_DELI)
    line(OTHER_DELI)
    line(ANOTHER_DELI)

    take_a_number(KATZ_DELI, "Ada")
    take_a_number(OTHER_DELI, "Gracie")
    take_a_number(ANOTHER_DELI, "John")

    line(KATZ_DELI)
    line(OTHER_DELI)
    line(ANOTHER_DELI)

    now_serving(KATZ_DELI)
    now_serving(OTHER_DELI)
    now_serving(ANOTHER_DELI)

    line(KATZ_DELI)
    line(OTHER_DELI)
    line(ANOTHER_DELI)
