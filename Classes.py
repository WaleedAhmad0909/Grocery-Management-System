#Class for products
class Product():
    def __init__(self):
        self.prod_attributes = {}
    
    #Add products in our dictionary    
    def add_product(self, product, price):
        self.prod_attributes[product] = {"price":price}
    
    #Print product names using dictionary
    def print_products(self):
        for key, value in self.prod_attributes.items() :
            print(key)
      
#Class for Shopping Cart
class ShoppingCart(Product):
    def __init__(self, Prod):
        self.prod_list = None
        self.subtotal = 0.0
        self.total = 0.0
        self.count_apple = 0
        self.count_soup = 0
        self.count_bread = 0
        self.count_discount = 0
        self.prod_attributes = Prod.prod_attributes
    
    #Add the user input to a list
    def list_append(self, input_string):
        self.prod_list = input_string.split()
        
    #Check if the input entered by user is valid or not    
    def check_list(self):
        
        if self.prod_list[0] != 'PriceBasket':
            print('\nInvalid input. Please enter the products following "PriceBasket". Returning to the main menu..\n')
            return 0
        
        temp_prod_list = []
        check_avail = 1
        for key, value in self.prod_attributes.items():
            temp_prod_list.append(key)
        
        temp_list = list(self.prod_list)
        temp_list.remove("PriceBasket")
        for i in temp_list:
            if i not in temp_prod_list:
                print('\nInvalid input. We do not have', i)
                check_avail = 0
        
        if check_avail == 0:
            print('Returning to the main menu..\n')
        return check_avail
                    

    #Calculate subtotal        
    def calculate_subtotal(self):
        for i in self.prod_list:
                if i in self.prod_attributes:
                    self.subtotal+= self.prod_attributes[i]["price"]

    #Percentage discounts in the below function. In this case, Apple.    
    def calculate_percentage_offer(self, apples_disc_percentage):
        self.total = round(self.subtotal,2)
        for i in self.prod_list:
            if i == 'Apples':
                self.total -= apples_disc_percentage
                self.count_apple+=1
                
    #Discounts against products in the below function i.e., half price of bread for 2 soups                        
    def calculate_product_offer(self):
        for i in self.prod_list:
            if i == 'Soup':
                self.count_soup+=1
                
            if i == 'Bread':
                self.count_bread+=1
        
        
        if self.count_bread > 0 and self.count_soup >= 1:
                self.count_soup = self.count_soup // 2
            
                for i in self.prod_list:
                    if i == 'Bread':
                        if self.count_discount < self.count_soup:
                            self.total -= (self.prod_attributes[i]["price"]/2)
                            self.count_discount+=1
        
        
        
    #Result printed in below function    
    def print_result(self):
        if self.count_apple > 0 or self.count_discount > 0:
            subtotal = round(self.subtotal,2)
            print(f"\nSubtotal: £{subtotal}")
        
        if self.count_apple> 0:
            count_apple = 10*self.count_apple
            print(f"Apples 10% off: {count_apple}p")
        
        if self.count_bread>0 and self.count_soup>=1:
            bread_dis= round(0.5*100*(self.count_discount*self.prod_attributes["Bread"]["price"]),2)
            bread_dis = int(bread_dis)
            print(f"Loaf of bread half price: {bread_dis}p")   
            
        if self.count_apple > 0 or self.count_discount > 0:
            total= round(self.total,2)
            print(f"Total: £{total}\n")  
            
        if round(self.subtotal,2) == round(self.total,2):
            subtotal = round(self.subtotal,2)
            print(f"\nSubtotal: £{subtotal} (No offers available)")
            total = round(self.total,2)
            print(f"Total price: £{total}\n")