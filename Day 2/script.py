f = open('list.txt', 'r')

content = f.read()

#first, organize into reports, seperated by lines.
reports = content.split('\n')

# now, each element in our list is a report. We can iterate over them, and check the values according to the rules.

# Part 1 - Count the number of reports that are safe.
# A report only counts as safe if both of the following are true:
# rule 1: The levels are either all increasing or all decreasing.
# rule 2: Any two adjacent levels differ by at least one and at most three.

safe = []

for value in reports:
    # rule 1 - test and record value if safe
    levels = list(map(int, value.split()))

    # Check rule 1: Levels are either all increasing or all decreasing
    increasing = all(levels[i] > levels[i-1] for i in range(1, len(levels)))
    decreasing = all(levels[i] < levels[i-1] for i in range(1, len(levels)))
    
    if not (increasing or decreasing):
        continue  # Skip this report if it fails rule 1

    differences_valid = all(1 <= abs(levels[i] - levels[i-1]) <= 3 for i in range(1, len(levels)))
    
    if differences_valid:
        safe.append(value)

print("Number of safe reports in Part 1: ", len(safe))

# Part 2 - Find the number of valid reports if safety systems tolerate a single bad level.
# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
mistakes = 0
valid_reports = 0
for value in reports:
    # rule 1 - test and record value if safe
    levels = list(map(int, value.split()))

    current_mistakes = 0

    # Check rule 1: Levels are either all increasing or all decreasing. Has fault tolerance of 1 mistake.
