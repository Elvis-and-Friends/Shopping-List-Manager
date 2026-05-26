try:
    with open("shopping_list.txt", "r+") as f:
        content = f.read()
        print("Current content:")
        print(content)

        updated = content.replace("No items yet.", "- Butter")
        f.seek(0)
        f.write(updated)
        f.truncate()
        print("File updated successfully!")

except FileNotFoundError:
    print("File not found!")