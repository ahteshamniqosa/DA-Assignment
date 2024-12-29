# Q1. Check a person’s eligibility for a loan based on their age, credit score, and income.
# Eligibility Criteria:
# - Must be 18 years or older.
# - Credit score should be 650 or higher with income of 30000 or more.
# - If credit score is 700 or above, eligible with income of 25000 or more.

age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))
income = int(input("Enter your annual income: "))

if age >= 18:
    if credit_score >= 700 and income >= 25000:
        print("You are eligible for the loan.")
    elif credit_score >= 650 and income >= 30000:
        print("You are eligible for the loan.")
    else:
        print("Sorry, you are not eligible for the loan.")
else:
    print("Sorry, you are not eligible for the loan.")





# Q2. Check if a person is an adult and categorize their experience.
# If underage, just show "You are underage."
# For adults, classify experience based on years.

age = int(input("Enter your age: "))

if age < 18:
    print("You are underage.")
else:
    experience = int(input("Enter your years of experience: "))
    if experience >= 10:
        print("You have a lot of experience.")
    elif 5 <= experience <= 9:
        print("You have moderate experience.")
    elif 2 <= experience <= 4:
        print("You are relatively new.")
    else:
        print("You are just starting out.")





# Q3. Explore variables:
# a) Check if Python assigns the same address to variables with the same value.
# b) Find memory size and identify the type with the smallest memory.
# c) Print the type with the smallest memory usage.

a = 15
b = 15.5
c = "Ahmed"
d = [10, 20, 30]

variables = [a, b, c, d]
memory_sizes = []

for var in variables:
    print(f"Memory address of {var}: {id(var)}")
    size = var.__sizeof__()
    memory_sizes.append((type(var).__name__, size))

min_memory = min(memory_sizes, key=lambda x: x[1])
print("The type with the smallest memory is:", min_memory[0])






# Q4. Validate an email address.
# Check if it contains "@" and ".".

email = input("Enter your email address: ")

if "@" in email and "." in email:
    print("Email format is valid.")
else:
    print("Invalid email format.")





# Q5. Find the data types of elements in a tuple and display them in a list.

x = (10, 20.5, 'Ali', [1, 2, 3], ('a', 'b'))
data_types = [type(element).__name__ for element in x]
print("Data types of tuple elements:", data_types)





# Q6. Check if a username exists and verify if it's an admin.

users = [("Aisha", "admin"), ("Hassan", "user"), ("Fatima", "moderator")]

username = input("Enter username: ")
role = input("Enter role: ")

if any(user[0] == username for user in users):
    print("Username exists.")
    if (username, role) is ("Aisha", "admin"):
        print("This user is an admin.")
else:
    print("Username does not exist.")





# Q7. Determine relationships based on family data.
# If person1 and person2 have the same family, print "Siblings".
# If person1 and person3 have the same district but different family, print "Cousins".

person1 = ['Ali', 'Raya', 'Karachi', 12345]
person2 = ['Ali', 'Raya', 'Karachi', 12345]
person3 = ['Hassan', 'Mehwish', 'Karachi', 67890]

if person1 == person2:
    print("Relation: Siblings")
elif person1[2] == person3[2]:
    print("Relation: Cousins")




 

# Q8. Store and display book details using a tuple.

title = input("Enter book title: ")
author = input("Enter book author: ")
year = int(input("Enter year of publication: "))
price = float(input("Enter book price: "))

book = (title, author, year, price)
print(f"Book Details: Title: {book[0]}, Author: {book[1]}, Year: {book[2]}, Price: {book[3]}")







# Q9. Check if a subject is available in the offered list.

subjects = ["Math", "Science", "English", "History"]
chosen_subject = input("Enter a subject: ")

if chosen_subject in subjects:
    print("Subject is available.")
else:
    print("Subject is not available.")






# Q10. Tuple operations: Find index of a number and count its occurrences.

numbers = (1, 2, 3, 2, 4, 5, 2, 6)

num1 = int(input("Enter a number to find its index: "))
if num1 in numbers:
    print(f"First occurrence of {num1} is at index {numbers.index(num1)}")
else:
    print(f"{num1} is not in the tuple.")

num2 = int(input("Enter another number to count: "))
print(f"{num2} appears {numbers.count(num2)} times in the tuple.")






# Hard Question: Categorize weather based on temperature.
# Freezing: ≤ -5, Normal: ≤ 25, Hot: ≥ 40.

temperature = float(input("Enter the current temperature in Celsius: "))

if temperature <= -5:
    print("The weather is freezing.")
elif temperature <= 25:
    print("The weather is normal.")
elif temperature >= 40:
    print("The weather is hot.")
else:
    print("The weather is moderate.")
