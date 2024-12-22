class Menu:
    def __init__(self,menu):
        self.menu = menu
    
    def add_item(self,item):
        if self.check_item(item):
            print(f"\t{item} already exists in the menu.")
            return
        self.menu.append(item)
        print(f"\t{item} added to the menu.")

    def remove_item(self, item):
        if item in self.menu:
            self.menu.remove(item)
            print(f"\t{item} removed from the menu.")
        else:
            print(f"\t{item} not found in the menu.")
    
    def check_item(self,item):
        return item in self.menu
    
initial_items = []
for i in range(int(input("Enter no.of items: "))):
    initial_items.append(input("Enter item: "))


def check_input_operation(opp):
    operations = ["add","remove","check"]
    return (opp[0] in operations and len(opp) == 2) or (opp[0]=="exit" and len(opp) == 1)


menu_obj = Menu(initial_items)

print("\nTo Add item to Menu Enter: add <item_name>")
print("To Remove item from Menu Enter: remove <item_name>")
print("To Check if item exists in Menu Enter: check <item_name>")
print("To Exit the Program Enter: exit")

while True:
    print("\n\tCurrent Menu: ",*menu_obj.menu,"\n")
    
    opp = input("\tEnter the Operation: ").split()

    if not check_input_operation(opp):
        print("\tInvalid operation!")
        continue

    if opp[0]=="exit":
        print("ByeBye!")
        exit(0)

    item = opp[1]
    if opp[0]=="add":
        menu_obj.add_item(item)
    elif opp[0]=="remove":
        menu_obj.remove_item(item)
    elif opp[0]=="check":
        if menu_obj.check_item(item):
            print(f"\t{item} found in the menu.")
        else:
            print(f"\t{item} not found in the menu.")