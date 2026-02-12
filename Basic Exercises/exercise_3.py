# EXERCISE 3: LISTS

# Write a program that prints:
# The temperature on Wednesday (index 2)
# The maximum temperature
# The minimum temperature
# The average temperature (rounded to 1 decimal)
# The number of days above 17 degrees
# The list sorted from lowest to highest


temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

t_above = 0
for i in temperatures:
    if i >= 17:
        t_above += 1

temperatures.sort()

print("Wednesday Tª:", temperatures[1])
print("Max Tª:", max(temperatures))
print("Min Tª:", min(temperatures))
print("Average Tª:", round((sum(temperatures)/len(temperatures)), 2))
print("Days above 17 degrees:", t_above)
print("Sorted from lowest to highest:", temperatures)
