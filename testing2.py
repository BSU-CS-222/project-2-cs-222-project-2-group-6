class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.schedule = []
        self.courses_dict = {}

    def add_course(self, course_code):
       
        if course_code in self.courses_dict:
            available_classes = self.courses_dict[course_code]
            selected_section = available_classes[0]

            section, days, start_time, end_time = map(str.strip, selected_section)
            formatted_course_info = f"{course_code}: {section}, {days}, {start_time}-{end_time}"

            if self.is_safe(formatted_course_info):
                self.schedule.append(formatted_course_info)
                
    def read_courses_from_file(self, file_path):
        with open(file_path, 'r') as file:
            self.courses_dict = {}
            for line in file:
                course_data = line.strip().split()
                course_code = course_data[0]
                course_details = course_data[1:]
                if course_code not in self.courses_dict:
                    self.courses_dict[course_code] = []
                self.courses_dict[course_code].append(course_details)
        return self.courses_dict
    
    def is_safe(self):
       
        for course_code, course_details_list in self.courses_dict.items():
                print(self.courses_dict[2])
                #existing_info_split = selected_section

                #days_existing, existing_start_time, existing_end_time, _ = existing_info_split

            # Check for day overlap
                #if days_existing != days_new:
                   # continue

            # Check for time conflict
                #if int(existing_end_time) > int(start_time_new) and int(existing_start_time) < int(end_time_new):
                   # return False

       # return True

    def view_available_courses(self):
        available_courses_str = "Available Courses:\n"
        for course_code, course_details_list in self.courses_dict.items():
            for i in course_details_list:
                if course_code not in available_courses_str:
                    available_courses_str += f"{course_code} \n"
        return available_courses_str

    def main(self):
        coursesfile = self.read_courses_from_file("classes.txt")
        print(self.view_available_courses())
        num_courses = int(input("Enter the number of courses you'd like to register for: "))
        for i in range(num_courses):
            course_code = input("Enter the course code: ")
            if course_code in coursesfile:
                self.add_course(course_code)  
            else:
                print("Course not found")
                
          
        print("\nSchedule Successfuly Created!")
        print("\nYour Schedule:")
        for course_info in self.schedule:
            print(course_info)


student_instance = Student("12345")
student_instance.is_safe()
student_instance.main()