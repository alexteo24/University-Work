class StudentException(Exception):
    def __init__(self, message):
        self._message = message


class DisciplineException(Exception):
    def __init__(self, message):
        self._message = message


class GradeException(Exception):
    def __init__(self, message):
        self._message = message


class Student:
    def __init__(self, student_id=None, student_name=None):
        self._student_id = student_id
        self._student_name = student_name

    @property
    def id(self):
        return self._student_id

    @property
    def name(self):
        return self._student_name

    def __str__(self) -> str:
        return "The student {0} has the id {1}".format(self._student_name, self._student_id)


class Discipline:
    def __init__(self, discipline_id=None, discipline_name=None):
        self._discipline_id = discipline_id
        self._discipline_name = discipline_name

    @property
    def id(self):
        return self._discipline_id

    @property
    def name(self):
        return self._discipline_name

    def __str__(self) -> str:
        return "The discipline {0} has the id {1}".format(self._discipline_name, self._discipline_id)


class Grade:
    def __init__(self, student_id=None, discipline_id=None, grade_value=None):
        self._discipline_id = discipline_id
        self._student_id = student_id
        self._grade_value = grade_value

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def student_id(self):
        return self._student_id

    @property
    def value(self):
        return self._grade_value

    def __str__(self) -> str:
        return "The grade {0} is for the student {1} at the discipline" \
               " {2}".format(self._grade_value, self._student_id, self._discipline_id)


class StudentValidator:
    @staticmethod
    def validate(student):
        if student.name is None or student.id is None:
            raise StudentException('Invalid student format! You are missing either the name or the ID!')
        student_name = student.name
        student_name = student_name.replace(' ', '')
        if not student_name.isalpha():
            raise StudentException('Invalid student name!')
        if len(student.id) != 6:
            raise StudentException('Invalid student ID!')
        if not student.id.isdigit():
            raise StudentException('Invalid student ID!')


class DisciplineValidator:
    @staticmethod
    def validate(discipline):
        if discipline.id is None or discipline.name is None:
            raise DisciplineException('Invalid discipline format! You are missing either the name or the ID!')
        discipline_name = discipline.name
        discipline_name = discipline_name.replace(' ', '')
        if not discipline_name.isalpha():
            raise DisciplineException('Invalid discipline name!')
        if len(discipline.id) != 5:
            raise DisciplineException('Invalid discipline ID!')
        if not discipline.id.isdigit():
            raise DisciplineException('Invalid discipline ID!')


class GradeValidator:
    @staticmethod
    def validate(grade):
        if grade.student_id is None or grade.discipline_id is None or grade.value is None:
            raise GradeException('Invalid grade format! You are missing the student it, discipline id or grade value!')
        if len(grade.student_id) != 6:
            raise GradeException('Invalid student ID!')
        if not grade.student_id.isdigit():
            raise GradeException('Invalid discipline ID!')
        if len(grade.discipline_id) != 5:
            raise GradeException('Invalid discipline ID!')
        if not grade.discipline_id.isdigit():
            raise GradeException('Invalid discipline ID!')
        if grade.value.isalpha():
            raise GradeException('Invalid grade!')
        if int(grade.value) < 0 or int(grade.value) > 10:
            raise GradeException('Invalid grade!')
