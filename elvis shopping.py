try:
    with open("shopping_list.txt","x") as f:
        f.write("Shopping List Manager\n")
        f.write("created 4/28/26")
        f.write("Item\n")
        f.write("No items yet.\n")
        
        print("shopping list initialize")
        
except FileExistsError:
    print("File Already Exist") 
        