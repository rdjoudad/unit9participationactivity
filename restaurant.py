class Restaurant:

    def __init__(self, restaurant_type, cuisine_type):
        self.restaurant_type = restaurant_type
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self, restaurant_type, cuisine_type):
        print(f"This is a {restaurant_type} restaurant. We make {cuisine_type} dishes.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

tensuke_express = Restaurant("Tensuke Express", "Japanese")
tensuke_express.increment_number_served(5)
tensuke_express.increment_number_served(5)
tensuke_express.increment_number_served(5)
print(tensuke_express.number_served)
tensuke_express.set_number_served(0)
print(tensuke_express.number_served)

olive_garden = Restaurant("Olive Garden", "Italian")
the_avenue = Restaurant("The Avenue", "Steakhouse")
bonifacio = Restaurant("Bonifacio", "Filipino")

olive_garden.describe_restaurant("Pasta", "Italian")
the_avenue.describe_restaurant("Steak", "American")
bonifacio.describe_restaurant("Filipino", "Filipino")