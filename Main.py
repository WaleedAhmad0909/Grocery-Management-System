from Classes import *

#Control of program in this file
if __name__ == "__main__":
    while(1):
        Prod= Product()
        Prod.add_product('Soup', 0.65)
        Prod.add_product('Bread', 0.80)
        Prod.add_product('Milk', 1.30)
        Prod.add_product('Apples', 1.00)
        
        user_response = input('Welcome to the main menu! \n Press 1 to buy \n Press 2 to exit\n')
        
        if user_response == '1':
            
            print('\nThe available products we have in our shop are as follows: \n')
            
            Prod.print_products()
            
            SC= ShoppingCart(Prod)
            
            input_string = input('''\nPlease enter the products you want to buy in the following format:
                                 
PriceBasket product1 product2 product3\n
''')
        
            SC.list_append(input_string)
            
            check_input = SC.check_list()
            
            if check_input != 0:
                SC.calculate_subtotal()
                apples_disc_percentage = 10/100
                SC.calculate_percentage_offer(apples_disc_percentage)
                SC.calculate_product_offer()
                SC.print_result()
                break
                
        elif user_response == '2':
           print('\nThank you! We hope to see you soon')
           break
       
        else:
           print('\nInvalid input. Returning to Main menu..\n')