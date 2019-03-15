from MenuItem import MenuItem


class Menu(object):
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    def __init__(self, dict):
        self.__dict = dict
        self.__menuItemDictionary = {}
        self.__menuItemDictionary["Drink"] = []
        self.__menuItemDictionary["Appetizer"] = []
        self.__menuItemDictionary["Entree"] = []
        self.__menuItemDictionary["Dessert"] = []

        # Open and read the csv file and create a MenuItem object from each line in the file.
        fin = open(dict, "r")
        for line in fin:
            line = line.strip()
            dataList = line.split(",")

            name = dataList[0]
            t = dataList[1]
            price = dataList[2]
            description = dataList[3]
            item = MenuItem(name, t, price, description)

            # Add the new object to the dictionary by using its type as the key.
            if t == "Drink":
                self.__menuItemDictionary["Drink"].append(item)
            elif t == "Appetizer":
                self.__menuItemDictionary["Appetizer"].append(item)
            elif t =="Entree":
                self.__menuItemDictionary["Entree"].append(item)
            elif t == "Dessert":
                self.__menuItemDictionary["Dessert"].append(item)

        fin.close()

    # Get the MenuItem object from the dictionary using its type and index position in the list of items.
    def getMenuItem(self, types, index):
        item = self.__menuItemDictionary[types][index]
        return item

    # Print a header with the type of menu items, followed by a numbered list of all the menu items of that type
    def printMenuItemsByType(self, types):

        counter = 0
        print("--------", types, "----------")
        for menuItem in self.__menuItemDictionary[types]:
            print(counter, ")",
                  "\n", menuItem)

            counter += 1

    # get the number of MenuItems of the input type of the food.
    def getNumMenuItemsByType(self, types):
        x = 0
        for i in self.__menuItemDictionary[types]:
            x += 1
        return x





