class Users():
    def __init__(self, firstname, lastname, age):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age

    def get_firstname(self):
        return self.__firstname
    def get_lastname(self):
        return self.__lastname
    def get_age(self):
        return self.__age

    def set_firstname(self, firstname):
        self.__firstname = firstname
    def set_lastname(self, lastname):
        self.__lastname = lastname
    def set_age(self, age):
        self.__age = age