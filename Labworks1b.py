students = []
courses = []
marks = {}

def input_students():
    """Input number of students in a class, then their information"""
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students.append({"id": s_id, "name": name, "dob": dob})

def input_courses():
    """Input number of courses, then their information"""
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        c_id = input("Course ID: ")
        name = input("Course Name: ")
        courses.append({"id": c_id, "name": name})

def input_marks():
    """Select a course, input marks for students in this course"""
    course_id = input("Enter Course ID to input marks: ")

    if not any(course["id"] == course_id for course in courses):
        print("Course not found!")
        return
    
    marks[course_id] = {}
    for student in students:
        mark = float(input(f"Enter mark for {student['name']}: "))
        marks[course_id][student['id']] = mark

def list_courses():
    """List all courses"""
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    """List all students"""
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_marks():
    """Show student marks for a given course"""
    course_id = input("Enter Course ID to view marks: ")
    if course_id in marks:
        for student in students:
            student_mark = marks[course_id].get(student['id'], "No mark")
            print(f"{student['name']}: {student_mark}")
    else:
        print("No marks found for this course.")

while True:
    print("\n1. Input students | 2. Input courses | 3. Input marks")
    print("4. List students  | 5. List courses  | 6. Show marks | 0. Exit")
    
    choice = input("Select an option: ")
    
    if choice == '1':
        input_students()
    elif choice == '2':
        input_courses()
    elif choice == '3':
        input_marks()
    elif choice == '4':
        list_students()
    elif choice == '5':
        list_courses()
    elif choice == '6':
        show_marks()
    elif choice == '0':
        break