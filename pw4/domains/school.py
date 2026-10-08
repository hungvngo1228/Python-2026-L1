class School:
    """Holds all students and courses and the operations on them."""

    def __init__(self):
        self.students = []   # list of Student
        self.courses = {}    # course_id -> Course

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses[course.id] = course

    def get_course(self, course_id):
        return self.courses.get(course_id)

    def sort_students_by_gpa(self):
        """Sort the real student list by GPA, highest first."""
        self.students.sort(key=lambda s: s.gpa(self.courses), reverse=True)
