products = {
    "vegan taco": 2.5, 
    "beef taco": 3, 
    "pork taco": 5, 
    "taco cookie": 1, 
    "salad": 2
}
cart = []

def add_to_cart(product_name): 
    cart = open("cart.txt", 'a', encoding='utf-8') 
    cart.write(product_name + '/n')
    cart.close()

def add_to_cart(product_name):
    if product_name in products:
        cart.append(product_name)
    else:
        print("No")

    print("Cart:", cart)

def remove_from_cart(product_name):
    if product_name in cart:
        cart.remove(product_name)
    else:
        print("No")

    print("Cart:", cart)

def calculate_price():
    sum = 0
    for product in cart:
        price = products[product]
        sum += price
    return sum



while True:
    action = input("Say 'add', 'remove', or 'pay': ")

    if action == 'add':
        product = input("What do you whant? ")
        add_to_cart(product)
    elif action == 'remove': 
        product = input("Chaged your mind? ")
        remove_from_cart(product)
    elif action == 'pay':
       calculate_price()
       
       
       print("total price:", sum)
       break 


def calculate_price():
    sum = 0
    for product in cart:
        price = products[product]
        sum += price

    print("Total price to pay:", sum)


while True:
    action = input("Enter 'add', 'remove' or 'pay': ")

    if action == 'add':
        product = input("Enter product name: ")
        add_to_cart(product)
    elif action == 'remove':
        product = input("Enter product name: ")
        remove_from_cart(product)
    elif action == 'pay':
        calculate_price()
        break