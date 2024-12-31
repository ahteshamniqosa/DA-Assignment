# Q1. my_tuple = ( (1, 2, 3), [4, 5, 6], (&#39;apple&#39;, &#39;banana&#39;, &#39;cherry&#39;), [7, 8, 9] )
# • Print all elements from my_tuple on a new line (using for loop)
# • Create a new tuple by concatenating the first and last elements of my_tuple
my_tuple = ( (1, 2, 3), [4, 5, 6], ('apple', 'banana', 'cherry'), [7, 8, 9] )
for item in my_tuple:
    print(item)
new_tuple = my_tuple[0] + my_tuple[-1]
print(new_tuple)


# Q2. inventory = { &quot;The Great Gatsby&quot;: {&quot;price&quot;: 10.99, &quot;quantity&quot;: 5}, &quot;Rich dad poor dad&quot;: {&quot;price&quot;:
# 8.99, &quot;quantity&quot;: 8}, &quot;Harry Potter&quot;: {&quot;price&quot;: 12.50, &quot;quantity&quot;: 2}, }
# • Add a new book in inventory using method and get all book titles using method
# • Remove a book if it&#39;s out of stock
inventory = {
    "The Great Gatsby": {"price": 10.99, "quantity": 5},
    "Rich dad poor dad": {"price": 8.99, "quantity": 8},
    "Harry Potter": {"price": 12.50, "quantity": 2},
}

inventory["The Alchemist"] = {"price": 11.50, "quantity": 3}

for book in inventory:
    print(book)
    
out_of_stock_books = [book for book, details in inventory.items() if details["quantity"] == 0]
for book in out_of_stock_books:
    del inventory[book]
print(inventory)



# Q3. An ecommerce store stores information about its products in a nested dictionary. The outer
# dictionary uses product IDs as keys, and the inner dictionary stores product details like name,
# category, price, and stock quantity.
# products = { 101: {&quot;name&quot;: &quot;Laptop&quot;, &quot;category&quot;: &quot;Electronics&quot;, &quot;price&quot;: 1200, &quot;stock&quot;: 50}, 102:
# {&quot;name&quot;: &quot;Shirt&quot;, &quot;category&quot;: &quot;Apparel&quot;, &quot;price&quot;: 25, &quot;stock&quot;: 200}, 103: {&quot;name&quot;: &quot;Coffee Maker&quot;,
# &quot;category&quot;: &quot;Home Appliances&quot;, &quot;price&quot;: 80, &quot;stock&quot;: 30} }
# • Increase the stock of the &quot;Shirt&quot; product (add 50 more units)
# • Add a new product (e.g., &quot;Smartphone&quot;)
products = {
    101: {"name": "Laptop", "category": "Electronics", "price": 1200, "stock": 50},
    102: {"name": "Shirt", "category": "Apparel", "price": 25, "stock": 200},
    103: {"name": "Coffee Maker", "category": "Home Appliances", "price": 80, "stock": 30},
}
products[102]["stock"] += 50
products[104] = {"name": "Smartphone", "category": "Electronics", "price": 700, "stock": 100}
print(products)


# Q4. You are given a list that contains some duplicate items. Remove the duplicates by converting the
# list to a set.
# shopping_list = [&quot;apple&quot;, &quot;banana&quot;, &quot;apple&quot;, &quot;orange&quot;, &quot;banana&quot;, &quot;grape&quot;]
shopping_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
unique_items = set(shopping_list)
print(unique_items)



# Q5. You are managing a list of students enrolled in two different courses. You need to perform
# various set operations to understand the student enrollment. Task: Create two sets: one for students
# in &quot;Course A&quot; and one for students in &quot;Course B&quot;. Find the students who are in &quot;Course A&quot; but not in
# &quot;Course B&quot; (difference). Find students who are only in one of the two courses (symmetric
# difference). course_a = {&quot;John&quot;, &quot;Alice&quot;, &quot;Bob&quot;, &quot;David&quot;} course_b = {&quot;Alice&quot;, &quot;Eve&quot;, &quot;Charlie&quot;,
# &quot;David&quot;}
# • Find students who are in Course A but not in Course B (difference)
# • Find students who are only in one of the two courses (symmetric difference)
course_a = {"Ali", "Ahmed", "Zaid", "Omar"}
course_b = {"Ahmed", "Eli", "Aisha", "Omar"}
only_in_a = course_a - course_b
print(only_in_a)
only_in_one = course_a ^ course_b
print(only_in_one)



# Q6. Write a Python program that calculates the sum of all even numbers between 1 and 50
# (inclusive) using a for loop.
# Hint
# 1. Initialize a variable to hold the sum (e.g., sum_of_evens).
# 2. Use a for loop to iterate through all numbers from 1 to 50.
# 3. Inside the loop, check if the number is even.
# 4. If the number is even, add it to sum_of_evens.
# 5. After the loop finishes, print the total sum of all even numbers between 1 and 50.
sum_of_evens = 0
for number in range(1, 51):
    if number % 2 == 0:
        sum_of_evens += number
print(sum_of_evens)


# Q7. Write a Python program that prints the multiplication table for a given number (between 1 and
# 10) using a for loop.
# Hint:
# 1. Ask the user for a number between 1 and 10 .
# 2. Use a for loop to iterate through the numbers from 1 to 10.
# 3. For each iteration, calculate the product of the given number and the current number in the
# loop.
# 4. Print the result in a readable format (e.g., 5 x 1 = 5).
# 5. Ensure the program works correctly for any number between 1 and 10.
# Output Hint:
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40
num = int(input("Enter a number between 1 and 10: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# Q8. Power of a Number
# Write a Python program that takes a number and prints the powers of the number (starting from 1
# to 10) using a while loop. For example, if the user inputs 3, the output should be:
# 3^1 = 3
# 3^2 = 9
# 3^3 = 27
# ... up to 3^10.
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{number}^{i} = {number**i}")
    i += 1


# Q9. Problem Statement: Write a Python program that takes an integer input from the user and
# counts down from that number to 0. The program should display the current number at each step
# until it reaches 0, at which point it should print a message indicating the countdown is finished
# Output Hint:
# Enter a number to start the countdown: 3
# 3
# 2
# 1
# 0
# Countdown finished!
num = int(input("Enter a number to start the countdown: "))
while num >= 0:
    print(num)
    num -= 1
print("Countdown finished!")


# Q10. Write a Python program that takes an integer input n from the user and generates a right-
# angled triangle pattern of stars (*) with n rows. The first row should contain 1 star, the second row 2
# stars, the third row 3 stars, and so on until the nth row.
# Ensure the stars in each row are separated by spaces, and each row starts on a new line.
# # Pattern:
# *
# **
# ***
# ****
# *****
n = int(input("Enter the number of rows for the triangle: "))
for i in range(1, n + 1):
    print("* " * i)
