
'''
print(sports)
print(type(sports))
print(len(sports))
print(sports[0])
print(sports[-1])
print(sports[-2])
# print(type(sports[0:3]))
# print(type(sports[1]))
# print(type(sports[2]))
# print(type(sports[3]))
'''

"""

for sport in sports:
    print(type(sport))
    print(sport)
"""

repeat = "yes"
while repeat == "yes":
    sports = ["Basketball"] # Empty list
    new_sport = input("Enter your favourite sport: ") #Get user input
    if new_sport:
        sports.append(new_sport)
        print("Updated sports list: ", sports)
    else:
        print("No new sports added")
        print("Sports list:")

    for i, sport in enumerate(sports): # Loop through the sports list with index
        print(f"Sport {i+1}: {sport}") # Print the index and sport

    repeat = input("Do you want to add another sport? (Yes/No): ").strip().lower() # Ask if the user wants to add another sport
print("Exiting the program.") # Print a message when the user exists the program