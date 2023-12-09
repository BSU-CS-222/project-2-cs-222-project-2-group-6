class Student:
    def __init__(self):
        self.schedule = []
        self.courses_dict = {}

    def add_course(self, course_code):
        
        if course_code in self.courses_dict:
            available_classes = self.courses_dict[course_code]

            for chosen in available_classes:
                section, days, time_range = chosen
                start_time, end_time = time_range.split('-') #time is hyphenated to begin with
                formatted_course_info = f"{course_code}: {section}, {days}, {start_time}-{end_time}"

                if not self.time_conflict(formatted_course_info):
                    self.schedule.append(formatted_course_info)
                    break  #break the loop if a non-conflicting course is found
            else:
                return "Schedule can't be made."
        

    def time_conflict(self, course_details):
        
        days, time_range = course_details.split(" ")[2], course_details.split(" ")[3].split("-")
        start_time_conflict, end_time_conflict = int(time_range[0]), int(time_range[1]) #splits course details into separate indexes

        for schedule_courses in self.schedule: #these also convert all the strings of times to ints for comparison
            schedule_days, schedule_time_range = schedule_courses.split(" ")[2], schedule_courses.split(" ")[3].split("-")
            schedule_start, schedule_end = int(schedule_time_range[0]), int(schedule_time_range[1])

            #checks if the days are different
            if days != schedule_days:
                continue

            #checks for any overlapping times
            if start_time_conflict < schedule_end and schedule_start < end_time_conflict:
                return True  

        return False  

    def read_courses_from_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                details = line.split()
                course_code = details[0]
                course_section = details[1]
                course_days = details[2]
                course_start = details[3]
                course_end = details[4]
                if course_code not in self.courses_dict:
                    self.courses_dict[course_code] = []
                self.courses_dict[course_code].append((course_section, course_days, f"{course_start}-{course_end}"))

        return self.courses_dict

    def view_available_courses(self):
        available_courses_str = "Available Courses:\n"
        for course_code, course_details_list in self.courses_dict.items():
            for i in course_details_list:
                if course_code not in available_courses_str:
                    available_courses_str += f"{course_code} \n"
        return available_courses_str
#
    def main(self):
        coursesfile = self.read_courses_from_file("classes.txt")
        print(self.view_available_courses())  
        time_conflict = None

        num_courses = int(input("Enter the number of courses you'd like to register for: "))
        for i in range(num_courses):
            course_code = input("Enter the course code: ")
            if course_code in coursesfile:
              time_conflict = self.add_course(course_code)
            else:
                print("Course not found")

        if time_conflict == "Schedule can't be made.":
            print("Schedule can't be made.")
        else:
            print("\nYour Schedule:")
            if self.schedule:
                for course_info in self.schedule:
                    print(course_info)
            else:
                print("Your schedule is empty.")

student_instance = Student()
student_instance.main()
