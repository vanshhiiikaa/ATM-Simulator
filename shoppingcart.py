cart = []
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "stock": 5
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 500,
        "stock": 10
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 200,
        "stock": 15
    }
]

def show_products():
    print("\n PRODUCTS")
    for product in products:
        print(
            f'ID: {product["id"]}  '
            f'Name: {product["name"]}  '
            f'Price: ₹{product["price"]}  '
            f'Stock: {product["stock"]}'
        )

def add_to_cart():
    show_products()

    product_id = int(input("\nEnter Product ID: "))
    quantity = int(input("Enter Quantity: "))

    for product in products:
        if product["id"] == product_id:

            if quantity > product["stock"]:
                print("Not enough stock!")
                return

            cart.append({
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "quantity": quantity
            })

            product["stock"] -= quantity

            print("✅ Item added to cart.")
            return

    print("Product not found.")

def view_cart():

    if len(cart) == 0:
        print("\nCart is empty.")
        return

    print("\nYOUR CART")

    total = 0

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print(
            f'{item["name"]} | '
            f'Qty: {item["quantity"]} | '
            f'Price: ₹{item["price"]} | '
            f'Subtotal: ₹{subtotal}'
        )

    print(f"\nCurrent Total: ₹{total}")

def remove_item():

    if len(cart) == 0:
        print("Cart is empty.")
        return

    name = input("Enter product name to remove: ")

    for item in cart:

        if item["name"].lower() == name.lower():

            for product in products:
                if product["id"] == item["id"]:
                    product["stock"] += item["quantity"]

            cart.remove(item)

            print("Item removed.")
            return

    print("Item not found.")


def calculate_total():

    total = 0

    for item in cart:
        total += item["price"] * item["quantity"]

    print(f"\nTotal Bill = ₹{total}")


while True:

    print("\nSHOPPING CART")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove Item")
    print("5. Calculate Total")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        remove_item()

    elif choice == "5":
        calculate_total()

    elif choice == "6":
        print("Thank you for using Shopping Cart!")
        break

    else:
        print("Invalid choice.")