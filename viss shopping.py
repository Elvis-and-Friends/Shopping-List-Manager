try:
    with open("shopping_list.txt", "a") as f:
        f.write("- Eggs\n")
        f.write("- Milk\n")
        f.write("- Bread\n")
    print("Items added!")

except FileNotFoundError:
    print("File not found!")