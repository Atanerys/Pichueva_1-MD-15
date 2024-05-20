def zad1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на кухне {self.cuisine_type}.")

        def open_restaurant(self):
            print("Ресторан открыт!")

    newRestaurant = Restaurant("Toca", "японская")

    print("Название ресторана:", newRestaurant.restaurant_name)
    print("Тип кухни:", newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
def zad2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на кухне {self.cuisine_type}.")

    restaurant1 = Restaurant("La  France", "французская")
    restaurant2 = Restaurant("pokke", "корейская")
    restaurant3 = Restaurant("Toca", "японская")


    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def zad3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, initial_rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = initial_rating

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на кухне {self.cuisine_type}.")
            print(f"Рейтинг ресторана: {self.rating}")

        def open_restaurant(self):
            print("Ресторан открыт!")

        def update_rating(self, new_rating):
            self.rating = new_rating
    restaurant1 = Restaurant("Toca", "японская", 4.5)
    restaurant1.describe_restaurant()
    restaurant1.update_rating(4.8)
    restaurant1.describe_restaurant()
zad3()