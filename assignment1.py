salaries = ['20k', '40k', '50k', '60k', '35k', '89k','40k']

# 1. What is the length of the salaries list.

print(len(salaries))

# 2. Retrieve the third salary in the list by using index.

print(salaries[2])

# 3. Extract the last salary from the list by using a negative index.

print(salaries[-1])

# 4. Slice the salaries list to get only the middle three salaries.

print(salaries[2:5])

# 5. Add a new salary to the list, ‘100k’ by using append() method.

salaries.append("100K")
print(salaries)

# 6. Add a new salary to the list, ‘120k’ without method.

salaries = salaries + ["120k"]
print(salaries)

# 7. Replace the third salary in the list with '55k' and print the updated list.

salaries[2] = "55k"
print(salaries)

# 8. Count how many times '40k' appears in the list.

countOfSalaries = salaries.count("40k")
print(countOfSalaries)

# 9. Insert a new salary at the second position.

salaries[1] = "30k"
print(salaries)

# 10. Reverse the order of the salaries list with method.

reversedSala =  salaries[::-1]
print(reversedSala)

# 11. Reverse the order of the salaries list without method.

reversedSala2 = salaries.reverse()
print(reversedSala2)