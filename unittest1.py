import unittest
'''from main import fetchcourses'''

class TestCourses(unittest.TestCase):
    def seUp(self):
        self.scheduler = Courses()
    
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
            
    
    #Student who need special assistance
    #The student need a gap time between each of the class
    #This is testing about student can view clearly the detail of the course times
    def test_show_courses(self):
        expected = [
    ['CS120', '001', 'MWF', '0900', '0950'],
    ['CS120', '003', 'TR', '0930', '1045'],
    ['CS121', '001', 'TR', '1230', '1345'],
    ['CS120', '002', 'MWF', '1300', '1350'],
    ['CS222', '005', 'TR', '1100', '1215'],
    ['CS416', '001', 'TR', '0900', '1015'],
    ['MATH181','001','TR','1400','1459'],
    ['CS418','001','MWF','1200','1250'],
    ['CS239','001','TR','0900','0950']
]
        self.assertEqual(expected, fetchcourses())

    def test_add_course_sucess(self):
        result = self.scheduler.add_course("CS120", "002", "MWF", 1300, 1350, 3)
        self.assertEqual(result, "Sucessfuly added.")

    def test_conflict_adding_course(self):
        self.scheduler.adding_course("CSS222", "005", "TR", 1100, 1215, 3)
        result = self.scheduler.adding_course("CSS222", "005", "TR", 1100, 1215, 3)
        self.assertEqual(result, "Oh there is schedule conflict. You will need to add different course.")

     #testing for full time student wih live in campus and willing to take 15 credits   
    def test_fulltimestudent_in_campus(self):
        course= [
            "CS120, 001, MWF, 0900, 0950, 3",
            "CS121, 001, TR, 1230, 1345, 3",
            "MATH181, 001, TR, 1400, 1450, 3",
            "CS418, 001, MWF, 1200, 1250, 3",
            "CS239, 001, TR, 0900, 0950, 3"
        ]

        
        # Add courses to the scheduler using list comprehension
        [self.scheduler.add_course(course_info) for course_info in course]

        # Get the list of courses and check if they are added correctly
        courses = self.scheduler.get_courses()
        expected_courses = [
            "CS120, 001, MWF, 0900, 0950, 3",
            "CS121, 001, TR, 1230, 1345, 3",
            "MATH181, 001, TR, 1400, 1450, 3",
            "CS418, 001, MWF, 1200, 1250, 3",
            "CS239, 001, TR, 0900, 0950, 3"
        ]

        self.assertEqual(courses, expected_courses, "Courses are not added correctly")

    #Not to get overlapping course time people who commute to campus and taking classes
    #The student only can go Tuesday and Thursday
    #Testing for the student who only can go TR, not to get overlapping course time
    def test_overlapping_course_time(self):

        #Input data
        overlapping_courses = [
            "CS120,003,TR,0930,1045, 3",
            "CS239,001,TR,0900,0950, 3",  # Overlaps with the first course
        ]

        # Add overlapping courses to the scheduler
        [self.scheduler.add_course(course_info) for course_info in overlapping_courses]

        # Check if the scheduler detects overlapping times
        has_overlap = self.scheduler.has_time_overlap()

        self.assertTrue(has_overlap, "Scheduler did not detect time overlap")

if __name__ == "__main__":
    unittest.main()