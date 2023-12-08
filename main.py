def get_total_num_courses():
    pass #i have 4 right now.

def credit_hour_check():
    fileHandle = open("classes.txt", "r")
    fileData = fileHandle.readlines()

    for line in fileData:
        course_info = line.strip().split(',')


def fetchspecificcourses():
    courses = []
    fileHandle = open("classes.txt", "r")
    fileData = fileHandle.readlines()
    for line in fileData:
        course_info = line.strip().split(',')
    


def fetchcourses():
    courses = []
    seenCourses = []
    fileHandle = open("classes.txt", "r")
    fileData = fileHandle.readlines()
    for line in fileData:
        course_info = line.strip().split(',')
         
         
        if course_info not in seenCourses:
            seenCourses.append(course_info)
            courses.append(course_info)


    for course_info in seenCourses:
        print(f"Course: {course_info[0]}")
        print(f"Section: {course_info[1]}")
        print(f"Days: {course_info[2]}")
        print(f"Start Time: {course_info[3]}")
        print(f"End Time: {course_info[4]}")
        print(f"Credit Hours: {course_info[5]}")
        print()
        

    return courses


def main():
    getinfo = input("Welcome to the course scheduler! Enter 1 to see available courses for the upcoming semester:")
    if getinfo == "1":
        fetchcourses()
    else:
        quit()
        
    nCourses = input("Please enter the number of courses you would like to sign up for:")
    nCourseNumbers = input("Enter Course Number to search: ")
    courses = []
    fileHandle = open("classes.txt", "r")
    fileData = fileHandle.readlines()

    for line in fileData:
        course_info = line.strip().split(',')
    
        if nCourseNumbers == course_info[0]:
            print(f"Course: {course_info[0]}")
            print(f"Section: {course_info[1]}")
            print(f"Days: {course_info[2]}")
            print(f"Start Time: {course_info[3]}")
            print(f"End Time: {course_info[4]}")
            print()
            
        
    

main()