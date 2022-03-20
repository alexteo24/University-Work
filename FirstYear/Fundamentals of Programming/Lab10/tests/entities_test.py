from domain.entities import Student, Discipline, Grade, StudentValidator, DisciplineValidator, GradeValidator, \
    StudentException, DisciplineException, GradeException
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self._Student = Student()

    def test_instance(self):
        self.assertIsInstance(self._Student, Student)

    def test_student_attributes(self):
        test_student = Student('123456', 'Jane Doe')
        assert test_student.id == '123456'
        assert test_student.name == 'Jane Doe'

    def test_string(self):
        test_student = Student('123456', 'Jane Doe')
        string_return = test_student.__str__()
        assert string_return == "The student Jane Doe has the id 123456"


class TestDiscipline(unittest.TestCase):
    def setUp(self):
        self._Discipline = Discipline()

    def test_instance(self):
        self.assertIsInstance(self._Discipline, Discipline)

    def test_discipline_attributes(self):
        test_discipline = Discipline('12345', 'FP')
        assert test_discipline.id == '12345'
        assert test_discipline.name == 'FP'

    def test_string(self):
        test_discipline = Discipline('12345', 'FP')
        string_return = test_discipline.__str__()
        assert string_return == 'The discipline FP has the id 12345'


class TestGrade(unittest.TestCase):
    def setUp(self):
        self._Grade = Grade()

    def test_instance(self):
        self.assertIsInstance(self._Grade, Grade)

    def test_grade_attributes(self):
        test_grade = Grade('123456', '12345', '10')
        assert test_grade.student_id == '123456'
        assert test_grade.discipline_id == '12345'
        assert test_grade.value == '10'

    def test_string(self):
        test_grade = Grade('123456', '12345', '10')
        string_return = test_grade.__str__()
        assert string_return == 'The grade 10 is for the student 123456 at the discipline 12345'


class TestStudentValidator(unittest.TestCase):
    def setUp(self):
        self._StudentValidator = StudentValidator()

    def test_instance(self):
        self.assertIsInstance(self._StudentValidator, StudentValidator)

    def test_validator(self):
        test_student = Student(None, 'George')
        with self.assertRaises(StudentException):
            self._StudentValidator.validate(test_student)
        test_student = Student('123456', None)
        with self.assertRaises(StudentException):
            self._StudentValidator.validate(test_student)
        test_student = Student('123456', "12George Bibi")
        with self.assertRaises(StudentException):
            self._StudentValidator.validate(test_student)
        test_student = Student('12344645', 'Nicholas')
        with self.assertRaises(StudentException):
            self._StudentValidator.validate(test_student)
        test_student = Student('abcdef', 'Chicken')
        with self.assertRaises(StudentException):
            self._StudentValidator.validate(test_student)


class TestDisciplineValidator(unittest.TestCase):
    def setUp(self):
        self._DisciplineValidator = DisciplineValidator()

    def test_instance(self):
        self.assertIsInstance(self._DisciplineValidator, DisciplineValidator)

    def test_validator(self):
        test_discipline = Discipline(None, 'FP')
        with self.assertRaises(DisciplineException):
            self._DisciplineValidator.validate(test_discipline)
        test_discipline = Discipline('12345', None)
        with self.assertRaises(DisciplineException):
            self._DisciplineValidator.validate(test_discipline)
        test_discipline = Discipline('12345', '12Geometry')
        with self.assertRaises(DisciplineException):
            self._DisciplineValidator.validate(test_discipline)
        test_discipline = Discipline('1235655', 'God Planned')
        with self.assertRaises(DisciplineException):
            self._DisciplineValidator.validate(test_discipline)
        test_discipline = Discipline('abcde', 'Nema')
        with self.assertRaises(DisciplineException):
            self._DisciplineValidator.validate(test_discipline)


class TestGradeValidator(unittest.TestCase):
    def setUp(self):
        self._GradeValidator = GradeValidator()

    def test_instance(self):
        self.assertIsInstance(self._GradeValidator, GradeValidator)

    def test_validator(self):
        test_grade = Grade(None, '12345', '10')
        with self.assertRaises(GradeException):
            self._GradeValidator.validate(test_grade)
        test_grade = Grade('123456', None, '10')
        with self.assertRaises(GradeException):
            self._GradeValidator.validate(test_grade)
        test_grade = Grade('123456', '12345', None)
        with self.assertRaises(GradeException):
            self._GradeValidator.validate(test_grade)
        test_grade = Grade('1234568', '12345', '10')
        with self.assertRaises(GradeException):
            self._GradeValidator.validate(test_grade)
        test_grade = Grade('12345a', '12345', '10')
        with self.assertRaises(GradeException):
            self._GradeValidator.validate(test_grade)
        test_grade = Grade('123456', '12356777', '10')
        with self.assertRaises(GradeException):
            self._GradeValidator.validate(test_grade)
        test_grade = Grade('123456', 'avcde', '10')
        with self.assertRaises(GradeException):
            self._GradeValidator.validate(test_grade)
        test_grade = Grade('123456', '12345', 'ten')
        with self.assertRaises(GradeException):
            self._GradeValidator.validate(test_grade)
        test_grade = Grade('123456', '12345', '11')
        with self.assertRaises(GradeException):
            self._GradeValidator.validate(test_grade)
            test_grade = Grade('123456', '12345', '-1')
            with self.assertRaises(GradeException):
                self._GradeValidator.validate(test_grade)
