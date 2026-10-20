# Program 1
# Basic Method

scores = [("Riya", 85),("Aman", 90),("Neha", 90),("Kabir", 72)]

# First, here's how we'd sort by score alone:
def get_score(record):
    return record[1]

sorted_scores = sorted(scores, key=get_score, reverse=True)

# Sort students by score from highest to lowest.
# If two students have the same score, sort their names alphabetically.
# -record[1] puts higher scores first, and record[0] sorts names A-Z.

sorted_scores = sorted(scores, key=lambda record: (-record[1], record[0]))

print("Original scores:", scores)
print("Sorted scores:", sorted_scores)



# Program 2
# Advanced Method

scores = [("Riya", 85),("Aman", 90),("Neha", 90),("Kabir", 72)]

# Sort students by score from highest to lowest.
# If two students have the same score, sort their names alphabetically.
# -record[1] puts higher scores first, and record[0] sorts names A-Z.

sorted_scores = sorted(scores, key=lambda record: (-record[1], record[0]))

#key=: We are about to provide a new rule for how to sort.
#lambda record:: A lambda is just a quick, one-line, nameless function. It does the exact same job
#as def get_score(record):, but it saves you from having to type out a full def block. It basically
#says, "Take one student pair and temporarily call it record."

print("Original scores:", scores)
print("Sorted scores:", sorted_scores)

#-record[1] (The Primary Rule): This takes the score (record[1]) and puts a minus sign in front of it.
#Why? Because Python naturally sorts from smallest to largest. By making a score of 90 into -90, and 85
#into -85, the -90 becomes the "smaller" number mathematically. Python puts -90 before -85. This is a 
#clever math trick to sort highest scores first without needing to type reverse=True.

#record[0] (The Tie-Breaker Rule): If two students have the exact same score (like Aman and Neha both
#having 90), the first rule ends in a tie. Python will then look at this second rule. record[0] is the 
#student's name. Since names are text, Python automatically sorts them in standard A-to-Z alphabetical 
#order.