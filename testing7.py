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
            
    def compare_times_in_dict(self):

        for i in range(len(self.schedule)):
            reference_start_time, reference_end_time = self.schedule[i].split(" ")[3].split('-')


            for j in range(i+1, len(self.schedule)):
                start_time, end_time = self.schedule[j].split(" ")[3].split('-')
                

                if start_time <= reference_end_time and end_time >= reference_start_time:
                    print("Can't create schedule. ")
                    return True

        return False

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

        time_conflict = self.compare_times_in_dict()

        if time_conflict == False:
            print("\nSchedule Successfully Created!")
            print("\nYour Schedule:")
            for course_info in self.schedule:
                print(course_info)
       

student_instance = Student()
student_instance.main()