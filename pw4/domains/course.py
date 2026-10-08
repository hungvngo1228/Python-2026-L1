class Course:
    """A course with an id, a name and a number of credits."""

    def __init__(self, course_id, name, credit):
        self.id = course_id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Credits: {self.credit}"
