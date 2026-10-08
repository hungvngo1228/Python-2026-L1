import numpy as np


class Student:
    """A student with an id, a name, a date of birth and marks per course."""

    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # course_id -> mark

    def set_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        return self.marks.get(course_id)

    def gpa(self, courses):
        """Average GPA weighted by credits.

        courses: dict {course_id: Course}, used to look up the credits.
        """
        mark_list = []
        credit_list = []
        for course_id, mark in self.marks.items():
            if course_id in courses:
                mark_list.append(mark)
                credit_list.append(courses[course_id].credit)

        if not mark_list:
            return 0.0

        marks_arr = np.array(mark_list)
        credits_arr = np.array(credit_list)
        total_credits = np.sum(credits_arr)
        if total_credits == 0:
            return 0.0
        return float(np.sum(marks_arr * credits_arr) / total_credits)

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | DoB: {self.dob}"
