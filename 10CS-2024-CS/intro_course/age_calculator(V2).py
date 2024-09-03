from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    # Input birthdate from user
    while True:
        try:
            birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
            birthdate = date.fromisoformat(birthdate_str)
            break
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

    # Calculate age
    age = calculate_age(birthdate)
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()
