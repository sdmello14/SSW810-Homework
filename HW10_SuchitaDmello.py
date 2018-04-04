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
        Dictionary to hold the all required course for the major
        Key is the major and value is the list of required course for that key
        """
        self.required_course = defaultdict(list)
        """
        Dictionary to hold the all elective course for the major
        Key is the major and value is the list of elective course for that key
        """
        self.elective_course = defaultdict(list)

        """
        Steps to read student, instructor and grade file and print the summary
        """
        self.read_student_file()
        self.read_instructor_file()
        self.read_grade_file()
        self.read_major_file()
        self.add_student_grade()
        self.add_number_of_student()
        self.add_student_remaining_course()
        print("Repository for",dir_path)
        self.print_major_summary()
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
    
    def read_major_file(self):
        """
        Read the major file line by line and create the required_course and elective_course dictionary
        """
        try:
            file_line=open("majors.txt",'r')
        except FileNotFoundError:
            print("Cannot open the file")
        else: 
            for line in file_line:
                data = line.strip().split("\t")
                major = Major(data[0],data[1],data[2])
                if major.flag == 'R':
                    self.required_course[major.major].append(major.course)
                elif major.flag == 'E':
                    self.elective_course[major.major].append(major.course)


    def add_student_grade(self):
        """
        Add the details of course complete with grade to each student from grade file
        """
        for grade in self.grades:
            student = self.students.get(grade.cwid_student)
            dd = student.grade
            if grade.grade:
                dd[grade.course_name] = grade.grade
    
    def add_student_remaining_course(self):
        """
        Add the details of remaining course of student
        """
        for student_cwid,student in self.students.items():
            major =student.major
            completed_course =set([k for k,grade in student.grade.items() if grade in ['A', 'A-', 'B+', 'B', 'B-', 'C+','C']])
            student.remaining_required = set(self.required_course.get(major)).difference(completed_course)
            if not set(self.elective_course.get(major)).intersection(completed_course):
                student.remaining_elective = self.elective_course.get(major)

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
        student_table.field_names = ["CWID", "Name","Major","Completed Courses","Remaining Required","Remaining Elective"]
        for cwid,student in self.students.items():
            remaining_elective = "None"
            if len(student.remaining_elective) is not 0:
                remaining_elective=student.remaining_elective
            student_table.add_row([cwid,student.name,student.major,[k for k,grade in student.grade.items() if grade in ['A', 'A-', 'B+', 'B', 'B-', 'C+','C'] ],list(student.remaining_required),remaining_elective])
        print("Student Summary")
        print(student_table)
    
    def print_major_summary(self):
        """
        Method to show the major details or required adn elective course in pretty table
        """
        major_table = PrettyTable()
        major_table.field_names = ["Dept", "Required","Electives"]
        for major,courses in self.required_course.items():
            major_table.add_row([major,courses,self.elective_course.get(major)])
        print("Majors Summary")
        print(major_table)


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

        self.remaining_required = list()
        self.remaining_elective = list()
    
class Major:
    """
    Major class to hold details of required and elective course for each major
    """  
    def __init__(self,major,flag,course):
        self.major = major
        self.flag =flag
        self.course = course
       

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
