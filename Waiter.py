from Menu import Menu
from Diner import Diner


class Waiter(object):

    # Input: a Menu object.
    def __init__(self, menu):
        self.__menu = menu
        self.__diners = []

    # Input: a Diner object
    # Add the new Diner object to the waiter’s list of diners.
    def addDiner(self, diner):
        self.__diners.append(diner)

    # get the number of diners the waiter is currently keeping track of
    def getNumDiners(self):
        x = 0
        for i in self.__diners:
            x += 1
        return x

    # Print all the diners the waiter is keeping track of, grouped by their statuses.
    def printDinerStatuses(self):
        for i in Diner.STATUSES:
            print("Diners who are", i, end=": ")
            for k in self.__diners:
                if k.getStatus() > 4:
                    pass
                elif Diner.STATUSES[k.getStatus()] == i:
                    print(k, end=",")
            print()


    def takeOrders(self):
        for i in self.__diners:
            if i.getStatus() == 2:
                for types in Menu.MENU_ITEM_TYPES:
                    self.__menu.printMenuItemsByType(types)
                    print(i.getName(), ", please select a ", types,"menu item number.")
                    choice = int(input(">"))

                    n = self.__menu.getNumMenuItemsByType(types)                  # This is Error Checking.
                    while choice < 0 or choice >= n:
                        choice = int(input(">"))

                    i.addToOrder(self.__menu.getMenuItem(types, choice))          # This is adding the item to the diner.
                i.printOrder()                                                # This is printing the diner’s order.

    # For each diner that is paying, calculate the diner’s meal cost and print it out in a message to the diner.
    def ringUpDiners(self):
        for i in self.__diners:
            if i.getStatus() == 4:
                mealCost = i.calculateMealCost()

                print("\n", i.getName(), ", your meal cost", mealCost)

    # For each diner that is leaving, print a message thanking the diner.
    # And then remove the “leaving” diners from the list of diners.
    def removeDoneDiners(self):
        for i in self.__diners:
            if i.getStatus() == 5:
                print("\n", i.getName(), ", thank you for dining with us! Come again soon!")
                self.__diners.remove(i)

    # To move each diner on to the next stage.
    def advanceDiners(self):
        self.printDinerStatuses()
        for diner in self.__diners:
            diner.updateStatus()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()






