"""Module for input: everything that reads from the keyboard."""

import math

from domains import Course, Student


def read_number(prompt, cast, low=None, high=None):
    """Keep asking until the user types a valid number in [low, high]."""
    while True:
        try:
            value = cast(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")
            continue
        if (low is not None and value < low) or (high is not None and value > high):
            print("Value is out of the allowed range, please try again.")
            continue
        return value


def floor_mark(raw_mark):
    """Round a mark down to 1 decimal digit, e.g. 8.77 -> 8.7."""
    return math.floor(raw_mark * 10) / 10.0


def input_students(school):
    count = read_number("Enter number of students: ", int, low=1)
    for i in range(count):
        print(f"\n--- Student {i + 1} ---")
        student_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        school.add_student(Student(student_id, name, dob))


def input_courses(school):
    count = read_number("Enter number of courses: ", int, low=1)
    for i in range(count):
        print(f"\n--- Course {i + 1} ---")
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        credit = read_number("Course Credits (e.g., 3): ", int, low=1)
        school.add_course(Course(course_id, name, credit))


def ask_course_id(school):
    """Ask for a course id. Return it, or None if the course does not exist."""
    course_id = input("Enter Course ID: ")
    if school.get_course(course_id) is None:
        print("Course ID not found!")
        return None
    return course_id


def input_marks(school):
    if not school.students:
        print("No students yet. Input students first.")
        return
    course_id = ask_course_id(school)
    if course_id is None:
        return

    print(f"--- Entering marks for course: {course_id} ---")
    for student in school.students:
        raw = read_number(f"Enter mark for {student.name} (0-20): ", float, 0, 20)
        student.set_mark(course_id, floor_mark(raw))
