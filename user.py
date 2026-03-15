class User:

    def __init__(self, first_name, last_name, alma_mater, workplace):
        self.first_name = first_name 
        self.last_name = last_name
        self.alma_mater = alma_mater
        self.workplace = workplace


    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}. The user graduated from {self.alma_mater} and now works at {self.workplace}.")

    def greet_user(self):
        print(f"Good morning, {self.first_name} {self.last_name}!")


john_smith = User("John", "Smith", "The Ohio State University", "Nvidia")
john_smith.describe_user()
john_smith.greet_user()

ethan_brown = User("Ethan", "Brown", "Western Governors University", "Amazon Web Services")
ethan_brown.describe_user()
ethan_brown.greet_user()