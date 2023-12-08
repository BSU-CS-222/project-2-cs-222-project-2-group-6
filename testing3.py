class Student:
    def __init__(self):
        self.schedule = []
        self.courses_dict = {}

    def add_course(self, course_code):
        if course_code in self.courses_dict:
            available_classes = self.courses_dict[course_code]
            selected_section = available_classes[0]

            section, days, start_time, end_time = map(str.strip, selected_section)
            formatted_course_info = f"{course_code}: {section}, {days}, {start_time}-{end_time}"

            
            self.schedule.append(formatted_course_info)


    def read_courses_from_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                elements = line.strip().split()
                course_code = elements[0]
                course_section = elements[1]
                course_days = elements[2]
                course_start = elements[3]
                course_end = elements[4]
                if course_code not in self.courses_dict:
                    self.courses_dict[course_code] = []
                self.courses_dict[course_code].append((course_section, course_days, course_start, course_end))

        return self.courses_dict

    def view_available_courses(self):
        available_courses_str = "Available Courses:\n"
        for course_code, course_details_list in self.courses_dict.items():
            for i in course_details_list:
                if course_code not in available_courses_str:
                    available_courses_str += f"{course_code} \n"
        return available_courses_str
    
    def check_schedule_conflict(self):
        has_conflict = False  # Variable to track if any conflicts are found

        for course_details_list in self.courses_dict.values():
            for course_details in course_details_list:
                if "MWF" in course_details[1]:
                    if not has_conflict:  
                        print("Schedule conflict: Days are the same for multiple courses.")
                        has_conflict = True
                    break  
                if not has_conflict: #needs fixed
                    print("No schedule conflict.")
                    
        

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


        conflict = self.check_schedule_conflict()
        
        if conflict:       
            print("\nSchedule Successfully Created!")
            print("\nYour Schedule:")
            for course_info in self.schedule:
                print(course_info)

student_instance = Student()
student_instance.main()