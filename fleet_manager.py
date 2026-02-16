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

    def remove_member(names, ranks, divs, ids):
        """Removes a member by ID from all lists."""
    print("\n REMOVE MEMBER")
    target_id = input("Enter ID to remove: ")
    
    if target_id in ids:
        idx = ids.index(target_id)
        removed_name = names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print(f"Success: {removed_name} removed.")
    else:
        print("Error: ID not found.")
    
    def update_rank(names, ranks, ids):
        """Updates the rank of a specific member."""
    print("\nUPDATE RANK")
    target_id = input("Enter ID to update: ")
    
    if target_id in ids:
        idx = ids.index(target_id)
        print(f"Current Rank for {names[idx]}: {ranks[idx]}")
        new_rank = input("Enter new rank: ")
        ranks[idx] = new_rank
        print("Rank updated.")
    else:
        print("Error: ID not found.")

    def display_roster(names, ranks, divs, ids):
        """Prints a formatted table of all crew."""
    print("\n CREW ROSTER")
    print(f"{'ID':<6} {'Name':<20} {'Rank':<15} {'Division':<15}")
    print("-" * 60)
    
    for i in range(len(names)):
        print(f"{ids[i]:<6} {names[i]:<20} {ranks[i]:<15} {divs[i]:<15}")

    def search_crew(names, ranks, divs, ids):
        """Prints crew members whose name contains the search term."""
    print("\nSEARCH CREW")
    term = input("Enter name to search: ").lower()
    found = False
    
    print(f"{'ID':<6} {'Name':<20} {'Rank':<15} {'Division':<15}")
    for i in range(len(names)):
        if term in names[i].lower():
            print(f"{ids[i]:<6} {names[i]:<20} {ranks[i]:<15} {divs[i]:<15}")
            found = True
            
    if not found:
        print("No matches found.")

def filter_by_division(names, divs):
    """Prints members in a specific division."""
    print("\nFILTER BY DIVISION")
    target_div = input("Enter Division to filter (e.g. Command, Operations): ")
    
    print(f"Members in {target_div}:")
    count = 0
    for i in range(len(names)):
        if divs[i].lower() == target_div.lower():
            print(f"- {names[i]}")
            count += 1
            
    if count == 0:
        print("No members found in this division.")

def calculate_payroll(ranks):
    """Calculates total payroll based on rank values."""
    print("\nPAYROLL CALCULATION")
    total_cost = 0
    
    for rank in ranks:
        if rank == "Captain":
            total_cost += 1000
        elif rank == "Commander":
            total_cost += 800
        elif rank == "Lt. Commander":
            total_cost += 600
        elif rank == "Lieutenant":
            total_cost += 500
        elif rank == "Ensign":
            total_cost += 200
        else:
            total_cost += 100