from console.console import Console
from jproperties import Properties
from console.GUI import GUI
from domain.entities import StudentValidator, DisciplineValidator, GradeValidator
from functionalities.functionalities import ServiceStudents, ServiceDisciplines, ServiceGrades, ServiceStatistic, \
    UndoRedoService
from repositories.repository import test_init_discipline, test_init_students, test_init_grades, StatisticRepository, \
    StudentRepositoryFiles, DisciplineRepositoryFiles, GradeRepositoryFiles, RepositoryException, \
    StudentRepositoryBinary, DisciplineRepositoryBinary, GradeRepositoryBinary


class Settings:

    def __init__(self, file):
        program_config = Properties()
        with open(file, 'rb') as config_file:
            program_config.load(config_file)
            self._repository = program_config['repository'].data
            self._student_repository = program_config['students'].data
            self._discipline_repository = program_config['disciplines'].data
            self._grade_repository = program_config['grades'].data
            self._ui = program_config['ui'].data

    @property
    def repository(self):
        return self._repository

    @property
    def ui(self):
        return self._ui

    @property
    def student_repository(self):
        return self._student_repository

    @property
    def discipline_repository(self):
        return self._discipline_repository

    @property
    def grade_repository(self):
        return self._grade_repository


if __name__ == '__main__':
    student_validator = StudentValidator()
    discipline_validator = DisciplineValidator()
    grade_validator = GradeValidator()
    settings = Settings("settings.properties")
    if settings.repository == "in_memory":
        student_repository = test_init_students()
        discipline_repository = test_init_discipline()
        grade_repository = test_init_grades(student_repository, discipline_repository)
    elif settings.repository == "text_files":
        try:
            student_repository = StudentRepositoryFiles(settings.student_repository)
            discipline_repository = DisciplineRepositoryFiles(settings.discipline_repository)
            grade_repository = GradeRepositoryFiles(settings.grade_repository)
        except RepositoryException as re:
            print(re)
    elif settings.repository == "binary_files":
        try:
            student_repository = StudentRepositoryBinary(settings.student_repository)
            discipline_repository = DisciplineRepositoryBinary(settings.discipline_repository)
            grade_repository = GradeRepositoryBinary(settings.grade_repository)
        except RepositoryException as re:
            print(re)
    else:
        print("Invalid repository type!")
        exit(0)
    undo_redo_service = UndoRedoService()
    student_service = ServiceStudents(student_repository, student_validator, undo_redo_service)
    discipline_service = ServiceDisciplines(discipline_repository, discipline_validator, undo_redo_service)
    grade_service = ServiceGrades(grade_repository, grade_validator, undo_redo_service)
    statistic_service = ServiceStatistic(StatisticRepository(), student_repository, discipline_repository,
                                         grade_repository, grade_service)
    if settings.ui == "ui":
        console = Console(student_service, discipline_service, grade_service, statistic_service, undo_redo_service)
        console.start_console()
    else:
        gui = GUI(student_service, discipline_service, grade_service, statistic_service, undo_redo_service)
        gui.run_GUI()
