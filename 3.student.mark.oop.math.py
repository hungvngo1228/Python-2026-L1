import math
import numpy as np
import curses

students = []
courses = []
marks = {}       
credits_dict = {} 

def input_students():
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        print(f"\n--- Student {i+1} ---")
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students.append({"id": s_id, "name": name, "dob": dob})

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        print(f"\n--- Course {i+1} ---")
        c_id = input("Course ID: ")
        name = input("Course Name: ")
        credit = int(input("Course Credits (e.g., 3): "))
        courses.append({"id": c_id, "name": name})
        credits_dict[c_id] = credit

def input_marks():
    course_id = input("Enter Course ID to input marks: ")
    if course_id not in [c['id'] for c in courses]:
        print("Course ID not found!")
        return
        
    if course_id not in marks:
        marks[course_id] = {}
        
    print(f"--- Entering Marks for Course: {course_id} ---")
    for student in students:
        raw_mark = float(input(f"Enter mark for {student['name']} (0-20): "))
        floored_mark = math.floor(raw_mark * 10) / 10.0
        marks[course_id][student['id']] = floored_mark

def list_courses():
    print("\n--- Courses ---")
    for course in courses:
        c_credit = credits_dict.get(course['id'], 0)
        print(f"ID: {course['id']} | Name: {course['name']} | Credits: {c_credit}")

def list_students():
    print("\n--- Students ---")
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | DoB: {student['dob']}")

def show_marks():
    course_id = input("Enter Course ID to view marks: ")
    if course_id in marks:
        print(f"\n--- Marks for Course {course_id} ---")
        for student in students:
            m = marks[course_id].get(student['id'], "No mark")
            print(f"{student['name']}: {m}")
    else:
        print("No marks found for this course.")

def calculate_gpa(student_id):
    """Calculate average GPA for a given student using numpy arrays (weighted sum of credits and marks)"""
    student_marks = []
    course_credits = []
    
    for c_id, course_marks in marks.items():
        if student_id in course_marks:
            student_marks.append(course_marks[student_id])
            course_credits.append(credits_dict.get(c_id, 0))
            
    if not student_marks:
        return 0.0
        
    marks_arr = np.array(student_marks)
    credits_arr = np.array(course_credits)
    
    total_credits = np.sum(credits_arr)
    if total_credits == 0:
        return 0.0
        
    gpa = np.sum(marks_arr * credits_arr) / total_credits
    return float(gpa)

def sort_students_by_gpa():
    """Sort student list by GPA descending using numpy/calculated GPAs"""
    student_gpas = []
    for student in students:
        gpa = calculate_gpa(student['id'])
        student_gpas.append((student, gpa))
        
    student_gpas.sort(key=lambda x: x[1], reverse=True)
    
    print("\n--- Students Sorted by GPA (Descending) ---")
    for student, gpa in student_gpas:
        print(f"Name: {student['name']} (ID: {student['id']}) - GPA: {gpa:.2f}")

def curses_menu(stdscr):
    curses.curs_set(0)

    options = [
        "Input students",
        "Input courses",
        "Input marks",
        "List students",
        "List courses",
        "Show marks",
        "Sort by GPA",
        "Exit"
    ]

    actions = [
        input_students,
        input_courses,
        input_marks,
        list_students,
        list_courses,
        show_marks,
        sort_students_by_gpa
    ]

    selected = 0

    while True:
        stdscr.clear()

        # Title
        stdscr.addstr(
            0,
            2,
            "STUDENT MARK MANAGEMENT",
            curses.A_BOLD
        )

        # Menu
        for i, text in enumerate(options):
            if i == selected:
                attribute = curses.A_REVERSE
            else:
                attribute = curses.A_NORMAL

            stdscr.addstr(
                2 + i,
                4,
                text,
                attribute
            )

        stdscr.refresh()

        # Wait for keyboard input
        key = stdscr.getch()

        # Move up
        if key == curses.KEY_UP:
            selected = (selected - 1) % len(options)

        # Move down
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(options)

        # Enter
        elif key in (10, 13):

            # Exit
            if selected == len(options) - 1:
                break

            # Leave curses temporarily
            curses.endwin()

            # Run selected function
            actions[selected]()

            input("\nPress Enter to return to menu...")

def main():
    curses.wrapper(curses_menu)
    
    while True:
        print("\n" + "="*40)
        print("STUDENT MARK MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Input students")
        print("2. Input courses & credits")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Sort students by GPA descending")
        print("0. Exit")
        
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
        elif choice == '7':
            sort_students_by_gpa()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()