class InternationalStudentScheduler:
    def __init__(self, course_file):
        self.course_file = course_file
        self.courses = self.read_course_data()
        self.selected_courses = []

    def read_course_data(self):
        
        return {
            'OnlineCourse1': {'type': 'online', 'days': 'TBD', 'time': 'TBD'},
            'OnlineCourse2': {'type': 'online', 'days': 'TBD', 'time': 'TBD'},
            'InPersonCourse1': {'type': 'in-person', 'days': 'MWF', 'time': '0900-0950'},
            'InPersonCourse2': {'type': 'in-person', 'days': 'TR', 'time': '1100-1215'},
          
        }

    def get_courses(self):
        return self.courses

    def select_course(self, course_id):
      if course_id in self.courses:
        course_type = self.courses[course_id]['type']
        if course_type == 'online' and self.has_online_course():
            return False  # Prevent adding more than one online course
        self.selected_courses.append(course_id)
        return True
      return False

    def has_online_course(self):
        return any(self.courses[course]['type'] == 'online' for course in self.selected_courses)

    def get_selected_online_courses(self):
        return [course for course in self.selected_courses if self.courses[course]['type'] == 'online']

    def get_final_schedule(self):
        return {course: self.courses[course] for course in self.selected_courses}