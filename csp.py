subjects = ["Maths", "Python", "DBMS", "AI"]
slots = ["9:00 AM", "11:00 AM", "2:00 PM"]

constraints = {
    "Maths": ["Python"],
    "Python": ["Maths"],
    "DBMS": ["AI"],
    "AI": ["DBMS"]
}

timetable = {}

def is_valid(subject, slot):
    for other in constraints[subject]:
        if timetable.get(other) == slot:
            return False
    return True

def backtrack(index):
    if index == len(subjects):
        return True

    subject = subjects[index]

    for slot in slots:
        if is_valid(subject, slot):
            timetable[subject] = slot

            if backtrack(index + 1):
                return True

            del timetable[subject]

    return False

if backtrack(0):
    print("Final Timetable")
    print("----------------")
    for subject in subjects:
        print(subject, "->", timetable[subject])
else:
    print("No solution found")