# Answer__1: Age-based categorization
def Answer__1():    
    try:
        age = int(input("Enter the age of the person: "))  
        if age < 0:
            print("Please enter a non-negative number.")  
        elif age <= 12:
            print("Child")  
        elif age <= 19:
            print("Teenager") 
        elif age <= 64:
            print("Adult")  
        else:
            print("Senior")  
    except ValueError:
        print("Please enter a valid number.")  
Answer__1()



# Answer__2: Membership discount eligibility
membership_status = input("Enter membership status (premium/regular): ").strip().lower()  
purchase_amount = float(input("Enter purchase amount: "))  
if (membership_status == "premium" and purchase_amount >= 1000) or \
   (membership_status == "regular" and purchase_amount >= 2000):
    print("Accepted for discount")  
else:
    print("Not Accepted for discount")  



# Answer__3: Voting eligibility based on age and citizenship
age = int(input("Enter your age: "))  
citizenship_status = input("Enter your citizenship status (citizen/non-citizen): ").strip().lower()  
special_region = input("Are you from a special region where voting is allowed at 16? (yes/no): ").strip().lower()  
if (age >= 18 and citizenship_status == "citizen") or (age >= 16 and citizenship_status == "citizen" and special_region == "yes"):
    print("Accepted to vote")  
else:
    print("Not Accepted to vote")  



# Answer__4: Bonus eligibility based on performance and years of service
performance_rating = input("Enter performance rating (Excellent/Good/Satisfactory): ").strip().lower() 
years_of_service = int(input("Enter years of service: ")) 
if (performance_rating == "excellent" and years_of_service >= 5) or \
   (performance_rating == "good" and years_of_service >= 10) or \
   (performance_rating == "satisfactory" or years_of_service >= 15):
    print("Accepted for bonus")  
else:
    print("Not Accepted for bonus")  



# Answer__5: String manipulation to replace spaces with underscores
text = "I'm learning Python programming?"  
updated_text = text.replace(' ', '_')  
underscore_count = updated_text.count('_')  
first_underscore_position = updated_text.find('_') 
print(f"Updated text: {updated_text}")
print(f"Number of underscores: {underscore_count}")
print(f"Position of the first underscore: {first_underscore_position}")



# Answer__6: String slicing and reversal
text = input("Enter a string: ")  
print("All characters except the last 3:", text[:-3])  
print("Every second character:", text[::2])  
print("Reversed string:", text[::-1])  



# Answer__7: Reversing words in a sentence
text = "Hello World, We are learning Python"  
words = text.split()  
reversed_words = words[::-1] 
reversed_sentence = ' '.join(reversed_words)  
print(reversed_sentence)



# Answer__8: Extracting product code number
product_code = "SKU-12345-XYZ"  
number = product_code.replace("SKU-", "").replace("-XYZ", "")  
print("Extracted number:", number)



# Answer__9: Password validation for different conditions
import string
password = input("Enter a password: ")  
contains_upper = any(char.isupper() for char in password)  
contains_lower = any(char.islower() for char in password)  
contains_space = any(char.isspace() for char in password)  
contains_special = any(char in string.punctuation for char in password)  
print(f"Contains uppercase: {contains_upper}")
print(f"Contains lowercase: {contains_lower}")
print(f"Contains spaces: {contains_space}")
print(f"Contains special characters: {contains_special}")



# Answer__10: Finding the longest word in a sentence
sentence = "programming in Python"  
words = sentence.split()  
longest_word = max(words, key=len)  
print("Longest word:", longest_word)
