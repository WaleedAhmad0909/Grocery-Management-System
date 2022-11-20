# How to set up and run the code
* Download the files `Classes` and `Main` in the same folder.
* `Classes` file contains `Product` and `ShoppingCart` classes while `Main` file controls the flow of the program.

# Explanation of the flow of Program
* On executing the code, the program will go to the main menu.
* Main menu will have two options:
    * Press `1` to buy.
    * Press `2` to quit.
* After pressing `1`, user will have the description of the products available and how to buy.
* User will have to enter the products in the format: `PriceBasket product1 product2 product3`
    * If the format and products are correct, the program will return the `subtotal`, `discounts(if any)` and `total` and the program will exit.
    * If the format or products are incorrect, the program will give an `invalid input` error and return to main menu with the `buy` or `exit` option again.
    * The program is case sensitive as per the input requirements in the assignment.

# Explanation about the code
* The prices of products having prices in `Pence` are stored after converting to `Pounds`.
* The available products are stored in a `dictionary`.
    * `Product name` is stored as a `key`.
    * `Price` is stored in a `nested dictionary`. The nested dictionary will make it easier to add further attributes of a product if required. For example origin, barcode etc.
* There are two Classes:
    * `Product Class`: This is a Class to store the attributes and methods related to the product.
    * `ShoppingCart Class`: This Class contains attributes and methods related to the shopping cart. It also receives the product `dictionary` from `Product Class`.
* The two classes are seperated to ensure a clean readable code as well as smooth extendibility in the future.
* Both classes are kept in the same file because they are tightly coupled.
* Brief one line explanation of each method is added above the respective method in the code.
# Brief description of methods used in Classes
* `Product Class`:
    * `add_product(self, product, price)`: Takes product name and price as input and stores it in a dictionary.
    * `print_products`(): Prints the list of `product names` in the shop.

* `ShoppingCart Class`:
    * `list_append(self, input_string)`: Gets user input and inserts into a list.
    * `check_list()`: Validates if the list entered by user is valid or not. Below are the validation checks:
        * The list should start with `PriceBasket`. If not, the input is invalid.
        * After `PriceBasket`. All the products entered should be available. One wrong input would result in an `invalid input` error.
    * `calculate_subtotal()`: The products entered are simply added up to calculate a subtotal.
    * `calculate_percentage_offer(self, apples_disc_percentage)`: Flat discount for buying Apple is calculated in this method and adjusted in subtotal. In future for other products, all flat discounts can be adjusted in this method.
    * `calculate_product_offer()`: Discount on bread for buying 2 soups is adjusted in this method. For future, all product based discounts can be adjusted in this method.
    * `print_result()`: The conditions are checked to see if there is any discount applied or not and the output is printed.