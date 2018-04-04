"""
Author : Suchita Dmello
Program to Create a repository of given college
"""
import os
from prettytable import PrettyTable
from collections import defaultdict

class Repository:
    """
        Repository class to hold the list of students, instructors and grades
    """ 

    def __init__(self,dir_path):
        """
        dictioary to store student cwid as key and the student instance as value
        """
        self.students = dict()
        

        """
        dictioary to store instructor cwid as key and the instructor instance as value
        """
        self.instructors = dict()

        """
        list to store all the instance of Grade
        """
        self.grades = list()

        """
        Steps to read student, instructor and grade file and print the summary
        """
        self.read_student_file()
        self.read_instructor_file()
        self.read_grade_file()
        self.add_student_grade()
        self.add_number_of_student()
        print("Repository for",dir_path)
        self.print_student_summary()
        self.print_instructor_summary()

    def add_student(self,student):
        self.students[student.cwid] = student

    def add_instructor(self,instructor):
        self.instructors[instructor.cwid] = instructor
    
    def add_grade(self,Grade):
        self.grades.append(Grade)

    def read_student_file(self):
        """
        Read the student file line by line and create student object for each line
        add the student object in student list in repository class
        """
        try:
            file_line=open("students.txt",'r')
        except FileNotFoundError:
            print("Cannot open the file")
        else:
            for line in file_line:
                data = line.strip().split("\t")
                student = Student(data[0],data[1],data[2])
                self.add_student(student)

    def read_instructor_file(self):
        """
        Read the instructor file line by line and create instructor object for each line
        add the instructor object in instructor list in repository class
        """
        try:
            file_line=open("instructors.txt",'r')
        except FileNotFoundError:
            print("Cannot open the file")
        else:
            for line in file_line:
                data = line.strip().split("\t")
                instructor = Instructor(data[0],data[1],data[2])
                self.add_instructor(instructor)

    def read_grade_file(self):
        """
        Read the grade file line by line and create grade object for each line
        add the grade object in grade list in repository class
        """
        try:
            file_line=open("grades.txt",'r')
        except FileNotFoundError:
            print("Cannot open the file")
        else:
            for line in file_line:
                data = line.strip().split("\t")
                grade = Grade(data[0],data[1],data[2],data[3])
                self.add_grade(grade)

    def add_student_grade(self):
        """
        Add the details of course complete with grade to each student from grade file
        """
        for grade in self.grades:
            student = self.students.get(grade.cwid_student)
            dd = student.grade
            if grade.grade:
                dd[grade.course_name] = grade.grade

    def add_number_of_student(self):
        """
        Add the courses taught with number of students in each course taught
        """
        for grade in self.grades:
            instructor = self.instructors.get(grade.cwid_instructor)
            dd = instructor.courses
            dd[grade.course_name] = dd.get(grade.course_name,0)+1

    def print_student_summary(self):
        """
        Method to show the students detail in pretty table
        """
        student_table = PrettyTable()
        student_table.field_names = ["CWID", "Name","Completed Courses"]
        for cwid,student in self.students.items():
            student_table.add_row([cwid,student.name,list(student.grade.keys())])
        print("Student Summary")
        print(student_table)

    def print_instructor_summary(self):
        """
        Method to show the instructor detail in pretty table
        """
        instructor_table = PrettyTable()
        instructor_table.field_names = ["CWID", "Name","Dept","Course","Students"]
        for cwid,instructor in self.instructors.items():
            for key,value in instructor.courses.items():
                instructor_table.add_row([cwid,instructor.name,instructor.department,key,value])
        print("Instructor Summary")
        print(instructor_table)


class Student:
    """
    Student class to hold details of students
    """  
    def __init__(self,cwid,name,major):
        self.cwid = cwid
        self.name = name
        self.major = major
        """
        Dictionary to hold the each course nane completed by student as key 
        and the grade associated with that course as value
        """
        self.grade = dict()
    
    
class Instructor:
    """
    Instructor class to hold details of instructor
    """ 
    def __init__(self,cwid,name,department):
        self.cwid = cwid
        self.name = name
        self.department = department
        self.courses = defaultdict(int)
  
class Grade:
    """
    Grade class to hold details of grades
    """ 
    def __init__(self,cwid_student,course_name,grade,cwid_instructor):
        self.cwid_student = cwid_student
        self.course_name = course_name
        self.grade = grade
        self.cwid_instructor = cwid_instructor

def main():
    try:
        number_of_repository = int(input("Enter the number of repository you want to create:"))
    except:
        print("Please enter valid number")
        exit()
    dir_paths = list()
    for i in range(number_of_repository):
        dir_paths.append(input("Enter directory path of data files for repository {}: ".format(i+1)))
    for dir_path in dir_paths:
        try:
            os.chdir(dir_path)
        except (TypeError,FileNotFoundError):
            print("Invalid directory path")
        else:
            r = Repository(dir_path)
            
        
if __name__ == "__main__":
    main()              
