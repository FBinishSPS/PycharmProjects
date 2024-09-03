import os

# Define the file path
file_path = 'sports01.txt'

# Function to read sports from file
def read_sports(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

# Initialize the sports list by reading from the file
sports = read_sports(file_path)

# Function to add a new sport to the list
def add_sport(new_sport):
    if new_sport:
        if new_sport in sports:
            print(f"{new_sport} is already in the list")
        else:
            sports.append(new_sport)
            print("Updated sports list:", sports)
            save_sports(file_path, sports)
    else:
        print("No new sport added")

# Function to save sports list to file
def save_sports(file_path, sports):
    with open(file_path, 'w') as file:
        for sport in sports:
            file.write(sport + '\n')

# Main program loop
while True:
    print("\nCurrent sports list:")
    for i, sport in enumerate(sports):
        print(f"Sport {i + 1}: {sport}")

    new_sport = input("\nEnter your favorite sport (or press Enter to exit): ").strip()

    if not new_sport:
        print("Exiting the program.")
        break

    add_sport(new_sport)
