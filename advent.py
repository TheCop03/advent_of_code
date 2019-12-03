import math

# Read the data from file
with open('day1_data.txt') as file:
    modules = file.read().splitlines();

# Total fuel required for the whole spacecraft
total_fuel = 0;

# Loop through the data and calculate the fuel for each module and add to total
for mass in modules:
    fuel = math.floor(int(mass)/3) - 2;
    # Do not add if the answer is negative
    if (fuel > 0):
        total_fuel += fuel;
    fuel = 0;

print(total_fuel)
