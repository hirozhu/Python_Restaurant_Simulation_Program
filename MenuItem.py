class MenuItem(object):
    def __init__(self, name, t, price, description):
        self.__name = name
        self.__type = t
        self.__price = float(price)
        self.__description = description

    # Define getters and setters for each of the 4 attributes
    def getName(self):
        return self.__name

    def setName(self, n):
        self.__name = n

    def getType(self):
        return self.__type

    def setType(self, n):
        self.__type = n

    def getPrice(self):
        return self.__price

    def setPrice(self, n):
        self.__price = n

    def getDescription(self):
        return self.__description

    def setDescription(self, n):
        self.__description = n

    # Construct a message to describe the food using all four attributes.
    def __str__(self):
        msg = self.__name + "(" + self.__type + "): " + str(self.__price) + "\n" + self.__description
        return msg
    


