def initdatabase():
    """Returns 4 lists pre-populated with at least 5 Star Trek characters."""
    names = ["Jean-Luc Picard", "William Ryker", "Data", "Geordi La Forge", "Worf"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lt. Commander", "Lieutenant"]
    divs = ["Command", "Command", "Operations", "Operations", "Security"]
    ids = ["101", "102", "103", "104", "105" ]
    return names, ranks, divs, ids

def display_menu(user_name):
    """Prints menu and returns user choice."""
    print(f"\n FLEET MANAGEMENT SYSTEM")
    print(f"Logged in as: {user_name}")
    print("1. Add Crew Member")
    print("2. Remove Crew Member")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    return input("Select an option: ")

def add_member(names, ranks, divs, ids):
    """Adds a new member after validation."""
    print("\n ADD MEMBER")
    new_id = input("Enter new ID: ")
    
    if new_id in ids:
        print("Error: ID already exists.")
        return
    
    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    new_rank = input(f"Enter Rank ({'/'.join(valid_ranks)}): ")
    if new_rank not in valid_ranks:
        print("Error: Invalid Rank.")
        return

    new_name = input("Enter Full Name: ")
    new_div = input("Enter Division (Command/Operations/Sciences/Security): ")

    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print(f"Success: {new_name} added.")