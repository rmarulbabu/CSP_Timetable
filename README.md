# Constraint Satisfaction Problem – Timetable Scheduling

## Aim

To develop a Constraint Satisfaction Problem (CSP) solution for assigning subjects to available time slots using backtracking.

## Problem Statement

Assign a time slot to each subject while satisfying the given constraints.

## Subjects

* Maths
* Python
* DBMS
* AI

## Time Slots

* 9:00 AM
* 11:00 AM
* 2:00 PM

## CSP Structure

| CSP Component | Description                                                                         |
| ------------- | ----------------------------------------------------------------------------------- |
| Variables     | Maths, Python, DBMS, AI                                                             |
| Domains       | 9:00 AM, 11:00 AM, 2:00 PM                                                          |
| Constraints   | Maths and Python cannot be at the same time; DBMS and AI cannot be at the same time |
| Search        | Backtracking                                                                        |

## Constraints

1. Each subject must be assigned exactly one time slot.
2. Maths and Python must not have the same time slot.
3. DBMS and AI must not have the same time slot.
4. All subjects must be assigned a valid time slot.

## Algorithm

1. Select a subject.
2. Try each available time slot.
3. Check whether the selected slot satisfies all constraints.
4. If valid, assign the slot to the subject.
5. Continue with the next subject.
6. If no valid slot is available, go back to the previous subject and try another slot.
7. Continue until all subjects are assigned.

## Program

The program is implemented in Python using a dictionary to store the timetable and a recursive backtracking method to find a valid solution.

## Output

```text
Final Timetable
Maths -> 9:00 AM
Python -> 11:00 AM
DBMS -> 9:00 AM
AI -> 11:00 AM
```

## Constraint Verification

* Maths → 9:00 AM
* Python → 11:00 AM

Maths and Python have different time slots, so the first constraint is satisfied.

* DBMS → 9:00 AM
* AI → 11:00 AM

DBMS and AI have different time slots, so the second constraint is satisfied.

Each subject has exactly one time slot, so all the given constraints are satisfied.

## Result

Thus, the timetable was successfully generated using the **Constraint Satisfaction Problem (CSP)** technique with **backtracking**.
