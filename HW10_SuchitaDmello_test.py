"""
    Author : Suchita Dmello
    Test class to test Homework 10
"""
import unittest 
import os
from HW10_SuchitaDmello import Repository,Student,Grade,Instructor,Major

class TestClass(unittest.TestCase):
    os.chdir("C:\Stevens_data_file")
    r = Repository("C:\Stevens_data_file")
    
    def test_read_student_file(self):
        """
        Test the read student file method
        """
        self.assertEquals(10,len(self.__class__.r.students))

    def test_read_instructor_file(self):
        """
        Test the read instructor file method
        """
        self.assertEquals(6,len(self.__class__.r.instructors))

    def test_read_grade_file(self):
        """
        Test the read grade file methode
        """
        self.assertEquals(23,len(self.__class__.r.grades))
    
    def test_read_major_file(self):
        """
        Test the read major file methode
        """
        self.assertEquals(4,len(self.__class__.r.required_course.get("SFEN")))
        self.assertEquals(3,len(self.__class__.r.elective_course.get("SFEN")))


    def test_add_student_grade(self):
        """
        Test the add grades and course to student method
        """
        s =self.__class__.r.students.get("10103")
        self.assertEquals(len(s.grade), 4)

    def test_add_number_of_student(self):
        """
        Test the add number of students for the courses taught by instructor
        """
        i =self.__class__.r.instructors.get("98765")
        self.assertEquals(len(i.courses), 3)
        self.assertEquals(i.courses.get("SSW 567"), 4)
    
    def test_add_student_remaining_course(self):
        """
        Test the remaining course of student
        """
        student =self.__class__.r.students.get("10103")
        self.assertEquals(len(student.remaining_required), 2)
        self.assertEquals(len(student.remaining_elective), 0)

if __name__ == '__main__':
        unittest.main(exit=False, verbosity=2)