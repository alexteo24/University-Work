class ConsoleException(Exception):
    def __init__(self, message):
        self._message = message


def print_commands():
    print("Please choose one of the following commands:")
    print("1.1 Add new student")  # done
    print("1.2 Add new discipline")  # done
    print("1.3 Grade student")  # done
    print("2.1 Remove student")  # done
    print("2.2 Remove a discipline")  # done
    print("3.1 Update student")  # done
    print("3.2 Update discipline")
    print("4.1 List students")  # done
    print("4.2 List disciplines")  # done
    print("4.3 List grades")  # done
    print("5.1 Search student/s")
    print("5.2 Search discipline/s")
    print("6.1 Create failing students statistic")
    print("6.2 Create best students statistic")
    print("6.3 Create best discipline statistic")
    print("7. Undo last operation")
    print("8. Redo last operation")
    print("0. Exit")  # done


def add_student_ui(student_service):
    """
    This function adds a new student to the student list
    :param student_service: The service containing the student repo
    :return:
    """
    student_id = input('Please enter the student ID:')
    student_name = input('Please enter the student name:')
    student_service.add_to_repo(student_id, student_name)


def add_discipline_ui(discipline_service):
    """
    This function adds a new discipline to the discipline list
    :param discipline_service: The service containing the discipline repo
    :return:
    """
    discipline_id = input('Please enter the discipline ID:')
    discipline_name = input('Please enter the discipline name:')
    discipline_service.add_to_repo(discipline_id, discipline_name)


def add_grade_ui(grade_service, student_id, discipline_id, grade_value):
    """
    This function adds a new grade to the list of grades
    :param grade_service: The service containing the grade repo
    :param student_id: The ID of the student associated with the grade
    :param discipline_id: The ID of the discipline associated with the grade
    :param grade_value: The value of the grade
    :return:
    """
    grade_service.add_to_repo(student_id, discipline_id, grade_value)


def list_ui(student_or_discipline_or_grade_repository):
    """
    This function will list the contents of some_repository
    :param student_or_discipline_or_grade_repository: The repository which contains the data to be displayed
         (some_repository can be one of the following (student_repository, discipline_repository, grade_repository)
    :return:
    """
    for student_or_discipline_or_grade in student_or_discipline_or_grade_repository.list:
        print(student_or_discipline_or_grade)


def remove_ui(students_or_discipline_service, grade_service):
    """
    This function is responsible for the removals of elements from students_or_discipline_service
    :param students_or_discipline_service: Can be either student_service or discipline_service and contains the repo
    from which elements will be removed
    :param grade_service: The grade service which has the repo from which all the occurrences of the removed_id will be
        removed
    :return:
    """
    student_or_discipline_id = input("Please enter the ID you want to remove (len(ID) = 5/6 => "
                                     "remove discipline/student):")
    students_or_discipline_service.remove_from_repo(student_or_discipline_id)
    try:
        grade_service.repo.remove_grade_discipline(student_or_discipline_id)
    except ConsoleException:
        grade_service.repo.remove_grade_student(student_or_discipline_id)


def update_student_or_discipline_ui(students_or_discipline_service):
    """
    This function is responsible for the updates of elements from students_or_discipline_service
    :param students_or_discipline_service: Can be either student_service or discipline_service and contains the repo
        containing the element to be updated (student or discipline)
    :return:
    """
    student_or_discipline_id = input("Please enter the ID you want to update (len(ID) = 5/6 "
                                     "=> update discipline/student):")
    new_name_student_or_discipline = input("Please enter the new name associated with the ID:")
    students_or_discipline_service.update(student_or_discipline_id, new_name_student_or_discipline)


def check_if_in_repo(student_or_discipline_repository, id_to_search):
    """
    This functions check if the id = id_to_search is in student_or_grade_repository
    :param student_or_discipline_repository: Can be either student_repo or discipline_repo and contains either all
        students or all disciplines
    :param id_to_search: Can be either a student_id or a discipline_id
    :return: True if id_to_search was found in either student_repo or discipline_repo; False otherwise
    """
    if len(id_to_search) == 6:
        for student in student_or_discipline_repository:
            if student.id == id_to_search:
                return True
    elif len(id_to_search) == 5:
        for discipline in student_or_discipline_repository:
            if discipline.id == id_to_search:
                return True
    return False


def search_student_ui(student_service, student_name_or_id):
    """
    This function is responsible for displaying the results of the search for a student based on student_name_or_id in
        the student_repository
    :param student_service: The repository containing the data about all students
    :param student_name_or_id: The name or id based on which the search will be performed
    :return:
    """
    if student_name_or_id.isdigit():
        search_result = student_service.search_student_id(student_name_or_id)
    else:
        copy_student_name = student_name_or_id
        copy_student_name = copy_student_name.replace(" ", '')
        if copy_student_name.isalpha():
            search_result = student_service.search_student_name(student_name_or_id)
        else:
            raise ConsoleException('Invalid input data (name/id)!')
    for a_student in search_result:
        print(a_student)


def search_discipline_ui(discipline_service, discipline_name_or_id):
    """
    This function is responsible for displaying the results of the search for a discipline based on
        discipline_name_or_id in the discipline_repository
    :param discipline_service: The repository containing the data about all disciplines
    :param discipline_name_or_id: The name or id based on which the search will be performed
    :return:
    """
    if discipline_name_or_id.isdigit():
        search_result = discipline_service.search_discipline_id(discipline_name_or_id)
    else:
        copy_discipline_name = discipline_name_or_id
        copy_discipline_name = copy_discipline_name.replace(" ", '')
        if copy_discipline_name.isalpha():
            search_result = discipline_service.search_discipline_name(discipline_name_or_id)
        else:
            raise ConsoleException('Invalid input data(name/id)!')
    for a_discipline in search_result:
        print(a_discipline)


def statistic_failing_students_ui(statistic_service):
    """
    This function is responsible for displaying the list of all failing students, and clearing statistic list afterwards
    :param statistic_service: The service responsible for managing the statistics
    :return:
    """
    statistic_service.add_failing_student_statistic()
    if len(statistic_service.repo.list) == 0:
        print("There are no failing students!!!")
    else:
        print("The list of failing students:\n")
    for a_student in statistic_service.repo.list:
        print(a_student)
    print('\n')
    statistic_service.repo.clear_statistic()


def statistic_best_students_ui(statistic_service):
    """
    This function is responsible for displaying the list of all students in descending order based on their average
        grade at all disciplines, and clearing statistic list afterwards
    :param statistic_service: The service responsible for managing the statistics
    :return:
    """
    statistic_service.create_best_students_statistic()
    print("This is the list of students in descending order of their average grade:")
    print('\n')
    for a_student_and_average_grade in statistic_service.repo.list:
        print("The student having the id", a_student_and_average_grade['Student id'], "has the average grade",
              a_student_and_average_grade['average_grade'])
    print('\n')
    statistic_service.repo.clear_statistic()


def statistic_best_disciplines_ui(statistic_service):
    """
    This function is responsible for displaying the list of all disciplines in descending order based on the average
        grade of all graded students, and clearing statistic list afterwards
    :param statistic_service: The service responsible for managing the statistics
    :return:
    """
    statistic_service.create_best_disciplines_statistic()
    print("This is the list of disciplines in descending order of the average grade:")
    print('\n')
    for a_discipline_and_average_grade in statistic_service.repo.list:
        print("The discipline having the id", a_discipline_and_average_grade['Discipline id'], "has the average grade",
              a_discipline_and_average_grade['average_grade'])
    print('\n')
    statistic_service.repo.clear_statistic()


class Console:
    def __init__(self, service_student, service_discipline, service_grade, statistic_service, undo_redo_service):
        self._ServiceStudent = service_student
        self._ServiceDiscipline = service_discipline
        self._ServiceGrade = service_grade
        self._ServiceStatistic = statistic_service
        self._UndoRedoService = undo_redo_service

    def start_console(self):
        are_we_done_yet = False
        while not are_we_done_yet:
            try:
                print_commands()
                user_command = input('Enter your command:')
                if user_command == '0':
                    are_we_done_yet = True
                    print("Bye bye!")
                elif user_command == "1.1":
                    add_student_ui(self._ServiceStudent)
                elif user_command == "1.2":
                    add_discipline_ui(self._ServiceDiscipline)
                elif user_command == "1.3":
                    student_id = input('Please enter the student ID associated with the grade:')
                    discipline_id = input('Please enter the discipline ID associated with the grade:')
                    grade_value = input('Please enter the grade:')
                    copy_user_input = student_id+' '+discipline_id+' '+grade_value
                    id_check, something = copy_user_input.split(' ', 1)
                    check = False
                    if len(id_check) == 6:
                        check = check_if_in_repo(self._ServiceStudent.repo.list, id_check)
                    if not check:
                        raise ConsoleException('The student or the discipline does not exist!')
                    if len(id_check) == 5:
                        check = check_if_in_repo(self._ServiceDiscipline.repo.list, id_check)
                    if check:
                        add_grade_ui(self._ServiceGrade, student_id, discipline_id, grade_value)
                    else:
                        raise ConsoleException('The student or the discipline does not exist!')
                elif user_command == "2.1":
                    remove_ui(self._ServiceStudent, self._ServiceGrade)
                elif user_command == "2.2":
                    remove_ui(self._ServiceDiscipline, self._ServiceGrade)
                elif user_command == "3.1":
                    update_student_or_discipline_ui(self._ServiceStudent)
                elif user_command == "3.2":
                    update_student_or_discipline_ui(self._ServiceDiscipline)
                elif user_command == "4.1":
                    list_ui(self._ServiceStudent.repo)
                elif user_command == "4.2":
                    list_ui(self._ServiceDiscipline.repo)
                elif user_command == "4.3":
                    list_ui(self._ServiceGrade.repo)
                elif user_command == "5.1":
                    print("How do you wanna search the student?")
                    print("1. By student id")
                    print("2. By name")
                    user_command = input("Please enter your command:")
                    if user_command == "1":
                        student_id = input("Please enter the student's id/part of it:")
                        search_student_ui(self._ServiceStudent, student_id)
                    elif user_command == "2":
                        student_name = input("Please enter the student's name/part of it:")
                        search_student_ui(self._ServiceStudent, student_name)
                    else:
                        print("Invalid command!")
                elif user_command == "5.2":
                    print("How do you wanna search the discipline?")
                    print("1. By discipline id")
                    print("2. By name")
                    user_command = input("Please enter your command:")
                    if user_command == "1":
                        discipline_id = input("Please enter the discipline's id/part of it:")
                        search_discipline_ui(self._ServiceDiscipline, discipline_id)
                    elif user_command == "2":
                        discipline_name = input("Please enter the discipline's name/part of it:")
                        search_discipline_ui(self._ServiceDiscipline, discipline_name)
                    else:
                        print("Invalid command!")
                elif user_command == "6.1":
                    statistic_failing_students_ui(self._ServiceStatistic)
                elif user_command == "6.2":
                    statistic_best_students_ui(self._ServiceStatistic)
                elif user_command == "6.3":
                    statistic_best_disciplines_ui(self._ServiceStatistic)
                elif user_command == "7":
                    self._UndoRedoService.false()
                    self._UndoRedoService.undo()
                elif user_command == "8":
                    self._UndoRedoService.false()
                    self._UndoRedoService.redo()
                else:
                    print("Invalid command!")
            except Exception as ex:
                print(ex)
