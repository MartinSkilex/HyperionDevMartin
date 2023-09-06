
# Defining the menu list
menu_list = ['coffee', 'croissant', 'toast', 'muffin']

# Define the stock dictionary of quantities for each item
stock_dict = {'coffee': 25, 'croissant': 30, 'toast': 42, 'muffin': 10}

# Defining the dictionary of prices for each item
price_dict = {'coffee': 28, 'croissant': 12, 'toast': 25, 'muffin': 15}

# Initializing the variable to store the total stock value
total_stock = 0

# Iterating over each item in the menu list
for item in menu_list:
   
    # Calculating the value of the current item by multiplying the stock quantity with the price
    item_value = stock_dict[item] * price_dict[item]

    # Adding the value of the current item to the total stock value
    total_stock += item_value

# Printing the total stock value of the cafe
print(f"The total stock in the cafe is worth: R{total_stock}")