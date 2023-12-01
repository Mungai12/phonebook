class Contact:
    """A class modelling a contact"""
    def __init__(self):
        self.details = {'name': input("Enter the name: "), 'email': input("Enter email: "),
                        'Tel': input("Enter number: ")}

