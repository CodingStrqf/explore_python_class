from graph import *

entreprise = Company(
    name="Tech Innovators",
    employees=[
        Person(
            name="Jean Dupont",
            age=30,
            address=Address(
                street="123 Rue de Paris",
                city="Paris",
                postal_code="75001",
                country=Country(name="France", code="FR")
            )
        )
    ]
)
afficher_objet_depliable(entreprise)