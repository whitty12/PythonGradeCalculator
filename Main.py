#holds a students information, grade, and rank
class Student:
    rank = 0
    grade = ""

    def __init__(self, student_info):
        self.student_info = student_info

    def setRank(self, rank):
        self.rank =  rank

    def setRank(self,grade):
        self.grade = grade

#Helper method for determine eagernes
def determineEager(student):
    #if not eager, return false
    return 1

#Step 1: Load in the users
def loadUsers(self, filename):
    #1:load file
    file = open(filename,"r")

    for line in file:
        input = file.read(line)

    #2: loop through the array of input
    for i in input:
        student_info = []
        student_info = input[i]

    return students

#Helper method for calculating rank
def calculateRank(self, students):
    total_score = 0



def determineRank(self, students, n):
    rank = Student.rank
    #holds the a students
    a_array = []
    #holds the b students
    b_array = []
    #hodls the c students
    c_array = []
    #holds the d students
    d_array = []
    #holds the f students
    f_array = []

    for i in students:
        rank = calculateRank()
        i.setRank(rank)
    if rank <= (n/3):
        a_array.append(students.pop())
    if rank >= (n/3 + 1) and rank <= 2(n/3):
        b_array.append(students.pop())
    if rank > 2(n/3) and rank < (n/10):
        if determineEager(students.pop() == 1):
            c_array.append()
        else:
            d_array.append()
    else:
        f_array.append()


    #substep: Rank the users in each sub aray according to eagerness

#Step 3: Output the file to the html file output.txt
def outputHTML(self,studentArray):
    for i in studentArray:
        print(studentArray.pop())


#Main method execution
filename = input("Please enter the file name.")
students = loadUsers(filename)
determineRank(students, len(students))
outputHTML()