"""
Question:1 

Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . 
Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

Example
All permutations of  are:
.
Print an array of the elements that do not sum to .

Input Format

Four integers  and , each on a separate line.

Constraints

Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
Explanation 0

Each variable  and  will have values of  or . All permutations of lists in the form .
Remove all arrays that sum to  to leave only the valid permutations.

Sample Input 1

2
2
2
2
Sample Output 1

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2],[1, 1, 1], 
[1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
"""

#NOTE -  List Comprehension => List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
def List_Comprehension ():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ab=[]
    o=[]
    for x in range(x+1):
        for y in range (y+1):
            for z in range (z+1):
                if x+y+z!=n:
                    ab=[x,y,z]
                    o.append(ab)
    print(o)
# List_Comprehension()

"""Question 2.

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
"""
def participants_score():
    # n = int(input())
    arr = map(int, input().split())
    a = list(arr)
    b = []
    for i in range(len(a)):
        if max(a) == a[i]:
            b.append(a[i])

    c = set(a) - set(b)
    print(max(c))
    
#========================================================================================================================================================
"""Question 3.
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: .
Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""
def students_short():
    # Initialize an empty list to store the details of each student
    students_details = []

    # Get the number of students in the class
    n = int(input())

    # Initialize an empty list to store the grades of each student
    grades = []

    # Loop through each student
    for index in range(n):
        # Get the name of the student
        name = input()

        # Get the grade of the student
        grade = float(input())

        # Add the name and grade of the student to the list of students' details
        students_details.append([name, grade])

        # Add the grade of the student to the list of grades
        grades.append(grade)

    # Sort the list of students' details based on their grades
    students_details.sort(key=lambda x: x[1])

    # Remove the minimum grade from the list of grades
    grades.remove(min(grades))

    # Find the second minimum grade
    second_min_grade = min(grades)

    # Loop through the sorted list of students' details
    for student in students_details:
        # If the grade of the student is equal to the second minimum grade
        if student[1] == second_min_grade:
            # Print the name of the student
            print(student[0])









