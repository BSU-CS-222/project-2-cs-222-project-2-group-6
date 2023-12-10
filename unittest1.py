import unittest
from Project2Recursion import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student() 

    def test_read_courses_from_file(self):
        # Test if read_courses_from_file method properly reads the file and populates the courses_dict
        self.student.read_courses_from_file("classes.txt")
        self.assertEqual(len(self.student.courses_dict), 5)  
    def test_time_conflict(self):
        # Test for time conflict when there's no conflict
        self.student.schedule = [("Section1", "Mon", "10-12")]
        course_info = ("Section2", "Tue", "13-15")
        self.assertFalse(self.student.time_conflict(self.student.schedule[0], course_info))

        # Test for time conflict when there's a conflict
        self.student.schedule = [("Section1", "Mon", "10-12")]
        course_info = ("Section1", "Mon", "11-13")
        self.assertTrue(self.student.time_conflict(self.student.schedule[0], course_info))

    def test_add_courses(self):
        # Test adding multiple courses without conflicts
        self.student.courses_dict = {
            "CS101": [("Section1", "Mon", "10-12")],
            "CS102": [("Section2", "Tue", "13-15")],
            "CS103": [("Section3", "Wed", "09-11")]
        }
        courses_to_add = ["CS101", "CS102", "CS103"]
        result = self.student.add_courses(courses_to_add)
        self.assertIsNone(result)
        self.assertEqual(len(self.student.schedule), 3)

   

if __name__ == '__main__':
    unittest.main()
