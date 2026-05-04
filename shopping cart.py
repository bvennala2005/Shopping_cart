# Simple Shopping Cart 

# Product list
products = {
    "Book": 50,
    "Scale": 30,
    "Geomenry box": 120,
    "Pens": 40,
    "Water Bottle": 80
}

# Admin Login
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == "admin" and password == "123":
        print("Login successful")
        return True
    else:
        print("Wrong username or password")
        return False


# View Products
def view_products():
    print("\nAvailable Products are:")
    for item in products:
        print(item, "→ ₹", products[item])


# Add New Product
def add_product():
    name = input("Enter new product name: ")
    price = int(input("Enter product price: "))

    products[name] = price
    print("Product added successfully")


# Add Item to Cart
def add_to_cart(cart):
    name = input("Enter product name: ")

    if name in products:
        qty = int(input("Enter quantity: "))

        # If already in cart, increase quantity
        if name in cart:
            cart[name] = cart[name] + qty
        else:
            cart[name] = qty

        print("Item added to cart")
    else:
        print("Product not found")


# Remove Item from Cart
def remove_from_cart(cart):
    name = input("Enter product name to remove: ")

    if name in cart:
        del cart[name]
        print("Item removed")
    else:
        print("Item not in cart")


# View Cart
def view_cart(cart):
    if len(cart) == 0:
        print("Cart is empty")
    else:
        print("\nYour Cart:")
        for item in cart:
            price = products[item]
            qty = cart[item]
            print(item, "→ ₹", price, "x", qty)


# Calculate Total Cost
def get_total(cart):
    total = 0

    for item in cart:
        price = products[item]
        qty = cart[item]
        total = total + (price * qty)

    print("Total Cost = ₹", total)
    return total


# Add GST
def add_gst(total):
    gst = total * 0.18
    final_amount = total + gst

    print("GST (18%) = ₹", gst)
    print("Final Amount = ₹", final_amount)


# Main Program
def main():
    cart = {}

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")

        choice = input("Enter your choice: ")

        # ADMIN
        if choice == "1":
            if admin_login():
                while True:
                    print("\n--- ADMIN MENU ---")
                    print("1. View Products")
                    print("2. Add Product")
                    print("3. Back")

                    admin_choice = input("Enter choice: ")

                    if admin_choice == "1":
                        view_products()

                    elif admin_choice == "2":
                        add_product()

                    elif admin_choice == "3":
                        break

                    else:
                        print("Invalid choice")

        # CUSTOMER
        elif choice == "2":
            customer_name = input("Enter your name: ")
            print("Welcome", customer_name)

            while True:
                print("\n--- CUSTOMER MENU ---")
                print("1. View Products")
                print("2. Add Item to Cart")
                print("3. Remove Item from Cart")
                print("4. View Cart")
                print("5. Get Total Cost")
                print("6. Add GST")
                print("7. Back")

                customer_choice = input("Enter choice: ")

                if customer_choice == "1":
                    view_products()

                elif customer_choice == "2":
                    add_to_cart(cart)

                elif customer_choice == "3":
                    remove_from_cart(cart)

                elif customer_choice == "4":
                    view_cart(cart)

                elif customer_choice == "5":
                    total = get_total(cart)

                elif customer_choice == "6":
                    total = get_total(cart)
                    add_gst(total)

                elif customer_choice == "7":
                    break

                else:
                    print("Invalid choice")

        # EXIT
        elif choice == "3":
            print("Thank you for visiting")
            break

        else:
            print("Invalid choice")


# Run Program
main()