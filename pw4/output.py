"""Module for output: everything that is drawn with curses."""

import curses

TITLE_PAIR = 1
KEY_ENTER_CODES = (10, 13, curses.KEY_ENTER)


def setup(stdscr):
    """Initial curses settings: hide the cursor and prepare colors."""
    curses.curs_set(0)
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(TITLE_PAIR, curses.COLOR_CYAN, -1)


def _title_attr():
    attr = curses.A_BOLD
    if curses.has_colors():
        attr |= curses.color_pair(TITLE_PAIR)
    return attr


def _put(stdscr, y, x, text, attr=curses.A_NORMAL):
    """addstr that never crashes when the text does not fit the window."""
    height, width = stdscr.getmaxyx()
    if 0 <= y < height - 1 and 0 <= x < width - 1:
        stdscr.addstr(y, x, text[: width - x - 1], attr)


def menu(stdscr, title, options, selected=0):
    """Show a menu navigated with UP/DOWN and Enter. Return the chosen index."""
    while True:
        stdscr.erase()
        stdscr.border()
        _put(stdscr, 1, 3, title, _title_attr())
        for i, text in enumerate(options):
            attr = curses.A_REVERSE if i == selected else curses.A_NORMAL
            _put(stdscr, 3 + i, 5, f" {text} ", attr)
        _put(stdscr, 4 + len(options), 3, "UP/DOWN: move   ENTER: select")
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP:
            selected = (selected - 1) % len(options)
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(options)
        elif key in KEY_ENTER_CODES:
            return selected


def show_lines(stdscr, title, lines):
    """Show a titled page of text and wait for a key."""
    stdscr.erase()
    stdscr.border()
    _put(stdscr, 1, 3, title, _title_attr())
    for i, line in enumerate(lines):
        _put(stdscr, 3 + i, 5, line)
    _put(stdscr, 4 + len(lines), 3, "Press any key to go back...")
    stdscr.refresh()
    stdscr.getch()


def show_students(stdscr, students):
    lines = [str(s) for s in students] or ["(no students yet)"]
    show_lines(stdscr, "STUDENTS", lines)


def show_courses(stdscr, courses):
    lines = [str(c) for c in courses] or ["(no courses yet)"]
    show_lines(stdscr, "COURSES", lines)


def show_marks(stdscr, school, course_id):
    lines = []
    for student in school.students:
        mark = student.get_mark(course_id)
        lines.append(f"{student.name}: {'No mark' if mark is None else mark}")
    show_lines(stdscr, f"MARKS OF COURSE {course_id}",
               lines or ["(no students yet)"])


def show_sorted_students(stdscr, school):
    lines = [f"{s.name} (ID: {s.id}) - GPA: {s.gpa(school.courses):.2f}"
             for s in school.students]
    show_lines(stdscr, "STUDENTS SORTED BY GPA (DESCENDING)",
               lines or ["(no students yet)"])


def run_in_terminal(stdscr, func, *args, pause=True):
    """Leave curses, run a normal print/input function, then come back.

    It waits for Enter when pause is True, or when func returned None
    (so that an error message printed by func can still be read).
    """
    curses.endwin()
    result = func(*args)
    if pause or result is None:
        input("\nPress Enter to return to the menu...")
    stdscr.refresh()
    return result
