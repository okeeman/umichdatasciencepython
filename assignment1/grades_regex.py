import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()

    # YOUR CODE HERE
    return re.findall(r'([A-Z][a-z]*\s[A-Z][a-z]*)(?=: B)', grades)