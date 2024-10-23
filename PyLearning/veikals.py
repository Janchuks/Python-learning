products = {
    "vegan taco": 2.5, 
    "beef taco": 3, 
    "pork taco": 5, 
    "taco cookie": 1, 
    "salad": 2
}

def add_to_cart(product_name):
    cart = open("cart.txt", 'a', encoding='utf-8')
    cart.write(product_name + '\n')
    cart.close()

def remove_from_cart(product_name):
    cart = open('cart.txt', 'r', encoding='utf-8')
    cart_list = cart.readlines()
    cart.close()
    if product_name in cart_list: 
      cart_list.remove(product_name + '\n')
      cart = open('cart.txt', 'w', encoding='utf-8')
      cart.writelines(cart_list)
      cart.close()
    else:
        print("not in cart")
def calculate_price():
    cart = open('cart.txt', 'r', encoding='utf-8')
    cart_list = cart.readlines()
    cart.close()
    sum = 0
    for product in cart_list:
        price = products[product[0:-1]]
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