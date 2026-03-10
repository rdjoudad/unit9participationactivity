class Restaurant:

    def __init__(self, restaurant_type, cuisine_type):
        self.restaurant_type = restaurant_type
        self.cuisine_type = cuisine_type

    def describe_restaurant(restaurant_type, cuisine_type):
        print(f"This is a {restaurant_type} restaurant. We make {cuisine_type} dishes.")

    def open_restaurant():
        print("This restaurant is open.")

