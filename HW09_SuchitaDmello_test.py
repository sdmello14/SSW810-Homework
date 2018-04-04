"""
    Author : Suchita Dmello
    Test class to test Homework 09
"""
import unittest 
import os
from HW09_SuchitaDmello import Repository,Student,Grade,Instructor

class TestClass(unittest.TestCase):
    def setUp(self):
        os.chdir("C:\Stevens_data_file")
        
    def test_read_student_file(self):
        """
        Test the read student file method
        """
        r = Repository("C:\Stevens_data_file")
        self.assertEquals(10,len(r.students))

    def test_read_instructor_file(self):
        """
        Test the read instructor file method
        """
        r = Repository("C:\Stevens_data_file")
        self.assertEquals(6,len(r.instructors))

    def test_read_grade_file(self):
        """
        Test the read grade file methode
        """
        r = Repository("C:\Stevens_data_file")
        self.assertEquals(23,len(r.grades))

    def test_add_student_grade(self):
        """
        Test the add grades and course to student method
        """
        r = Repository("C:\Stevens_data_file")
        s =r.students.get("10103")
        self.assertEquals(len(s.grade), 4)

    def test_add_number_of_student(self):
        """
        Test the add number of students for the courses taught by instructor
        """
        r = Repository("C:\Stevens_data_file")
        i =r.instructors.get("98765")
        self.assertEquals(len(i.courses), 3)
        self.assertEquals(i.courses.get("SSW 567"), 4)

if __name__ == '__main__':
        unittest.main(exit=False, verbosity=2)