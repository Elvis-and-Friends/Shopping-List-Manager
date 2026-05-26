keyword = input("Enter item to search or delete: ")

try:
    with open("shopping_list.txt", "r") as f:
        lines = f.readlines()

    found = False
    for line in lines:
        if keyword.lower() in line.lower():
            print("Found: " + line.strip())
            found = True

    if not found:
        print("Item not found.")

    choice = input("Do you want to delete this item? (yes/no): ")

    if choice.lower() == "yes":
        with open("shopping_list.txt", "w") as f:
            for line in lines:
                if keyword.lower() not in line.lower():
                    f.write(line)
        print("Item deleted successfully!")
    else:
        print("No changes made.")

except FileNotFoundError:
    print("File not found!")