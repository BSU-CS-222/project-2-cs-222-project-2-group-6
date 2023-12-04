class Student:
    def __init__(self, student_id, max_credit_hours):
        self.student_id = student_id
        self.max_credit_hours = max_credit_hours
        self.schedule = []
        self.courses_dict = {}  # Initialize the dictionary to store course details

    def add_course(self, course_info):
        # Assuming course_info is a string in the format "CS120,001,MWF,0900,0950"
        try:
            course_details = course_info.split(',')
            course_code, section, days, start_time, end_time, credits = course_details

            # Format start_time and end_time as HH:MM
            start_time = f"{start_time[:2]}:{start_time[2:]}"
            end_time = f"{end_time[:2]}:{end_time[2:]}"

            # Check for time conflicts before adding the course
            if not self.has_time_conflict(course_details):
                # Append the formatted course information to the schedule
                formatted_course_info = f"{course_code} {section} {days} {start_time}-{end_time} {credits}"
                self.schedule.append(formatted_course_info)
                return "Successfully added."
            else:
                return "Time conflict with an existing course."
        except ValueError:
            return "Please enter the course information in the correct format."





    def has_time_conflict(self, new_course_details):
        for existing_course in self.schedule:
            # Check for overlapping days and time
            if existing_course[2] == new_course_details[2] and \
               max(existing_course[3], new_course_details[3]) < min(existing_course[4], new_course_details[4]):
                return True
        return False

    def view_schedule(self):
        if not self.schedule:
            return "Your schedule is empty."
        else:
            schedule_header = "Class Schedule:\n"
            schedule_table = "X----------------------------------------------------X\n"
            schedule_table += "|Course|Section|Days|Start-Time|End-Time|Credits\n"
            schedule_table += "X---------------------------------------------------X\n"

            for course_str in self.schedule:
                # No need to split course_str since it's already a string
                schedule_table += f"| {course_str}\n"

            schedule_table += "+----------------------------------------------+"
            return schedule_header + schedule_table
        
    def read_courses_from_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into key-value pairs
                course_data = line.strip().split(',')

                # Assuming the first element is the key (course code)
                course_code = course_data[0]

                # The rest of the elements are values (course details)
                course_details = course_data[1:]

                # Add the key-value pair to the dictionary
                self.courses_dict[course_code] = course_details

    def view_available_courses(self):
        print("Available Courses:")
        for course_code, course_details in self.courses_dict.items():
            print(f"{course_code}: {', '.join(course_details)}")

    def remove_course(self, course_to_remove):
        if course_to_remove in self.schedule:
            self.schedule.remove(course_to_remove)
            return f"Course {course_to_remove} removed successfully."
        else:
            return f"Course {course_to_remove} not found in your schedule."

    def main(self):
        while True:
            print('''\nx------------------------------------------x
|              Class Schedule              |
x------------------------------------------x''')
            print("1. Add the Courses")
            print("2. You can view your Schedule")
            print("3. These are the available courses that offering for this semester.")
            print("4. Remove this courses")
            print("5. Clear Schedule")
            print("6. Exit")

            choice = input("Please make your choice (1 to 6): ")

            if choice == '1':
                self.read_courses_from_file("classes.txt")
                course_code = input("Enter the course code (e.g., CS120, CS121, CS122, CS416, MATH181, CS418, CS239): ")
                section = input("Enter the section:(e.g., 001,002,003,005):")
                days = input("Enter the meeting days (e.g., MWF or TR): ")
                start_time = input("Enter the start time (e.g., 0900, 0930, 1230, 1300, 1100, 1400, 1200): ")
                end_time = input("Enter the end time (e.g., 0950, 1045, 1345, 1350, 1215, 1015, 1450, 1250, 0950): ")
                credits = input("Enter the credit amount (e.g., 3 or 4):")
                # Format the input into the required string format
                course_to_add = f"{course_code},{section},{days},{start_time},{end_time},{credits}"

                result = student_instance.add_course(course_to_add)
                print(result)

            elif choice == '2':
                print(self.view_schedule())
            elif choice == '3':
                self.read_courses_from_file("classes.txt")
                self.view_available_courses()
            elif choice == '4':
                course_code = input("Enter the course code to remove (e.g., CS120): ")
                section = input("Enter the section to remove: ")
                course_to_remove = f"{course_code},{section}"
                result = self.remove_course(course_to_remove)
                print(result)
            elif choice == '5':
                self.schedule.clear()
                print("Schedule cleared.")
            elif choice == '6':
                print("You have successfully added the courses, good luck with all your classes!")
                break
            else:
                print("Please only choose 1 to 6, try again!")

# Create a student instance
student_instance = Student("12345", 15)

# Call the main method
student_instance.main()
