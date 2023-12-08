class Student:
    def __init__(self):
        self.schedule = []
        self.courses_dict = {}

    def add_course(self, course_code):
        if course_code in self.courses_dict:
            available_classes = self.courses_dict[course_code]

            for selected_section in available_classes:
                section, days, start_time, end_time = map(str.strip, selected_section)
                formatted_course_info = f"{course_code}: {section}, {days}, {start_time}-{end_time}"

                if not self.has_time_conflict(formatted_course_info):
                    self.schedule.append(formatted_course_info)
                    break  # Break the loop if a non-conflicting section is found
            else:
                print("Schedule can't be made.")
                exit()

        else:
            print(f"Course code {course_code} not found in available courses.")

    def has_time_conflict(self, new_course_details):
        
        new_days, new_time_range = new_course_details.split(" ")[2], new_course_details.split(" ")[3].split("-")
        new_start, new_end = map(int, new_time_range)

        for existing_course in self.schedule:
            existing_days, existing_time_range = existing_course.split(" ")[2], existing_course.split(" ")[3].split("-")
            existing_start, existing_end = map(int, existing_time_range)

            # Check if the days are different
            if new_days != existing_days:
                continue

            # Check for overlapping time ranges
            if new_start < existing_end and existing_start < new_end:
                return True 

        return False  

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

    def main(self):
        coursesfile = self.read_courses_from_file("classes.txt")
        print(self.view_available_courses())
        time_conflict = None  

        num_courses = int(input("Enter the number of courses you'd like to register for: "))
        for i in range(num_courses):
            course_code = input("Enter the course code: ")
            if course_code in coursesfile:
                self.add_course(course_code)
                if time_conflict == "Schedule can't be made.":
                    break
            else:
                print("Course not found")
                        
        if time_conflict != "Schedule can't be made.":
            print("\nYour Schedule:")
            if self.schedule:
                for course_info in self.schedule:
                    print(course_info)
            else:
                print("Your schedule is empty.")

student_instance = Student()
student_instance.main()
