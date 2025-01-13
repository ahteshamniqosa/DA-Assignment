# 1. Write a Python function called add_numbers that takes two numbers as arguments and returns their sum. Then, test the function by calling it with two numbers of your choice.

def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print(f"Sum: {result}")



# 2. Write a Python function count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in that string.
# - Example: 'Orange'
# - Output: 3 vowels

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)
vowel_count = count_vowels("Orange")
print(f"Number of vowels: {vowel_count}")



# 3. Create a Python function called currency_converter() that takes two arguments:
# - amount: The amount of money to be converted (in USD).
# - exchange_rate (default is 280): The conversion rate from USD to another currency (e.g., PKR). You can assume the default rate is 1 USD = 280 PKR.
# The function should return a message showing how much the given amount is worth in the target currency (PKR).

def currency_converter(amount, exchange_rate=280):
    converted_amount = amount * exchange_rate
    return f"{amount} USD is equal to {converted_amount} PKR"
print(currency_converter(10))


# 4. Write a Python function display_student_info that accepts the following details about a student:
# - name (Keyword argument): The name of the student.
# - age (Keyword argument): The age of the student.
# - grade (Keyword argument): The grade the student is in.
# - school (Keyword argument): The name of the school the student attends.

def display_student_info(name, age, grade, school):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    print(f"School: {school}")

display_student_info(name="Ahmed", age=15, grade="10th", school="City High School")



# 5. Write a Python function calculate_price that accepts two positional arguments:
# - price: The price of a single item.
# - quantity: The number of items bought.
# - The function should return the total price by multiplying price and quantity.

def calculate_price(price, quantity):
    return price * quantity

total = calculate_price(50, 3)
print(f"Total price: {total}")




# 6. Write a Python function display_prices that takes a product name and an arbitrary number of keyword arguments representing product prices. The function should display each product and its price.
# - Product: Laptop
# - Amazon: $800
# - eBay: $750
# - Walmart: $780


def display_prices(product, **prices):
    print(f"Product: {product}")
    for store, price in prices.items():
        print(f"{store}: ${price}")

display_prices("Laptop", Amazon=800, eBay=750, Walmart=780)



# 7. Write a Python function find_max that takes any number of numerical arguments and returns the maximum number.

def find_max(*numbers):
    return max(numbers)
max_num = find_max(10, 20, 5, 7, 30)
print(f"Maximum number: {max_num}")



# 8. Write a Python function display_info that takes:
# - Positional arguments for the name and age of a person.
# - Keyword arguments for other personal details like address, phone number, and email.
# Example Output:
# - Name: Alice
# - Age: 30
# - Other Details:
#     - address: 123 Main St
#     - phone: 123-456-7890
#     - email: alice@example.com



def display_info(name, age, **details):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print("Other Details:")
    for key, value in details.items():
        print(f"  - {key}: {value}")

display_info("Alice", 30, address="123 Main St", phone="123-456-7890", email="alice@example.com")



# 9. Write a Python function calculate_rectangle that accepts the length and width of a rectangle as arguments. Inside this function, create two nested functions:
# - calculate_area: This function should calculate the area of the rectangle.
# - calculate_perimeter: This function should calculate the perimeter of the rectangle.
# - The main function should return both the area and the perimeter of the rectangle.

def calculate_rectangle(length, width):
    def calculate_area():
        return length * width

    def calculate_perimeter():
        return 2 * (length + width)
    
    return calculate_area(), calculate_perimeter()

area, perimeter = calculate_rectangle(10, 5)
print(f"Area: {area}, Perimeter: {perimeter}")


# Q 10.

# products = [9
#     {"name": "Laptop", "price": 1200, "in_stock": True, "discount": 0.1},
#     {"name": "Smartphone", "price": 800, "in_stock": False, "discount": 0.05},
#     {"name": "Headphones", "price": 150, "in_stock": True, "discount": 0.2},
#     {"name": "Smartwatch", "price": 300, "in_stock": True, "discount": 0},
#     {"name": "Keyboard", "price": 100, "in_stock": True, "discount": 0.15}
# ]

# - Get names of in-stock products:
#   *Use list comprehension to generate a list of names for the products that are in stock.                       
# - Calculate final prices for in-stock products after discount:
#     *For products that have a discount, calculate the final price by applying the discount.
#     *For products with no discount, keep the original price.                                         
# - Generate a list of tuples with the product name and its final price.
# Example Output:
# - In-stock product names: ['Laptop', 'Headphones', 'Smartwatch', 'Keyboard']
# - Discounted prices: [('Laptop', 1080.0), ('Headphones', 120.0), ('Smartwatch', 300), ('Keyboard', 85.0)]


products = [
    {"name": "Laptop", "price": 1200, "in_stock": True, "discount": 0.1},
    {"name": "Smartphone", "price": 800, "in_stock": False, "discount": 0.05},
    {"name": "Headphones", "price": 150, "in_stock": True, "discount": 0.2},
    {"name": "Smartwatch", "price": 300, "in_stock": True, "discount": 0},
    {"name": "Keyboard", "price": 100, "in_stock": True, "discount": 0.15}
]

in_stock_names = [product["name"] for product in products if product["in_stock"]]

discounted_prices = [
    (product["name"], product["price"] * (1 - product["discount"]) if product["discount"] > 0 else product["price"])
    for product in products if product["in_stock"]
]

print(f"In-stock product names: {in_stock_names}")
print(f"Discounted prices: {discounted_prices}")
