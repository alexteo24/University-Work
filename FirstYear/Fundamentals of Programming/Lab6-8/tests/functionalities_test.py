import unittest

from domain.entities import StudentValidator, StudentException, DisciplineValidator, DisciplineException, \
    GradeValidator, GradeException, Grade, Discipline, Student
from functionalities.functionalities import ServiceStudents, ServiceDisciplines, ServiceGrades, ServiceStatistic, \
    UndoRedoService, UndoRedoException, FunctionCall, Operation
from repositories.repository import StudentRepository, DisciplineRepository, GradeRepository, StatisticRepository


class TestServiceStudentMethods(unittest.TestCase):
    def setUp(self):
        self._student_validator = StudentValidator()
        self._student_repository = StudentRepository()
        self._undo_redo_service = UndoRedoService()
        self._student_service = ServiceStudents(self._student_repository, self._student_validator,
                                                self._undo_redo_service)

    def test_instance(self):
        self.assertIsInstance(self._student_service, ServiceStudents)

    def test_add_to_repo(self):
        assert len(self._student_service.repo.list) == 0
        self._student_service.add_to_repo('123456', 'Jane Doe')
        assert len(self._student_service.repo.list) == 1
        self._student_service.add_to_repo('123457', 'John Doe')
        assert len(self._student_service.repo.list) == 2
        with self.assertRaises(StudentException):
            self._student_service.add_to_repo('123456', 'Gheorghe Passat')

    def test_remove_student(self):
        self._student_service.add_to_repo('123456', 'Jane Doe')
        self._student_service.add_to_repo('123457', 'John Doe')
        self._student_service.remove_from_repo('123456')
        assert len(self._student_service.repo.list) == 1
        with self.assertRaises(StudentException):
            self._student_service.remove_from_repo('123568')

    def test_update_student(self):
        self._student_service.add_to_repo('123456', 'Jane Doe')
        self._student_service.add_to_repo('123457', 'John Doe')
        self._student_service.update('123457', 'Johnutu Doe')
        for a_student in self._student_service.repo.list:
            if a_student.id == '1234567':
                assert a_student.name == 'Johnutu Doe'
        with self.assertRaises(StudentException):
            self._student_service.update('123458', 'Johnutu Doe')

    def test_search_student_id(self):
        self._student_repository.add_student(Student('123456', 'Jane Doe'))
        self._student_repository.add_student(Student('123457', 'John Doe'))
        self._student_repository.add_student(Student('123458', 'Johnny Bravo'))
        test_search_list = self._student_service.search_student_id('123456')
        assert len(test_search_list) == 1
        test_search_list = self._student_service.search_student_id('123')
        assert len(test_search_list) == 3
        with self.assertRaises(StudentException):
            test_search_list = self._student_service.search_student_id('1234567')

    def test_search_student_name(self):
        self._student_repository.add_student(Student('123456', 'Jane Doe'))
        self._student_repository.add_student(Student('123457', 'John Doe'))
        self._student_repository.add_student(Student('123458', 'Johnny Bravo'))
        test_search_list = self._student_service.search_student_name('Jane')
        assert len(test_search_list) == 1
        test_search_list = self._student_service.search_student_name('John')
        assert len(test_search_list) == 2
        with self.assertRaises(StudentException):
            test_search_list = self._student_service.search_student_name('Nicu')


class TestServiceDisciplineMethods(unittest.TestCase):
    def setUp(self):
        self._discipline_validator = DisciplineValidator()
        self._discipline_repository = DisciplineRepository()
        self._undo_redo_service = UndoRedoService()
        self._discipline_service = ServiceDisciplines(self._discipline_repository, self._discipline_validator,
                                                      self._undo_redo_service)

    def test_instance(self):
        self.assertIsInstance(self._discipline_service, ServiceDisciplines)

    def test_add_to_repo(self):
        assert len(self._discipline_service.repo.list) == 0
        self._discipline_service.add_to_repo('12345', 'Algebra')
        assert len(self._discipline_service.repo.list) == 1
        self._discipline_service.add_to_repo('12346', 'Geometry')
        assert len(self._discipline_service.repo.list) == 2
        with self.assertRaises(DisciplineException):
            self._discipline_service.add_to_repo('12345', 'Algebraa')

    def test_remove_discipline(self):
        self._discipline_service.add_to_repo('12345', 'Algebra')
        self._discipline_service.add_to_repo('12346', 'Geometry')
        self._discipline_service.remove_from_repo('12345')
        assert len(self._discipline_service.repo.list) == 1
        with self.assertRaises(DisciplineException):
            self._discipline_service.remove_from_repo('12345')

    def test_update_discipline(self):
        self._discipline_service.add_to_repo('12345', 'Algebra')
        self._discipline_service.add_to_repo('12346', 'Geometry')
        with self.assertRaises(DisciplineException):
            self._discipline_service.update('12347', 'Paranghelia')
        self._discipline_service.update('12345', 'Fundamentals of programming')
        for a_discipline in self._discipline_service.repo.list:
            if a_discipline.id == '12345':
                assert a_discipline.name == 'Fundamentals of programming'

    def test_search_discipline_id(self):
        self._discipline_repository.add_discipline(Discipline('12345', 'FP'))
        self._discipline_repository.add_discipline(Discipline('12346', 'MuSiC'))
        self._discipline_repository.add_discipline(Discipline('12347', 'ReLiGiOn'))
        test_search_list = self._discipline_service.search_discipline_id('12345')
        assert len(test_search_list) == 1
        test_search_list = self._discipline_service.search_discipline_id('123')
        assert len(test_search_list) == 3
        with self.assertRaises(DisciplineException):
            test_search_list = self._discipline_service.search_discipline_id('78')

    def test_search_discipline_name(self):
        self._discipline_repository.add_discipline(Discipline('12345', 'FP'))
        self._discipline_repository.add_discipline(Discipline('12346', 'FP GODS'))
        self._discipline_repository.add_discipline(Discipline('12347', 'ReLiGiOn'))
        test_search_list = self._discipline_service.search_discipline_name('Re')
        assert len(test_search_list) == 1
        test_search_list = self._discipline_service.search_discipline_name('FP')
        assert len(test_search_list) == 2
        with self.assertRaises(DisciplineException):
            test_search_list = self._discipline_service.search_discipline_name('Fundamentals of programming')


class TestServiceGradeMethods(unittest.TestCase):
    def setUp(self):
        self._grade_validator = GradeValidator()
        self._grade_repository = GradeRepository()
        self._undo_redo_service = UndoRedoService()
        self._grade_service = ServiceGrades(self._grade_repository, self._grade_validator, self._undo_redo_service)

    def test_instance(self):
        self.assertIsInstance(self._grade_service, ServiceGrades)

    def test_add_to_repo(self):
        assert len(self._grade_service.repo.list) == 0
        self._grade_service.add_to_repo('123456', '12345', '10')
        assert len(self._grade_service.repo.list) == 1
        self._grade_service.add_to_repo('123457', '12346', '5')
        assert len(self._grade_service.repo.list) == 2
        with self.assertRaises(GradeException):
            self._grade_service.add_to_repo('123456', '12345', '-1')
        with self.assertRaises(GradeException):
            self._grade_service.add_to_repo('1236', '12345', '1')
        with self.assertRaises(GradeException):
            self._grade_service.add_to_repo('123476', '12345', 'a')
        with self.assertRaises(GradeException):
            self._grade_service.add_to_repo('123476', '12345', '11')
        with self.assertRaises(GradeException):
            self._grade_service.add_to_repo('123456', '1345', '7')


class TestServiceStatisticMethods(unittest.TestCase):
    def setUp(self):
        self._statistic_repository = StatisticRepository()
        self._student_repository = StudentRepository()
        self._discipline_repository = DisciplineRepository()
        self._grade_repository = GradeRepository()
        self._ServiceStatistic = ServiceStatistic(self._statistic_repository, self._student_repository,
                                                  self._discipline_repository, self._grade_repository)

    def test_instance(self):
        self.assertIsInstance(self._ServiceStatistic, ServiceStatistic)

    def test_calculate_student_average_grade_discipline(self):
        self._grade_repository.add_grade(Grade('123456', '12345', '10'))
        self._grade_repository.add_grade(Grade('123457', '12346', '5'))
        self._grade_repository.add_grade(Grade('123457', '12346', '10'))
        self._grade_repository.add_grade(Grade('123457', '12345', '10'))
        self._discipline_repository.add_discipline(Discipline('12346', 'Test'))
        self._discipline_repository.add_discipline(Discipline('12345', 'Testing'))
        self._discipline_repository.add_discipline(Discipline('12347', 'Testul'))
        average_test = self._ServiceStatistic.calculate_student_average_grade_discipline('123457', '12346')
        assert average_test == 7.5
        average_test = self._ServiceStatistic.calculate_student_average_grade_discipline('123456', '12347')
        assert average_test == 0

    def test_add_failing_student_statistic(self):
        self._student_repository.add_student(Student('123456', 'Jane Doe'))
        self._discipline_repository.add_discipline(Discipline('12345', 'Test'))
        self._grade_repository.add_grade(Grade('123456', '12345', '3'))
        self._ServiceStatistic.add_failing_student_statistic()
        assert len(self._ServiceStatistic.repo.list) == 1

    def test_calculate_student_average_grade(self):
        self._student_repository.add_student(Student('123456', 'Jane Doe'))
        self._student_repository.add_student(Student('123466', 'John Doe'))
        self._discipline_repository.add_discipline(Discipline('12345', 'Nothing'))
        self._discipline_repository.add_discipline(Discipline('12346', 'Nothingness'))
        self._grade_repository.add_grade(Grade('123456', '12345', '10'))
        self._grade_repository.add_grade(Grade('123456', '12346', '8'))
        testing_dictionary = self._ServiceStatistic.calculate_student_average_grade('123456')
        assert testing_dictionary['average_grade'] == 9
        testing_dictionary = self._ServiceStatistic.calculate_student_average_grade('123466')
        assert testing_dictionary['average_grade'] == 0

    def test_calculate_discipline_average_grade(self):
        self._student_repository.add_student(Student('123456', 'John Doe'))
        self._student_repository.add_student(Student('123466', 'Jane Doe'))
        self._discipline_repository.add_discipline(Discipline('12345', 'Nothing'))
        self._discipline_repository.add_discipline(Discipline('12346', 'Nothingness'))
        self._grade_repository.add_grade(Grade('123456', '12345', '10'))
        self._grade_repository.add_grade(Grade('123466', '12345', '8'))
        testing_dictionary = self._ServiceStatistic.calculate_discipline_average_grade('12345')
        assert testing_dictionary['average_grade'] == 9
        testing_dictionary = self._ServiceStatistic.calculate_discipline_average_grade('12346')
        assert testing_dictionary['average_grade'] == 0

    def test_create_best_student_statistic(self):
        self._student_repository.add_student(Student('123456', 'Jane Doe'))
        self._student_repository.add_student(Student('123457', 'John Doe'))
        self._student_repository.add_student(Student('123458', 'Jojo Doe'))
        self._student_repository.add_student(Student('123459', 'Johanna Doe'))
        self._discipline_repository.add_discipline(Discipline('12345', 'Test'))
        self._discipline_repository.add_discipline(Discipline('12346', 'Testing'))
        self._discipline_repository.add_discipline(Discipline('12347', 'Tested'))
        self._grade_repository.add_grade(Grade('123456', '12345', '10'))
        self._grade_repository.add_grade(Grade('123456', '12346', '10'))
        self._grade_repository.add_grade(Grade('123456', '12347', '10'))
        self._grade_repository.add_grade(Grade('123457', '12345', '6'))
        self._grade_repository.add_grade(Grade('123457', '12347', '7'))
        self._grade_repository.add_grade(Grade('123458', '12345', '2'))
        self._ServiceStatistic.create_best_students_statistic()
        assert len(self._ServiceStatistic.repo.list) == 4
        assert self._ServiceStatistic.repo.list[0]['average_grade'] == 10

    def test_create_best_discipline_statistic(self):
        self._student_repository.add_student(Student('123456', 'Jane Doe'))
        self._student_repository.add_student(Student('123457', 'John Doe'))
        self._student_repository.add_student(Student('123458', 'Jojo Doe'))
        self._student_repository.add_student(Student('123459', 'Johanna Doe'))
        self._discipline_repository.add_discipline(Discipline('12345', 'Tested'))
        self._discipline_repository.add_discipline(Discipline('12346', 'Test'))
        self._discipline_repository.add_discipline(Discipline('12347', 'Testing'))
        self._discipline_repository.add_discipline(Discipline('12348', 'Tester'))
        self._grade_repository.add_grade(Grade('123456', '12345', '7'))
        self._grade_repository.add_grade(Grade('123456', '12346', '2'))
        self._grade_repository.add_grade(Grade('123456', '12347', '9'))
        self._grade_repository.add_grade(Grade('123457', '12345', '5'))
        self._grade_repository.add_grade(Grade('123457', '12347', '7'))
        self._grade_repository.add_grade(Grade('123458', '12345', '7'))
        self._ServiceStatistic.create_best_disciplines_statistic()
        assert len(self._ServiceStatistic.repo.list) == 4
        assert self._ServiceStatistic.repo.list[0]['average_grade'] == 8


class TestUndoRedoMethods(unittest.TestCase):
    def setUp(self):
        self._undo_redo_service = UndoRedoService()
        self._student_validator = StudentValidator()
        self._student_repository = StudentRepository()
        self._undo_redo_service = UndoRedoService()
        self._student_service = ServiceStudents(self._student_repository, self._student_validator,
                                                self._undo_redo_service)

    def test_instance(self):
        self.assertIsInstance(self._undo_redo_service, UndoRedoService)

    def test_record(self):
        assert len(self._undo_redo_service._history_list) == 0
        assert self._undo_redo_service._index == -1
        assert self._undo_redo_service._undo_redo is True
        self._undo_redo_service.false()
        assert self._undo_redo_service._undo_redo is False
        self._student_service.add_to_repo('123456', 'Test name')
        function_undo = FunctionCall(self._student_service.remove_from_repo, '123456')
        function_redo = FunctionCall(self._student_service.add_to_repo, '123456', 'Test name')
        self._undo_redo_service.record(Operation(function_undo, function_redo))
        assert len(self._undo_redo_service._history_list) == 1
        assert self._undo_redo_service._undo_redo is True
        self._undo_redo_service.record(Operation(function_undo, function_redo))
        assert len(self._undo_redo_service._history_list) == 2
        assert self._undo_redo_service._index == 1
        assert self._undo_redo_service._undo_redo is True

    def test_undo_redo(self):
        with self.assertRaises(UndoRedoException):
            self._undo_redo_service.undo()
        self._student_service.add_to_repo('123456', 'Test name')
        function_undo = FunctionCall(self._student_service.remove_from_repo, '123456')
        function_redo = FunctionCall(self._student_service.add_to_repo, '123456', 'Test name')
        self._undo_redo_service.record(Operation(function_undo, function_redo))
        with self.assertRaises(UndoRedoException):
            self._undo_redo_service.redo()
        self._undo_redo_service.false()
        self._undo_redo_service.undo()
        self._undo_redo_service.false()
        self._undo_redo_service.redo()
