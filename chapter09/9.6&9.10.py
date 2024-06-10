from class_Restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, flavours, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavours = flavours
    def describe_flavours(self):
        words = ''
        for i in self.flavours:
            words += i
            words += ' '
        print(f'The store has flavours: {words}.')

Sukiya = IceCreamStand(['a', 'b', 'c'], 'Sukiiya', 'Japanese Cuisine')
Sukiya.describe_flavours()