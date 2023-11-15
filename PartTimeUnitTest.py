import unittest
from PartTimeClass import PartTimeCourseScheduler
class TestPartTimeCourseScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = PartTimeCourseScheduler('test_courses.txt')

    def test_set_availability(self):
        self.scheduler.set_availability(['MWF', '0900', '1200'])
        self.assertEqual(self.scheduler.get_availability(), ['MWF', '0900', '1200'])

    def test_display_classes_within_availability(self):
        self.scheduler.set_availability(['MWF', '0900', '1200'])
        available_courses = self.scheduler.display_available_courses()
    

    def test_register_reduced_course_load(self):
        self.scheduler.set_availability(['MWF', '0900', '1200'])
        self.scheduler.set_max_courses(2)
        self.scheduler.select_course('CS120 001')
        self.scheduler.select_course('CS121 001')
        self.assertEqual(len(self.scheduler.get_selected_courses()), 2)

    def test_schedule_within_constraints(self):
        self.scheduler.set_availability(['MWF', '0900', '1200'])
        self.scheduler.set_max_courses(2) 
        self.scheduler.select_course('CS120 001')
        schedule = self.scheduler.get_schedule()
        self.assertIn('CS120 001', schedule)
       
    def test_flexibility_in_course_selection(self):
        self.scheduler.set_availability(['MWF', '0900', '1200'])
        self.scheduler.select_course('CS120 001')
        self.scheduler.adjust_courses(['CS121 001'])
        self.assertNotIn('CS120 001', self.scheduler.get_selected_courses())
        

if __name__ == '__main__':
    unittest.main()