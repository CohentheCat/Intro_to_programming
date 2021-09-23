class Pizza:
   def __init__(self, size, num_cheese, num_pepp, num_ham):
       self.size = size
       self.num_cheese = num_cheese
       self.num_pepp = num_pepp
       self.num_ham = num_ham
   #setters
   def setSize(self, size):
       self.size = size
   def setCheese(self, num_cheese):
       self.num_cheese = num_cheese
   def setPepp(self, num_pepp):
       self.num_pepp = num_pepp
   def setHam(self, num_ham):
       self.num_ham = num_ham   
   #getters
   def getSize(self):
       return self.size
   def getCheese(self):
       return self.num_cheese
   def getPepp(self):
       return self.num_pepp
   def getHam(self):
       return self.num_ham 

   def calculate_cost(self):
       prices = {"small" : 10.00, "medium" : 12.50, "large" : 14.50, "toppings" : 2.00}
       basePrice = prices[self.getSize()]
       cheesePrice = prices["toppings"] * self.getCheese()
       peppPrice = prices["toppings"] * self.getPepp()
       hamPrice = prices["toppings"] * self.getHam()
       totalPrice = basePrice + cheesePrice + peppPrice + hamPrice
       formatedTotal = "{:.2f}".format(totalPrice)
       return formatedTotal

   def get_discription(self):

       return f"A {self.getSize()} Pizza with [{self.getCheese()} Cheese topping][{self.getPepp()} Pepporoni topping][{self.getHam()} Ham Topping] costs ${self.calculate_cost()}. \n"    
       
       
running = True
order_list = []
while running:
    size = input("What size pizza would you like? (small, medium, large)")
    cheese = int(input("What level of cheese would you like? (1-3): "))
    pepporoni = int(input("What level of pepporoni would you like? (1-3): "))
    ham = int(input("What level of ham would you like? (1-3): "))
    new_order = Pizza(size, cheese, pepporoni, ham)
    order_list.append(new_order)
    for orders in order_list:
        print(orders.get_discription())





