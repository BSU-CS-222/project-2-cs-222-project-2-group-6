class Student:
    def __init__(self, student_id, max_credit_hours):
        self.student_id = student_id
        self.max_credit_hours = max_credit_hours
        self.schedule = [] 

    def add_course(self, course_info):
        try:
            course_code = course_info
            if course_code in self.courses_dict:
                available_classes = self.courses_dict[course_code]
                print(f"Available Sections for {course_code}:")
                print("Choose by inputting number, where '0' is the course at the top of the list.")

                for class_info in available_classes:
                    print(class_info)

                class_choice = int(input("Enter the number of the section you want to register for: "))
                selected_section = available_classes[class_choice]

                section, days, start_time, end_time, credits = selected_section
                formatted_course_info = f"{course_code},{section},{days},{start_time},{end_time},{credits}"

                if not self.has_time_conflict(formatted_course_info):
                    self.schedule.append(formatted_course_info) #adds courses to your schedule
                    return "Successfully added."
                else:
                    print("Time conflict with an existing course.")

            else:
                return f"Course code {course_code} not found in available courses."

        except ValueError:
            return "Time conflict with an existing course, please try again."

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
         with open(file_path, 'r') as file:   #stores info from txt file to dict.
            self.courses_dict = {}
            for line in file:
                course_data = line.strip().split(',')
                
                course_code = course_data[0]
                
                course_details = course_data[1:]
                
                if course_code not in self.courses_dict: #makes sure it prints every course from txt file
                                                         #not just 1 of each category of course code
                    self.courses_dict[course_code] = []

                self.courses_dict[course_code].append(course_details)

            return self.courses_dict

    def view_available_courses(self):
        print("Available Courses:")
        for course_code, course_details_list in self.courses_dict.items():
            for course_details in course_details_list:
                print(f"{course_code}: {course_details}")

    
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
                student_instance.read_courses_from_file("classes.txt")
                num_courses = int(input("Enter the number of courses you'd like to register for: "))
                for i in range(num_courses):
                    course_code = input("Enter the course code (e.g., CS120, CS121, CS122, CS416, MATH181, CS418, CS239): ")
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
                print("Please only choose 1 to 6, try again!")

# Create a student instance
student_instance = Student("12345", 15)

# Call the main method
student_instance.main()