class Restaurant:
    def __init__(self,restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'{self.restaurant_name.title()} is a {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        print('Opening')
    def set_number_served(self, number):
        self.number_served = number
    def increment_nnumber_served(self, n):
        self.number_served += n