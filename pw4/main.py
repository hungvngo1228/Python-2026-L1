"""Main script: only coordinates input.py, output.py and the domains package."""

import curses

import input as inp      # "import input" alone would hide the builtin input()
import output as out
from domains import School

OPTIONS = [
    "Input students",
    "Input courses",
    "Input marks",
    "List students",
    "List courses",
    "Show marks of a course",
    "Sort students by GPA (descending)",
    "Exit",
]


def run(stdscr):
    out.setup(stdscr)
    school = School()
    selected = 0

    while True:
        selected = out.menu(stdscr, "STUDENT MARK MANAGEMENT", OPTIONS, selected)

        if selected == 0:
            out.run_in_terminal(stdscr, inp.input_students, school)
        elif selected == 1:
            out.run_in_terminal(stdscr, inp.input_courses, school)
        elif selected == 2:
            out.run_in_terminal(stdscr, inp.input_marks, school)
        elif selected == 3:
            out.show_students(stdscr, school.students)
        elif selected == 4:
            out.show_courses(stdscr, list(school.courses.values()))
        elif selected == 5:
            course_id = out.run_in_terminal(
                stdscr, inp.ask_course_id, school, pause=False)
            if course_id is not None:
                out.show_marks(stdscr, school, course_id)
        elif selected == 6:
            school.sort_students_by_gpa()
            out.show_sorted_students(stdscr, school)
        elif selected == 7:
            break


def main():
    curses.wrapper(run)


if __name__ == "__main__":
    main()
