class PartTimeCourseScheduler:
    def __init__(self, course_file):
        self.course_file = course_file
        self.courses = self.read_course_data()
        self.availability = []
        self.selected_courses = []
        self.max_courses = 0 

    def read_course_data(self):
        
        return {
            'CS120 001': {'days': 'MWF', 'start_time': '0900', 'end_time': '0950'},
            'CS120 002': {'days': 'TR', 'start_time': '1100', 'end_time': '1215'},
            'CS121 001': {'days': 'MWF', 'start_time': '1000', 'end_time': '1050'},
            'CS121 002': {'days': 'TR', 'start_time': '1330', 'end_time': '1445'},
            'CS222 001': {'days': 'MWF', 'start_time': '1300', 'end_time': '1350'},
            'CS222 002': {'days': 'TR', 'start_time': '0930', 'end_time': '1045'},

        }

    def set_availability(self, availability):
        self.availability = availability

    def get_availability(self):
        return self.availability

    def display_available_courses(self):
        # Mock implementation - replace with actual availability check
        return self.courses

    def select_course(self, course_id):
        if course_id in self.courses:
            self.selected_courses.append(course_id)
            return True
        return False
    def set_max_courses(self, max_courses):
        self.max_courses = max_courses

    def select_course(self, course_id):
        if len(self.selected_courses) < self.max_courses and course_id in self.courses:
            self.selected_courses.append(course_id)
            return True
        return False

    def get_selected_courses(self):
        return self.selected_courses

    def get_schedule(self):
        # Mock implementation - replace with actual scheduling logic
        return {course_id: self.courses[course_id] for course_id in self.selected_courses}

    def adjust_courses(self, new_courses):
        self.selected_courses = new_courses