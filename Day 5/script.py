import re
from collections import defaultdict, deque

with open('list.txt') as f:
    content = f.read()

# Task 1 : order pages based on update rules
# The notation X|Y means that if both page number X and page number Y are to be 
# produced as part of an update, page number X must be printed at some point before
# page number Y

# The second section specifies the page numbers of each update. 
# Because most safety manuals are different, the pages needed in the updates are 
# different too. The first update, 75,47,61,53,29, means that the update consists 
# of page numbers 75, 47, 61, 53, and 29.
rules = []
updates = []

for value in content.split('\n'):
    if re.match(r'\d+\|\d+', value):
        rules.append(tuple(map(int, value.split('|'))))  # Convert to tuples of integers
    elif len(value.strip()) > 0:
        updates.append(list(map(int, value.split(','))))  # Convert update strings to lists of integers

# check if update orders are correct, and reorder if necessary. use the rules to determine
# the correct order of the updates.

# Step 2: Helper function to check if a page ordering is valid
def is_valid_order(pages, rules):
    for x, y in rules:
        # Find the indices of x and y in the pages
        if x in pages and y in pages:
            x_index = pages.index(x)
            y_index = pages.index(y)
            if x_index > y_index:  # If x appears after y, the order is invalid
                return False
    return True

# Step 3: Recursive function to fix the update by removing invalid elements
def fix_update(pages, rules):
    if is_valid_order(pages, rules):
        return pages  # If valid, return the pages as they are

    for x, y in rules:
        if x in pages and y in pages:
            x_index = pages.index(x)
            y_index = pages.index(y)
            if x_index > y_index:
                # Remove the invalid element and recursively fix the rest
                if x_index > y_index:
                    pages.pop(x_index)
                else:
                    pages.pop(y_index)
                return fix_update(pages, rules)  # Recursively check again

# Step 4: Process each update
fixed_updates = [fix_update(update[:], rules) for update in updates]  # Use a copy to avoid modifying the original list

# Step 4: Compute the median index
def median_index(pages):
    n = len(pages)
    if n == 0:
        return None  # No median for an empty list
    elif n % 2 == 1:
        return n // 2  # Middle index for odd-length list
    elif n % 2 == 0:
        return (n // 2 - 1 + n // 2) // 2 # Lower middle index for even-length list

# Step 5: Process updates and sum medians
def sum_of_medians(fixed_updates):
    total = 0
    for pages in fixed_updates:
        if not pages:  # Skip empty lists
            continue
        med_index = median_index(pages)
        if med_index is 0 <= med_index < len(pages):
            total += pages[med_index]
    return total

# Process updates and compute medians
medians = [median_index(update) for update in fixed_updates]
median_sum = sum_of_medians(fixed_updates)
    

# Output results 
# 1462 too low
print("Fixed updates:", fixed_updates)
print("Sum of median elements:", median_sum)