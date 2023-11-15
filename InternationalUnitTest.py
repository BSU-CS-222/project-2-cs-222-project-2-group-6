import unittest
from internationalScheduler import InternationalStudentScheduler
class TestInternationalStudentScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = InternationalStudentScheduler('test_courses.txt')

    def test_differentiate_course_types(self):
        courses = self.scheduler.get_courses()
        for course_id, course_info in courses.items():
            self.assertIn('type', course_info)  

    def test_limit_one_online_class(self):
        self.scheduler.select_course('OnlineCourse1')  
        self.scheduler.select_course('OnlineCourse2')  
        online_courses = self.scheduler.get_selected_online_courses()
        self.assertEqual(len(online_courses), 1)  # Should only have 1 online course

    def test_prevent_further_online_enrollment(self):
        self.scheduler.select_course('OnlineCourse1')
        selection_result = self.scheduler.select_course('OnlineCourse2')
        self.assertFalse(selection_result)  # The second online course selection should fail

    def test_confirm_final_schedule(self):
        self.scheduler.select_course('OnlineCourse1')  
        self.scheduler.select_course('InPersonCourse1') 
        final_schedule = self.scheduler.get_final_schedule()

        online_courses = [course_id for course_id in final_schedule if final_schedule[course_id]['type'] == 'online']
        self.assertEqual(len(online_courses), 1)  # Should only have 1 online course
    
if __name__ == '__main__':
    unittest.main()