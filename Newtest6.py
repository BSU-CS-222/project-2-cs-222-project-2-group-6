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

    def has_time_conflict(self, new_course_info, existing_schedule):
        _, _, reference_days, reference_start_time, reference_end_time = map(str.strip, new_course_info.split(" "))

        for course_info in existing_schedule:
            _, _, days, start_time, end_time = map(str.strip, course_info.split(" "))

            if any(day in reference_days for day in days):
            # Check for time conflict only if the courses are scheduled on the same day(s)
                if int(start_time) < int(reference_end_time) and int(end_time) > int(reference_start_time):
                    return True

        return False


    def backtrack_resolve_conflicts(self, courses, current_schedule):
        stack = [(courses, current_schedule)]

        while stack:
            current_courses, current_schedule = stack.pop()

            if not current_courses:
                self.schedule = current_schedule
                return True

            current_course = current_courses.pop()

            # Check for conflicts with the existing schedule
            if not self.has_time_conflict(current_course, current_schedule):
                # If no conflict, continue with the remaining courses
                stack.append((current_courses, current_schedule + [current_course]))

        # If no valid schedule is found, return False
        return False

    def main(self):
        coursesfile = self.read_courses_from_file("classes.txt")
        print(self.view_available_courses())

        num_courses = int(input("Enter the number of courses you'd like to register for: "))
        selected_courses = []
        for i in range(num_courses):
            course_code = input("Enter the course code: ")
            if course_code in coursesfile:
                selected_courses.append(course_code)
            else:
                print("Course not found")

        # Prepare a list of course information for the selected courses
        courses_info = []
        for course_code in selected_courses:
            available_classes = self.courses_dict[course_code]
            selected_section = available_classes[0]
            section, days, start_time, end_time = map(str.strip, selected_section)
            courses_info.append(f"{course_code}: {section}, {days}, {start_time}-{end_time}")

        # Use backtracking to resolve time conflicts and create the schedule
        success = self.backtrack_resolve_conflicts(courses_info, [])

        if success:
            print("\nSchedule Successfully Created!")
            print("\nYour Schedule:")
            for course_info in self.schedule:
                print(course_info)
        else:
            print("\nUnable to create a conflict-free schedule.")

# Create an instance of the Student class and run the program
student_instance = Student()
student_instance.main()
