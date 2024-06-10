class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name.title()} is a {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        print('Opening')

Sukiya = Restaurant('Sukiiya', 'Japanese Cuisine')
print(Sukiya.restaurant_name)
print(Sukiya.cuisine_type)
Sukiya.describe_restaurant()
Sukiya.open_restaurant()

McDonald = Restaurant('McDonald', 'fast food')
Haidilao = Restaurant('Haidilao', 'hot pot')
McDonald.describe_restaurant()
Haidilao.describe_restaurant()