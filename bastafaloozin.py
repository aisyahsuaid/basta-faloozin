# This program is about an Italian restaurant called Basta Fazoolin

# Creating Menu class
class Menu:
  # initial contstructor when menu object is created
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  # String representation when menu is called out 
  def __repr__(self):
    return 'You can order dishes from the {} menu from {} to {}'.format(self.name,self.start_time, self.end_time)
  # method to calculate the bill
  def calculate_bill(self, purchased_items):
    total_bill = 0
    #purchased items is given in a list
    for items in purchased_items:
      if items in self.items:
        total_bill += self.items[items] # getting price
    return "Your total bill is ${}".format(total_bill)
  
  

# The restaurant has 4 menu types 

# Each menu items is shown in a dictionary showing dishes as key and price as value
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

# Creating menu objects for each menu
brunch = Menu('brunch', brunch_items, 1100, 1600)

early_bird = Menu('Early-bird', early_bird_items, 1500, 1800)

dinner = Menu('dinner', dinner_items, 1700, 2300)

kids = Menu('kids', kids_items, 1100, 2100)

print(brunch)
# Testing calculate bill method using brunch menu
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

# Testing calculate bill method using early bird menu
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Business is booming, the restaurant is now a franchise with fantastic menus

# Creating Franchise class
class Franchise:
  # Initial constructor
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  # String representation  
  def __repr__(self):
    return"The address of this franchise is: {}".format(self.address)
  # Method to list our menus that are available at a given time
  def available_menus(self, time):
    avail_menus = []
    #looping through menu 
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        avail_menus.append(menu)
    return avail_menus

  


    
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry', [brunch, early_bird, dinner, kids])

# Testing available menu method at 12 noon
print(flagship_store.available_menus(1200))

# Testing available menu method at 5pm
print(new_installment.available_menus(1700))

# Again super successfull now we're looking to sell other products

# Creating Business class

class Business:
  # Initial Constructor
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    return 'The business is called {}'.format(self.name)

# Creating a new business
new_biz = Business("Basta Fazoolin", [flagship_store, new_installment])

# Before creating new business we need a Franchise, and before that we need a new menu

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
# Arepa menu object
arepa = Menu('Arepa', arepas_menu, 1000, 2000)
# Arepa Franchise object
arepas_place = Franchise('189 Fitzgerald Avenue', arepa)
# Arepa Business object
arepa_business = Business("Take a' Arepa!", arepas_place)

print(arepa_business)

