import pytest

from grade_system import GradeSystem, Student


def test_student_average_and_grade():
    student = Student("Ava", [90, 85, 95])

    assert student.average == pytest.approx(90.0)
    assert student.letter_grade() == "A"


def test_grade_system_adds_and_ranks_students():
    system = GradeSystem()
    system.add_student("Ava", [90, 85, 95])
    system.add_student("Noah", [80, 70, 75])
    system.add_student("Mia", [60, 70, 80])

    assert list(system.students.keys()) == ["Ava", "Noah", "Mia"]
    assert system.top_student()[0] == "Ava"
    assert system.top_student()[1] == pytest.approx(90.0)
    assert system.student_report("Noah")["letter_grade"] == "C"
