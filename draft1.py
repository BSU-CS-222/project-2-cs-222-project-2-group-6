from prettytable import PrettyTable

class Student:
    def __init__(self, student_id, max_credit_hours):
        self.student_id = student_id
        self.max_credit_hours = max_credit_hours
        self.schedule = []

    def add_course(self, course_code):
        try:
            if course_code in self.courses_dict:
                available_classes = self.courses_dict[course_code]

                # Choose the first available section automatically
                selected_section = available_classes[0]

                # Extract relevant information from the selected section
                section, days, start_time, end_time, credits = map(str.strip, selected_section)
                formatted_course_info = f"{course_code},{section},{days},{start_time},{end_time},{credits}"

                if not self.has_time_conflict(formatted_course_info):
                    self.schedule.append(formatted_course_info)  # adds courses to your schedule
                    return "Successfully added."
                else:
                    print("Time conflict with an existing course. You have been added this course.")
                    return "Please try to add a different course, no conflict time with your existing courses."

            else:
                return f"Course code {course_code} not found in available courses."

        except ValueError:
            return "Invalid input. Please try again."

    def resolve_time_conflict(self, new_course_details):
        for existing_course_index, existing_course in enumerate(self.schedule):
            # Check for overlapping days and time
            if existing_course.split(",")[2] == new_course_details.split(",")[2] and \
               max(existing_course.split(",")[3], new_course_details.split(",")[3]) < min(existing_course.split(",")[4], new_course_details.split(",")[4]):

                # Attempt to resolve conflict by swapping courses using backtracking
                if self.try_swap_courses(existing_course_index, new_course_details):
                    print("Time conflict resolved by swapping courses.")
                    return True

        # Unable to resolve conflict
        return False

    def try_swap_courses(self, existing_course_index, new_course_details):
        # Attempt to swap the conflicting courses using backtracking
        temp_schedule = self.schedule.copy()
        temp_schedule[existing_course_index], temp_schedule[-1] = temp_schedule[-1], temp_schedule[existing_course_index]

        if self.backtrack_resolve_conflicts(temp_schedule):
            self.schedule = temp_schedule[:-1]  # Remove the temporarily added course
            return True
        else:
            return False

    def backtrack_resolve_conflicts(self, schedule):
        # Backtracking algorithm to resolve conflicts in the schedule

        # Base case: If there are no more conflicts, return True
        if not self.has_conflicts(schedule):
            return True

        # Try swapping conflicting courses and recursively backtrack
        for i in range(len(schedule) - 1):
            if self.has_time_conflict(schedule[i]):
                temp_schedule = schedule.copy()
                temp_schedule[i], temp_schedule[-1] = temp_schedule[-1], temp_schedule[i]

                # Recursively check if the modified schedule is conflict-free
                if self.backtrack_resolve_conflicts(temp_schedule):
                    schedule[:] = temp_schedule
                    return True

        # If no valid swap is found, return False
        return False

    def has_conflicts(self, schedule):
        # Check if there are any conflicts in the schedule
        for i in range(len(schedule) - 1):
            if self.has_time_conflict(schedule[i]):
                return True
        return False

    def has_time_conflict(self, new_course_details):
        for existing_course in self.schedule:
            # Check for overlapping days and time
            if existing_course.split(",")[2] == new_course_details.split(",")[2] and \
               max(existing_course.split(",")[3], new_course_details.split(",")[3]) < min(existing_course.split(",")[4], new_course_details.split(",")[4]):
                return True
        return False

    def view_schedule(self):
        if not self.schedule:
            return "Your schedule is empty."
        else:
            schedule_table = PrettyTable(["Course", "Section", "Days", "Start-Time", "End-Time", "Credits"])

            for course_str in self.schedule:
                course_info = course_str.split(",")
                schedule_table.add_row(course_info)

            return f"Class Schedule:\n{schedule_table}"

    def read_courses_from_file(self, file_path):
        with open(file_path, 'r') as file:  # stores info from txt file to dict.
            self.courses_dict = {}
            for line in file:
                course_data = line.strip().split()

                course_code = course_data[0]

                course_details = course_data[1:]

                if course_code not in self.courses_dict:
                    # makes sure it prints every course from txt file
                    # not just 1 of each category of course code
                    self.courses_dict[course_code] = []

                self.courses_dict[course_code].append(course_details)

        return self.courses_dict

    def view_available_courses(self):
        available_courses_table = PrettyTable(["Course Code", "Section", "Days", "Start-Time", "End-Time", "Credits"])
        for course_code, course_details_list in self.courses_dict.items():
            for course_details in course_details_list:
                available_courses_table.add_row([course_code] + course_details)

        print("Available Courses:")
        print(available_courses_table)

    def main(self):
        while True:
            print('''\nx------------------------------------------x
|              Class Schedule              |
x------------------------------------------x''')
            print("1. Add Courses")
            print("2. View Schedule")
            print("3. Available Courses")
            print("4. Clear Schedule")
            print("5. Exit")

            choice = input("Please make your choice (1 to 5): ")

            if choice == '1':
                self.read_courses_from_file("classes.txt")
                num_courses = int(input("Enter the number of courses you'd like to register for: "))
                for i in range(num_courses):
                    course_code = input("Enter the course code (e.g., MATH166, CS222, CS120, CS124, CS121, CS230, MATH165): ")
                    result = self.add_course(course_code)
                    print(result)
            elif choice == '2':
                print(self.view_schedule())
            elif choice == '3':
                self.read_courses_from_file("classes.txt")
                self.view_available_courses()
            elif choice == '4':
                self.schedule.clear()
                print("Schedule cleared.")
            elif choice == '5':
                print("Good luck with your classes!")
                break
            else:
                print("Please only choose 1 to 5, try again!")

# Create a student instance
student_instance = Student("12345", 15)

# Call the main method
student_instance.main()