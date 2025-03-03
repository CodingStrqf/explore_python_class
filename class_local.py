class Country:
    def __init__(self, name, code):
        self._name = name
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Le nom du pays ne peut pas être vide.")
        self._name = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not value:
            raise ValueError("Le code du pays ne peut pas être vide.")
        self._code = value

class Address:
    def __init__(self, street, city, postal_code, country):
        self._street = street
        self._city = city
        self._postal_code = postal_code
        self._country = country

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        if not value:
            raise ValueError("La rue ne peut pas être vide.")
        self._street = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not value:
            raise ValueError("La ville ne peut pas être vide.")
        self._city = value

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value):
        if not value:
            raise ValueError("Le code postal ne peut pas être vide.")
        self._postal_code = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if not isinstance(value, Country):
            raise ValueError("Le pays doit être une instance de la classe Country.")
        self._country = value

class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Le nom ne peut pas être vide.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("L'âge ne peut pas être négatif.")
        self._age = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, Address):
            raise ValueError("L'adresse doit être une instance de la classe Address.")
        self._address = value

class Company:
    def __init__(self, name, employees):
        self._name = name
        self._employees = employees

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Le nom de l'entreprise ne peut pas être vide.")
        self._name = value

    @property
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, value):
        if not all(isinstance(emp, Person) for emp in value):
            raise ValueError("Tous les employés doivent être des instances de la classe Person.")
        self._employees = value