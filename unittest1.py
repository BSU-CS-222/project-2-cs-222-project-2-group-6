import unittest
from main import fetchcourses

class TestCourses(unittest.TestCase):
    
    def test_search_course(self):
        courses = [
            ['CS416', '001', 'TR', '0900', '1015'],
            
        ]

        result = search_courses(courses)
        expected = [
            {'Course': 'CS416', 'Section': '001', 'Days': 'TR', 'Start Time': '0900', 'End Time': '1030'}
        ]
        self.assertEqual(result, expected)
    
    def test_course_not_exist(self):
        courses = [
            ['CS4534', '001', 'TR', '0900', '1015'],
            
        ]

        result = search_courses(courses)
        
        expected = "Invalid course, try again"
        self.assertEqual(result, expected)
    
    def test_overlap(self):
        new_course = {'Days': 'MWF', 'Start Time': '0900', 'End Time': '0950'}
        registered_courses = [
            {'Days': 'TR', 'Start Time': '1000', 'End Time': '1115'},
            {'Days': 'MWF', 'Start Time': '1100', 'End Time': '1150'}
        ]
        result = check_course_overlapping(new_course, registered_courses)
        self.assertFalse(result)
    
    def test_class_limit(self):
        creditlimit = 21
        
        self.assertNotEqual(creditlimit, studenthours)
            
    
    
    def test_show_courses(self):
        expected = [
    ['CS120', '001', 'MWF', '0900', '0950'],
    ['CS120', '003', 'TR', '0930', '1045'],
    ['CS121', '001', 'TR', '1230', '1345'],
    ['CS120', '002', 'MWF', '1300', '1350'],
    ['CS222', '005', 'TR', '1100', '1215'],
    ['CS416', '001', 'TR', '0900', '1015']
]
        self.assertEqual(expected, fetchcourses())


if __name__ == "__main__":
    unittest.main()