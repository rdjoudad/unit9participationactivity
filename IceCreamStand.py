from restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_type, cuisine_type):
        super().__init__(restaurant_type, cuisine_type)
        self.flavors =  ["Vanilla", "Chocolate", "Strawberry", "Cookies and Cream", "Blueberry"]

    
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

graeters = IceCreamStand("Graeters", "Ice Cream Dessert")
graeters.describe_restaurant()
print(f"Our ice cream flavors are: ")
graeters.show_flavors()



