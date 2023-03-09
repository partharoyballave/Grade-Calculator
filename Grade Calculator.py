#   Dec 17, 2022              Grade Calculator                     Roy Ballave, Partha
#
# This program receives percentage marks and their respective subjects then calculates
# the average and median mark alongside a corresponding letter grade based on the canadian
# grading system.
#

# Finds letter grades from percentage grades
def find_letter_grade(mark):
    if mark > 100 or mark < 0:
        return "E"
    if mark >= 80:
        letter_Grade = "A"
    elif mark >= 70:
        letter_Grade  = "B"
    elif mark >= 60:
        letter_Grade = "C"
    elif mark >= 50:
        letter_Grade = "D"
    elif mark <= 49:
        letter_Grade = "F"
    return letter_Grade

# Recieves the total amount of marks wanted to process and sets different lists/variables
mark_Total = int(input("Please enter the total amount of marks you want to find the average for: "))
letter_Grade = "E"
marks_In_List = [     ]
subjects_List = [     ]
sum = 0
mark_Count = 0

# Receives subject and grades containing an Error Check for too high or too low percentage
marks_Enter_Not_Complete = True
while marks_Enter_Not_Complete:
    subjects = input(f"Please enter subject {mark_Count+1}: ")
    mark = float(input(f"Please enter your mark for {subjects} (%): "))
    if mark > 100 or mark < 0:
        print("Error! Please try again.")
    else:
        marks_In_List.append(mark)
        subjects_List.append(subjects)
        mark_Count += 1

    if mark_Count == mark_Total:
        marks_Enter_Not_Complete = False


# Loop that outputs letter grade for marks inputted
for m in marks_In_List:
    letter_Grade = find_letter_grade(m)
    idx = marks_In_List.index(m)
    print(f"\nFor {subjects_List[idx]}, your grade of {m}% is a {letter_Grade}")
    sum = sum + m

# Finds and outputs average mark with corresponding letter grade
average = sum // mark_Count
letter_Grade = find_letter_grade(average)
print(f"\nThe average of the grades you inputted is {average}%, or a {letter_Grade}.")

# Finds highest mark inputted and displays data inputted with letter mark
highest_Mark = -999
for m in marks_In_List:
    if m > highest_Mark:
        highest_Mark = m
        idx_Highest = marks_In_List.index(m)

print(f"\nYour highest mark is in the subject of {subjects_List[idx_Highest]}"
      f" which is a {highest_Mark}%, or a {find_letter_grade(highest_Mark)}.")

#Finds the median mark
marks_Sorted = sorted(marks_In_List)
if len(marks_Sorted) % 2 != 0:
    median_Idx = int((len(marks_Sorted)+1)/2-1)
    median_Mark = marks_Sorted[median_Idx]
else:
    median_Idx1 = int(len(marks_Sorted)/2-1)
    median_Idx2 = int(len(marks_Sorted)/2)
    median_Mark = (marks_Sorted[median_Idx1] + marks_Sorted[median_Idx2])/2

print(f"The median of the marks you inputted is {median_Mark}%, or a {find_letter_grade(median_Mark)}. ")