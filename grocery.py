# Grocery list class


class GroceryList:
    def __init__(self, initial_items=[]):
        # Use a set, so that we don't get duplicates
        self.grocery_list = set(initial_items)

    def add(self, item):
        # Use the lower case of the item so we don't get duplicates
        self.grocery_list.add(item.lower())

    def remove(self, item):
        self.grocery_list.remove(item.lower())

    def contains(self, item):
        return item.lower() in self.grocery_list

    def items(self):
        return list(self.grocery_list)

#################
# Example usage

my_list = GroceryList()
my_list.add("strawberries")
my_list.add("wine")
my_list.add("gouda cheese")
if not my_list.contains("Crackers"):
    my_list.add("crackers")
my_list.add("beer")
my_list.remove("beer")

print("My list has: ")
for item in my_list.items():
    print ("\t",item)