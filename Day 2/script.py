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

print("Number of safe reports in Part 1: ", len(safe)) # 483

# inversely select the reports that are not safe
unsafe = [value for value in reports if value not in safe]

print("Number of unsafe reports in Part 1: ", len(unsafe)) # 517
print("Total number of reports: ", len(reports))

# Part 2 - Find the number of valid reports if safety systems tolerate a single bad level.
# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, 
# the report instead counts as safe.
mistakes = 0
safe_adjusted = []

for value in unsafe:
    levels = list(map(int, value.split()))

    for i in range(len(levels)):
        # Create a new list excluding the current level to simulate removal
        modified_levels = levels[:i] + levels[i+1:]

        # Check rule 1: Levels are either all increasing or all decreasing
        increasing = all(modified_levels[j] > modified_levels[j-1] for j in range(1, len(modified_levels)))
        decreasing = all(modified_levels[j] < modified_levels[j-1] for j in range(1, len(modified_levels)))

        if not (increasing or decreasing):
            continue  # Skip this modification if it fails rule 1

        # Check rule 2: Differences between adjacent levels are valid
        differences_valid = all(1 <= abs(modified_levels[j] - modified_levels[j-1]) <= 3 for j in range(1, len(modified_levels)))

        if differences_valid:
            safe_adjusted.append(value)
            break  # No need to test further removals for this report

# Combine original safe reports and adjusted safe reports
all_safe_reports = set(safe + safe_adjusted)

print("Number of safe reports in Part 2:", len(all_safe_reports)) # 528

