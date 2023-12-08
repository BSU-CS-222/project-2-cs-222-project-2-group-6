import unittest
from testing2 import Student

class TestCourses(unittest.TestCase):

   def test_show_courses(self):
        student_instance = Student("12345")
        actual = student_instance.read_courses_from_file("classes.txt")
        expected = ['007', 'MWF', '1100', '1345']

        actual_first_line = actual[next(iter(actual))][0]

        self.assertEqual(expected, actual_first_line)


if __name__ == "__main__":
    unittest.main()