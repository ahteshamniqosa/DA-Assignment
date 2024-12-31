# Q1: Given a tuple, print all elements on a new line and create a new tuple by concatenating the first and last elements.
my_tuple = ((1, 2, 3), [4, 5, 6], ('apple', 'banana', 'cherry'), [7, 8, 9])
for element in my_tuple:
    print(element)
new_tuple = my_tuple[0] + tuple(my_tuple[-1])
print("Concatenated tuple:", new_tuple)



# Q2: Work with an inventory dictionary. Add a new book, get all book titles, and remove books out of stock.
inventory = {
    "The Great Gatsby": {"price": 10.99, "quantity": 5},
    "Rich dad poor dad": {"price": 8.99, "quantity": 8},
    "Harry Potter": {"price": 12.50, "quantity": 2},
}
inventory["New Book"] = {"price": 15.99, "quantity": 10}
print("Book titles:", list(inventory.keys()))
inventory = {book: details for book, details in inventory.items() if details["quantity"] > 0}
print("Updated inventory:", inventory)



# Q3: Manage a product catalog with stock updates and adding new products.
products = {
    101: {"name": "Laptop", "category": "Electronics", "price": 1200, "stock": 50},
    102: {"name": "Shirt", "category": "Apparel", "price": 25, "stock": 200},
    103: {"name": "Coffee Maker", "category": "Home Appliances", "price": 80, "stock": 30},
}
products[102]["stock"] += 50
products[104] = {"name": "Smartphone", "category": "Electronics", "price": 699, "stock": 100}
print("Updated products:", products)



# Q4: Remove duplicate items from a shopping list by converting it to a set.
shopping_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
unique_items = set(shopping_list)
print("Unique items:", unique_items)




# Q5: Perform set operations on two course enrollment lists.
course_a = {"Ahmed", "Ayesha", "Bilal", "Zainab"}
course_b = {"Ayesha", "Fatima", "Usman", "Zainab"}
difference = course_a - course_b
print("Course A but not in Course B:", difference)
symmetric_difference = course_a ^ course_b
print("Only in one of the courses:", symmetric_difference)




# Q6: Calculate the sum of all even numbers between 1 and 50 using a for loop.
sum_of_evens = sum(num for num in range(1, 51) if num % 2 == 0)
print("Sum of all even numbers between 1 and 50:", sum_of_evens)



# Q7: Print the multiplication table for a given number (between 1 and 10) using a for loop.
number = int(input("Enter a number between 1 and 10: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")



# Q8: Print the powers of a number (from 1 to 10) using a while loop.
num = int(input("Enter a number: "))
power = 1
while power <= 10:
    print(f"{num}^{power} = {num**power}")
    power += 1



# Q9: Countdown from a given number to 0 and display a finished message.
countdown = int(input("Enter a number to start the countdown: "))
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("Countdown finished!")




# Q10: Generate a right-angled triangle pattern of stars (*) with n rows.
rows = int(input("Enter the number of rows for the triangle: "))
for i in range(1, rows + 1):
    print("* " * i)
