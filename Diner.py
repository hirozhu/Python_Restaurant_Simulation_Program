from MenuItem import MenuItem


class Diner(object):
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # Set the diner’s name attribute to the input value.
    # Set the diner’s order attribute to an empty list.
    # Set the status attribute to 0.
    def __init__(self, name):
        self.__name = name
        self.__order = []
        self.__status = 0

    # Define getters and setters for all the instance attributes.
    def getName(self):
        return self.__name

    def setName(self, n):
        self.__name = n

    def getOrder(self):
        return self.__order

    def setOrder(self, n):
        self.__order = n

    def getStatus(self):
        return self.__status

    def setStatus(self, n):
        self.__status = n

    # Add the new MenuItem object to the diner’s order list.
    def addToOrder(self, n):
        self.__order.append(n)

    # Increase the diner’s status by 1.
    def updateStatus(self):
        self.__status += 1

    # Print a message containing all the menu items the diner ordered.
    def printOrder(self):
        print(self.__name, "ordered: ")
        for i in self.__order:
            print("-", i)

    # Total up the cost of each of the menu items the diner ordered.
    def calculateMealCost(self):
        cost = 0
        for i in self.__order:
            cost += i.getPrice()
        cost = float(cost)
        return cost

    # Construct a message containing the diner’s name and status.
    def __str__(self):
        msg = "Diner " + self.__name + " is currently " + Diner.STATUSES[self.__status]
        return msg

