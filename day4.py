# Check when going from left to right, the digits never decrease (Part 1 and 2)
def increasing_nums(x):
    last_num = 0;
    for i in str(x):
        if (int(i) < last_num):
            return False
        elif (int(i) >= last_num):
            last_num = int(i)

    return True

# Check whether two adjacent digits are the same (Part 1)
def two_same_adj(x):
    last_num = 0;
    for i in str(x):
        if (int(i) == last_num):
            return True
        elif (int(i) != last_num):
            last_num = int(i)

    return False

# Check whether two adjacent digits are the same and not more than that (Part 2)
def exactly_two_same_adj(x):
    last_num = 0
    num_adj = 0

    for i in str(x):
        # Still looking for two same adjacent digits
        if (num_adj < 2):
            # First digit of possible two same adjacent digits
            if (int(i) != last_num):
                last_num = int(i)
                num_adj  = 1
            # Second digit of two same adjacent digits. Check third digit now.
            elif (int(i) == last_num):
                num_adj += 1
        # Found two adjacent digits. Check third digit.
        elif (num_adj == 2):
            # More than two same adjacent digits
            if (int(i) == last_num):
                num_adj += 1
            # Exactly two same adjacent digits
            elif (int(i) != last_num):
                return True
        # Found more than two same adjacent digits
        elif (num_adj > 2):
            # Consume until you find a different digit
            if (int(i) == last_num):
                num_adj += 1
            # Restart count with new digit
            elif (int(i) != last_num):
                last_num = int(i)
                num_adj  = 1

    return True if num_adj == 2 else False

low_range = 245182
high_range = 790572
possible_results = 0

# Go through the range (Part 1)
# for x in range(low_range, high_range + 1):
#     if increasing_nums(x) and two_same_adj(x):
#         possible_results += 1

# Go through the range (Part 2)
for x in range(low_range, high_range + 1):
    if increasing_nums(x) and exactly_two_same_adj(x):
        possible_results += 1

print(possible_results)
