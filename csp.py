subjects=["Maths","Python","DBMS","AI"]
slots=["9:00 AM","11:00 AM","2:00 PM"]
constraints=[("Maths","Python"),("DBMS","AI")]
timetable={}
def valid(subject,slot):
    for a,b in constraints:
        if subject==a:
            other=b
        elif subject==b:
            other=a
        else:
            continue
        if timetable.get(other)==slot:
            return False
    return True
def solve(i):
    if i==len(subjects):
        return True
    subject=subjects[i]
    for slot in slots:
        if valid(subject,slot):
            timetable[subject]=slot
            if solve(i+1):
                return True
            del timetable[subject]
    return False
if solve(0):
    print("Final Timetable")
    for subject in subjects:
        print(subject,"->",timetable[subject])
else:
    print("No solution found")