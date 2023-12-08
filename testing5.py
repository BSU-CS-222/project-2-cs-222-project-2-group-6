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

    def compare_days_in_dict(self, index_to_compare):
        if not self.schedule:
            print("No courses in the schedule to compare.")
            return

        reference_day = self.schedule[0].split(", ")[1]  # Get the day from the first course in the schedule

        for course_info in self.schedule[1:]:
            day_to_compare = course_info.split(", ")[1]

            if day_to_compare == reference_day or day_to_compare != reference_day:
                self.compare_times_in_dict()
                break

    def compare_times_in_dict(self):
        for i in range(len(self.schedule)):
            course_info = self.schedule[i].split(", ")
            if len(course_info) >= 3:
                reference_section = course_info[0].split(":")[1].strip()
                reference_day = course_info[1]
                time_range_info = course_info[2].split(" ")
                if len(time_range_info) >= 2:
                    time_range = time_range_info[1].split('-')
                    if len(time_range) == 2:
                        reference_start_time, reference_end_time = time_range[0], time_range[1]
                    else:
                        print(f"Error: Unable to parse time range for course {course_info[0]}")
                        continue
                else:
                    print(f"Error: Unable to parse time range for course {course_info[0]}")
                    continue

                for j in range(i + 1, len(self.schedule)):
                    course_info_compare = self.schedule[j].split(", ")
                    if len(course_info_compare) >= 3:
                        section_compare = course_info_compare[0].split(":")[1].strip()
                        day_to_compare = course_info_compare[1]

                        if section_compare != reference_section and day_to_compare == reference_day:
                            time_range_info_compare = course_info_compare[2].split(" ")
                            if len(time_range_info_compare) >= 2:
                                time_range_compare = time_range_info_compare[1].split('-')
                                if len(time_range_compare) == 2:
                                    start_time, end_time = time_range_compare[0], time_range_compare[1]
                                else:
                                    print(f"Error: Unable to parse time range for course {course_info_compare[0]}")
                                    continue
                            else:
                                print(f"Error: Unable to parse time range for course {course_info_compare[0]}")
                                continue

                            if not (end_time < reference_start_time or start_time > reference_end_time):
                                print("Can't create schedule. Time conflict between courses.")
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


# Create an instance of the Student class and run the program
student_instance = Student()
student_instance.main()
