
f = open('list.txt', 'r')

content = f.read()

content = content.replace('   ', '\n', -1)

content = content.split('\n')

# list is now LHS, RHS, LHS, RHS, LHS, RHS, ...

length = len(content)

listLHS = []
listRHS = []

for i in range(length):
    if i % 2 == 0:
        listLHS.append(content[i])
    else:
        listRHS.append(content[i])

# Pair up the smallest number in the left list with the smallest number in the right list, 
# then the second-smallest left number with the second-smallest right number, and so on.

# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. 
# For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4;
# if you pair up a 9 with a 3, the distance apart is 6.

# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found.
# In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

sortLHS = sorted(listLHS)
sortRHS = sorted(listRHS)

# convert to integers
sortLHS = [int(i) for i in sortLHS]
sortRHS = [int(i) for i in sortRHS]

distance = 0

for i in range(1000):
    distance += abs(sortLHS[i] - sortRHS[i])

print("Total distance between the left list and the right list is", distance) # Answer was 2192892

# Part Two - Similarity - compare the two lists and find the number of elements that are the same in each.
# match by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

count = 0
simR = 0
count1 = 0
simL = 0

for i in range(len(sortLHS)):
    # Count occurrences of sortLHS[i] in sortRHS
    count = sortRHS.count(sortLHS[i])
    
    # Debug print
    if count > 0:  # Only print if the number is present in the right list
        print(sortLHS[i], "appears in the right list", count, "times.")
        # Add to similarity score
        simL += sortLHS[i] * count
    

print("The similarity score is", simL) # 22962826

for i in range(len(sortRHS)):
    # Count occurrences of sortRHS[i] in sortLHS
    count1 = sortLHS.count(sortRHS[i])
    
    # Debug print
    if count1 > 0:  # Only print if the number is present in the left list
        print(sortRHS[i], "appears in the left list", count1, "times.")
        # Add to similarity score
        simR += sortRHS[i] * count1
    

print("The similarity score is", simR) # 22962826

# Even though it says 'consider both sides' Answer was 22962826