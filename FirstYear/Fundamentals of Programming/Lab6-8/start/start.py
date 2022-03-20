from console.console import Console
from console.GUI import GUI
from domain.entities import StudentValidator, DisciplineValidator, GradeValidator
from functionalities.functionalities import ServiceStudents, ServiceDisciplines, ServiceGrades, ServiceStatistic, \
    UndoRedoService
from repositories.repository import test_init_discipline, test_init_students, test_init_grades, StatisticRepository

if __name__ == '__main__':
    student_validator = StudentValidator()
    discipline_validator = DisciplineValidator()
    grade_validator = GradeValidator()
    student_repository = test_init_students()
    discipline_repository = test_init_discipline()
    grade_repository = test_init_grades(student_repository, discipline_repository)
    undo_redo_service = UndoRedoService()
    student_service = ServiceStudents(student_repository, student_validator, undo_redo_service)
    discipline_service = ServiceDisciplines(discipline_repository, discipline_validator, undo_redo_service)
    grade_service = ServiceGrades(grade_repository, grade_validator, undo_redo_service)
    statistic_service = ServiceStatistic(StatisticRepository(), student_repository, discipline_repository,
                                         grade_repository)
    gui = GUI(student_service, discipline_service, grade_service, statistic_service, undo_redo_service)
    gui.run_GUI()
    #console = Console(student_service, discipline_service, grade_service, statistic_service, undo_redo_service)
    #console.start_console()
