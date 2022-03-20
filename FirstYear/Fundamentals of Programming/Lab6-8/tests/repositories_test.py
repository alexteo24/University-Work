from domain.entities import Student, Discipline, Grade, StudentException, DisciplineException, GradeException
from repositories.repository import StudentRepository, DisciplineRepository, GradeRepository, test_init_students, \
    test_init_discipline, test_init_grades, StatisticRepository
import unittest


class TestStudentRepositoryMethods(unittest.TestCase):
    def setUp(self):
        self._StudentRepository = StudentRepository([])

    def test_instance(self):
        self.assertIsInstance(self._StudentRepository, StudentRepository)

    def test_add_student_to_repo(self):
        assert len(self._StudentRepository.list) == 0
        self._StudentRepository.add_student(Student('123456', 'Jane Doe'))
        assert len(self._StudentRepository.list) == 1
        self._StudentRepository.add_student(Student('123457', 'John Doe'))
        assert len(self._StudentRepository.list) == 2
        with self.assertRaises(StudentException):
            self._StudentRepository.add_student(Student('123457', 'Johnny Bravo'))

    def test_remove_student_from_repo(self):
        self._StudentRepository.add_student(Student('123456', 'Jane Doe'))
        self._StudentRepository.add_student(Student('123457', 'John Doe'))
        self._StudentRepository.add_student(Student('123458', 'Johnny Bravo'))
        assert len(self._StudentRepository.list) == 3
        self._StudentRepository.remove_student('123456')
        assert len(self._StudentRepository.list) == 2
        self._StudentRepository.remove_student('123458')
        assert len(self._StudentRepository.list) == 1
        with self.assertRaises(StudentException):
            self._StudentRepository.remove_student('123456')

    def test_update_student(self):
        self._StudentRepository.add_student(Student('123456', 'Jane Doe'))
        self._StudentRepository.add_student(Student('123457', 'John Doe'))
        self._StudentRepository.add_student(Student('123458', 'Johnny Bravo'))
        test_updated_student = Student('123456', 'Johanna Doe')
        self._StudentRepository.update_student(test_updated_student)
        for a_student in self._StudentRepository.list:
            if a_student.id == test_updated_student.id:
                assert a_student.name == 'Johanna Doe'
        with self.assertRaises(StudentException):
            self._StudentRepository.update_student(Student('123444', 'Tony Stark'))


class TestDisciplineRepository(unittest.TestCase):
    def setUp(self):
        self._DisciplineRepository = DisciplineRepository([])

    def test_instance(self):
        self.assertIsInstance(self._DisciplineRepository, DisciplineRepository)

    def test_add_discipline_to_repo(self):
        assert len(self._DisciplineRepository.list) == 0
        self._DisciplineRepository.add_discipline(Discipline('12345', 'FP'))
        assert len(self._DisciplineRepository.list) == 1
        self._DisciplineRepository.add_discipline(Discipline('12346', 'MuSiC'))
        assert len(self._DisciplineRepository.list) == 2
        with self.assertRaises(DisciplineException):
            self._DisciplineRepository.add_discipline(Discipline('12345', 'Nice try'))

    def test_remove_discipline_from_repo(self):
        self._DisciplineRepository.add_discipline(Discipline('12345', 'FP'))
        self._DisciplineRepository.add_discipline(Discipline('12346', 'MuSiC'))
        self._DisciplineRepository.add_discipline(Discipline('12347', 'ReLiGiOn'))
        self._DisciplineRepository.remove_discipline('12347')
        assert len(self._DisciplineRepository.list) == 2
        self._DisciplineRepository.remove_discipline('12346')
        assert len(self._DisciplineRepository.list) == 1
        with self.assertRaises(DisciplineException):
            self._DisciplineRepository.remove_discipline('12346')

    def test_update_discipline(self):
        self._DisciplineRepository.add_discipline(Discipline('12345', 'FP'))
        self._DisciplineRepository.add_discipline(Discipline('12346', 'MuSiC'))
        self._DisciplineRepository.add_discipline(Discipline('12347', 'ReLiGiOn'))
        updated_discipline = Discipline('12347', 'Something useful')
        self._DisciplineRepository.update_discipline(updated_discipline)
        for a_discipline in self._DisciplineRepository.list:
            if a_discipline.id == updated_discipline.id:
                assert a_discipline.name == 'Something useful'
        updated_discipline = Discipline('12336', 'MuSiC')
        with self.assertRaises(DisciplineException):
            self._DisciplineRepository.update_discipline(updated_discipline)


class TestGradeRepository(unittest.TestCase):
    def setUp(self):
        self._GradeRepository = GradeRepository([])

    def test_instance(self):
        self.assertIsInstance(self._GradeRepository, GradeRepository)

    def test_add_grade_to_repo(self):
        assert len(self._GradeRepository.list) == 0
        self._GradeRepository.add_grade(Grade('123456', '12345', '10'))
        assert len(self._GradeRepository.list) == 1
        self._GradeRepository.add_grade(Grade('123456', '12346', '5'))
        assert len(self._GradeRepository.list) == 2

    def test_remove_grade_student(self):
        self._GradeRepository.add_grade(Grade('123456', '12345', '10'))
        self._GradeRepository.add_grade(Grade('123456', '12346', '5'))
        self._GradeRepository.add_grade(Grade('123457', '12347', '7'))
        self._GradeRepository.remove_grade_student('123456')
        assert len(self._GradeRepository.list) == 1

    def test_remove_grade_discipline(self):
        self._GradeRepository.add_grade(Grade('123456', '12345', '10'))
        self._GradeRepository.add_grade(Grade('123456', '12346', '5'))
        self._GradeRepository.add_grade(Grade('123457', '12347', '7'))
        self._GradeRepository.remove_grade_discipline('12345')
        assert len(self._GradeRepository.list) == 2

    def test_search_grade_student_id(self):
        self._GradeRepository.add_grade(Grade('123456', '12345', '10'))
        self._GradeRepository.add_grade(Grade('123456', '12346', '5'))
        self._GradeRepository.add_grade(Grade('123457', '12347', '7'))
        search_result = self._GradeRepository.search_grade_student_id('123456')
        assert len(search_result) == 2

    def test_search_grade_discipline_id(self):
        self._GradeRepository.add_grade(Grade('123456', '12345', '10'))
        self._GradeRepository.add_grade(Grade('123456', '12346', '5'))
        self._GradeRepository.add_grade(Grade('123457', '12345', '7'))
        search_result = self._GradeRepository.search_grade_discipline_id('12346')
        assert len(search_result) == 1
        search_result = self._GradeRepository.search_grade_discipline_id('12345')
        assert len(search_result) == 2

    def test_remove_grade(self):
        self._GradeRepository.add_grade(Grade('123456', '12345', '10'))
        self._GradeRepository.add_grade(Grade('123456', '12346', '5'))
        self._GradeRepository.add_grade(Grade('123457', '12345', '7'))
        self._GradeRepository.remove_from_repo(Grade('123456', '12345', '10'))
        assert len(self._GradeRepository.list) == 2
        with self.assertRaises(GradeException):
            self._GradeRepository.remove_from_repo(Grade('123456', '12346', '2'))

class TestStatisticRepository(unittest.TestCase):
    def setUp(self):
        self._StatisticRepository = StatisticRepository()

    def test_instance(self):
        self.assertIsInstance(self._StatisticRepository, StatisticRepository)

    def test_add_to_statistic(self):
        assert len(self._StatisticRepository.list) == 0
        self._StatisticRepository.add_to_statistic(Student('123456', 'Georgel'))
        assert len(self._StatisticRepository.list) == 1

    def test_clear_statistic(self):
        self._StatisticRepository.add_to_statistic(Student('123457', 'Georgeli'))
        self._StatisticRepository.add_to_statistic(Student('123458', 'Georgeliu'))
        self._StatisticRepository.add_to_statistic(Student('123459', 'Georgelinu'))
        self._StatisticRepository.add_to_statistic(Student('123450', 'Georgelini'))
        assert len(self._StatisticRepository.list) == 4
        self._StatisticRepository.clear_statistic()
        assert len(self._StatisticRepository.list) == 0


class TestInitRepositoryStudents(unittest.TestCase):
    def setUp(self):
        self._StudentRepository = test_init_students()

    def test_instance(self):
        self.assertIsInstance(self._StudentRepository, StudentRepository)

    def test_length(self):
        assert len(self._StudentRepository.list) == 10


class TestInitRepositoryDisciplines(unittest.TestCase):
    def setUp(self):
        self._DisciplineRepository = test_init_discipline()

    def test_instance(self):
        self.assertIsInstance(self._DisciplineRepository, DisciplineRepository)

    def test_length(self):
        assert len(self._DisciplineRepository.list) == 10


class TestInitRepositoryGrades(unittest.TestCase):
    def setUp(self):
        self._GradeRepository = test_init_grades(test_init_students(), test_init_discipline())

    def test_instance(self):
        self.assertIsInstance(self._GradeRepository, GradeRepository)

    def test_length(self):
        assert len(self._GradeRepository.list) == 10
