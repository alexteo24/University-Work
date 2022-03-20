from domain.entities import Student, Discipline, Grade, StudentException, DisciplineException


class StatisticException(Exception):
    def __init__(self, message):
        self._message = message


class ServiceStudents:
    def __init__(self, student_repository=None, student_validator=None, undo_redo_service=None):
        self._student_validator = student_validator
        self._student_repository = student_repository
        self._undo_redo_service = undo_redo_service

    def add_to_repo(self, student_id=None, student_name=None):
        """
        This method executes the addition to the student_repo of the student having the data student_id, student_name
        :param student_id: The id of the student to be added
        :param student_name: The name of the student to be added
        :return:
        """
        new_student = Student(student_id, student_name)
        validator = self._student_validator.validate(new_student)
        self._student_repository.add_student(new_student)
        function_undo = FunctionCall(self.remove_from_repo, student_id)
        function_redo = FunctionCall(self.add_to_repo, student_id, student_name)
        self._undo_redo_service.record(Operation(function_undo, function_redo))

    def remove_from_repo(self, student_id=None):
        """
        This method executes the removal of the student having the student_id from the student_repo and also removes
            all of his grades from the grade_repo
        :param student_id: The id of the student to be removed
        :return:
        """
        deleted_student = self._student_repository.remove_student(student_id)
        function_undo = FunctionCall(self.add_to_repo, student_id, deleted_student.name)
        function_redo = FunctionCall(self.remove_from_repo, student_id)
        self._undo_redo_service.record(Operation(function_undo, function_redo))

    def update(self, student_id=None, new_student_name=None):
        """
        This method executes the update of the student having the ID = student_id by updating his name with
            new_student_name
        :param student_id: The id of the student to be update
        :param new_student_name: The name which will replace the already existing student_name
        :return:
        """
        updated_student = Student(student_id, new_student_name)
        validator = self._student_validator.validate(updated_student)
        old_student_data = self._student_repository.update_student(updated_student)
        function_undo = FunctionCall(self.update, student_id, old_student_data.name)
        function_redo = FunctionCall(self.update, student_id, new_student_name)
        self._undo_redo_service.record(Operation(function_undo, function_redo))

    def search_student_id(self, full_or_part_of_id):
        """
        This method searches for students which contain in their id full_or_part_of_id
        :param full_or_part_of_id: Can be either the full id or just a substring from it
        :return: The list of all students which have full_or_part_of_id inside their id
        """
        search_result = []
        for a_student in self._student_repository.list:
            if full_or_part_of_id in a_student.id:
                search_result.append(a_student)
        if len(search_result) == 0:
            raise StudentException('No matches found!')
        else:
            return search_result

    def search_student_name(self, full_or_part_of_name):
        """
        This method searches for students which contain in their name full_or_part_of_name
        :param full_or_part_of_name: Can be either the full name of the student or just a substring from it
            (CASE SENSITIVE)
        :return: The list of all students which have full_or_part_of_name inside their name
        """
        search_result = []
        for a_student in self._student_repository.list:
            if full_or_part_of_name in a_student.name:
                search_result.append(a_student)
        if len(search_result) == 0:
            raise StudentException('No matches found!')
        else:
            return search_result

    @property
    def repo(self):
        return self._student_repository


class ServiceDisciplines:
    def __init__(self, discipline_repository=None, discipline_validator=None, undo_redo_service=None):
        self._discipline_repository = discipline_repository
        self._discipline_validator = discipline_validator
        self._undo_redo_service = undo_redo_service

    def add_to_repo(self, discipline_id=None, discipline_name=None):
        """
        This method executes the addition to the discipline_repo of the discipline having the data discipline_id,
            discipline_name
        :param discipline_id: The id of the discipline to be added
        :param discipline_name: The name of the discipline to be added
        :return:
        """
        new_discipline = Discipline(discipline_id, discipline_name)
        validator = self._discipline_validator.validate(new_discipline)
        self._discipline_repository.add_discipline(new_discipline)
        function_undo = FunctionCall(self.remove_from_repo, discipline_id)
        function_redo = FunctionCall(self.add_to_repo, discipline_id, discipline_name)
        self._undo_redo_service.record(Operation(function_undo, function_redo))

    def remove_from_repo(self, discipline_id=None):
        """
        This method executes the removal of the discipline having the discipline_id from the discipline_repo and also
        removes all the students' grades on this discipline
        :param discipline_id: The id of the discipline to be removed
        :return:
        """
        deleted_discipline = self._discipline_repository.remove_discipline(discipline_id)
        function_undo = FunctionCall(self.add_to_repo, discipline_id, deleted_discipline.name)
        function_redo = FunctionCall(self.remove_from_repo, discipline_id)
        self._undo_redo_service.record(Operation(function_undo, function_redo))

    def update(self, discipline_id=None, new_discipline_name=None):
        """
        This method executes the update of the discipline having the ID = discipline_id by updating his name with
            new_discipline_name
        :param discipline_id: The id of the discipline to be updated
        :param new_discipline_name: The name which will replace the already existing discipline_name
        :return:
        """
        updated_discipline = Discipline(discipline_id, new_discipline_name)
        validator = self._discipline_validator.validate(updated_discipline)
        old_discipline_data = self._discipline_repository.update_discipline(updated_discipline)
        function_undo = FunctionCall(self.update, discipline_id, old_discipline_data.name)
        function_redo = FunctionCall(self.update, discipline_id, new_discipline_name)
        self._undo_redo_service.record(Operation(function_undo, function_redo))

    def search_discipline_id(self, full_or_part_of_id):
        """
        This method searches for disciplines which contain in their id full_or_part_of_id
        :param full_or_part_of_id: Can be either the full id of the discipline or just a substring from it
        :return: The list of the disciplines containing full_or_part_of_id in their ID
        """
        search_result = []
        for a_discipline in self._discipline_repository.list:
            if full_or_part_of_id in a_discipline.id:
                search_result.append(a_discipline)
        if len(search_result) == 0:
            raise DisciplineException('No matches found!')
        else:
            return search_result

    def search_discipline_name(self, full_or_part_of_name):
        """
        This method searcher fo disciplines which contain in their name full_or_part_of_name
        :param full_or_part_of_name: Can be either the full name of the discipline or just a substring from it
            (CASE SENSITIVE)
        :return: The list of the disciplines containing full_or_part_of_name in their name
        """
        search_result = []
        for a_discipline in self._discipline_repository.list:
            if full_or_part_of_name in a_discipline.name:
                search_result.append(a_discipline)
        if len(search_result) == 0:
            raise DisciplineException('No matches found!')
        else:
            return search_result

    @property
    def repo(self):
        return self._discipline_repository


class ServiceGrades:
    def __init__(self, grade_repository=None, grade_validator=None, undo_redo_service=None):
        self._grade_repository = grade_repository
        self._grade_validator = grade_validator
        self._undo_redo_service = undo_redo_service

    def add_to_repo(self, student_id=None, discipline_id=None, grade_value=None):
        """
        This method executes the addition to the grade_repo of the grade having the value grade_value, for the student
            having the id student_id at the discipline having the id discipline_id
        :param student_id: The id of the graded student
        :param discipline_id: The id of the discipline for which the grade was accorded
        :param grade_value: The value of the grade
        :return:
        """
        new_grade = Grade(student_id, discipline_id, grade_value)
        validator = self._grade_validator.validate(new_grade)
        self._grade_repository.add_grade(new_grade)
        function_undo = FunctionCall(self.remove_from_repo, new_grade)
        function_redo = FunctionCall(self.add_to_repo, student_id, discipline_id, grade_value)
        self._undo_redo_service.record(Operation(function_undo, function_redo))

    def remove_from_repo(self, grade):
        validator = self._grade_validator.validate(grade)
        self._grade_repository.remove_from_repo(grade)

    @property
    def repo(self):
        return self._grade_repository


class ServiceStatistic:
    def __init__(self, statistic_repository, student_repository, discipline_repository, grade_repository):
        self._statistic_repository = statistic_repository
        self._student_repository = student_repository
        self._discipline_repository = discipline_repository
        self._grade_repository = grade_repository

    def calculate_student_average_grade_discipline(self, student_id, discipline_id):
        """
        This method computes the average grade of the student having the id = student_id at the discipline having the
            id = discipline_id
        :param student_id: The id of the student whose average grade we want to compute
        :param discipline_id: The id of the discipline at which we want to compute the student's average grade
        :return: The average grade of the student or 0 if the student has no grades at the discipline having the
            id = discipline_id
        """
        search_result = self._grade_repository.search_grade_student_id(student_id)
        index = 0
        while index < len(search_result):
            a_grade = search_result[index]
            if a_grade.discipline_id != discipline_id:
                search_result.remove(a_grade)
            else:
                index += 1
        if len(search_result) == 0:
            return 0
        grades_sum = 0
        grades_number = 0
        for a_grade in search_result:
            grades_sum += int(a_grade.value)
            grades_number += 1
        return grades_sum/grades_number

    def add_failing_student_statistic(self):
        """
        This method adds to the statistic list (self._StatisticList) the students failing at least one of the
            disciplines
        :return:
        """
        for a_student in self._student_repository.list:
            for a_discipline in self._discipline_repository.list:
                average_grade_discipline = self.calculate_student_average_grade_discipline(a_student.id, a_discipline.id)
                if 0 < average_grade_discipline < 5:
                    self._statistic_repository.add_to_statistic(a_student)
                    break

    def calculate_student_average_grade(self, student_id):
        """
        This method computes the average grade of the student having the id = student_id at all of the disciplines he
            was graded at
        :param student_id: The id of the student whose average grade we want to compute
        :return: A dictionary in the form {'Student id': student_id, 'average_grade': average_grade} containing the
            id of the student and the average_grade ( which will be 0 if the students wasn't graded at all)
        """
        grades_sum = 0
        grades_number = 0
        for a_discipline in self._discipline_repository.list:
            average_grade_at_discipline = self.calculate_student_average_grade_discipline(student_id, a_discipline.id)
            if average_grade_at_discipline != 0:
                grades_sum += average_grade_at_discipline
                grades_number += 1
        if grades_number != 0:
            average_grade = grades_sum/grades_number
            return {'Student id': student_id, 'average_grade': average_grade}
        else:
            return {'Student id': student_id, 'average_grade': 0}

    def calculate_discipline_average_grade(self, discipline_id):
        """
        This method computes the average grade at the discipline having the id = discipline_id of all the students that
            were graded at that discipline
        :param discipline_id: The discipline we want to compute the graded students average grade
        :return: A dictionary in the form of {'Discipline id': discipline_id, 'average_grade': average_grade}
            containing the id of the discipline and the average_grade ( which will be 0 if there were no grades recorded
            at that discipline)
        """
        grades_sum = 0
        grades_number = 0
        for a_student in self._student_repository.list:
            average_grade_of_student = self.calculate_student_average_grade_discipline(a_student.id, discipline_id)
            if average_grade_of_student != 0:
                grades_sum += average_grade_of_student
                grades_number += 1
        if grades_number != 0:
            average_grade = grades_sum/grades_number
            return {'Discipline id': discipline_id, 'average_grade': average_grade}
        else:
            return {'Discipline id': discipline_id, 'average_grade': 0}

    def create_best_students_statistic(self):
        """
        This method adds and orders, at the same time, all the students, in descending order of their average grade at
            all disciplines. The ones that are not graded, will be at the end of the list, having the average_grade = 0
        :return:
        """
        for a_student in self._student_repository.list:
            average_student_grade_dictionary = self.calculate_student_average_grade(a_student.id)
            if len(self._statistic_repository.list) == 0:
                self._statistic_repository.add_to_statistic(average_student_grade_dictionary)
            else:
                index = 0
                average_grade_of_existing_student = self._statistic_repository.list[index]['average_grade']
                average_grade_of_new_student = average_student_grade_dictionary['average_grade']
                while int(average_grade_of_new_student) < int(average_grade_of_existing_student) and index < len(self._statistic_repository.list):
                    index += 1
                    if index < len(self._statistic_repository.list):
                        average_grade_of_existing_student = self._statistic_repository.list[index]['average_grade']
                self._statistic_repository.list.insert(index, average_student_grade_dictionary)

    def create_best_disciplines_statistic(self):
        """
        This method adds and orders, at the same time, all the discipline, in descending order of the average grade of
            all the graded students at this disciplines. If there are no grades recorded, the discipline will be at the
            end of the list having the average_grade = 0
        :return:
        """
        for a_discipline in self._discipline_repository.list:
            average_discipline_grade_dictionary = self.calculate_discipline_average_grade(a_discipline.id)
            if len(self._statistic_repository.list) == 0:
                self._statistic_repository.add_to_statistic(average_discipline_grade_dictionary)
            else:
                index = 0
                average_grade_of_new_discipline = average_discipline_grade_dictionary['average_grade']
                average_grade_of_existing_discipline = self._statistic_repository.list[index]['average_grade']
                while int(average_grade_of_existing_discipline) > int(average_grade_of_new_discipline) and index < len(self._statistic_repository.list):
                    index += 1
                    if index < len(self._statistic_repository.list):
                        average_grade_of_existing_discipline = self._statistic_repository.list[index]['average_grade']
                self._statistic_repository.list.insert(index, average_discipline_grade_dictionary)

    @property
    def repo(self):
        return self._statistic_repository


class UndoRedoException(Exception):
    def __init__(self, message):
        self._message = message


class UndoRedoService:
    def __init__(self):
        self._history_list = []
        self._index = -1
        self._undo_redo = True

    def record(self, operation):
        if self._undo_redo:
            self._history_list = self._history_list[0:self._index + 1]
            self._history_list.append(operation)
            self._index += 1
        else:
            self._undo_redo = True

    def undo(self):
        if self._index == -1:
            raise UndoRedoException("There are no operations to be undone!")
        operation = self._history_list[self._index]
        operation.undo()
        self._index -= 1

    def redo(self):
        if self._index + 1 == len(self._history_list):
            raise UndoRedoException("There are no operations to be redone!")
        self._index += 1
        operation = self._history_list[self._index]
        operation.redo()

    def false(self):
        self._undo_redo = False


class Operation:
    def __init__(self, function_undo, function_redo):
        self._function_undo = function_undo
        self._function_redo = function_redo

    def undo(self):
        self._function_undo()

    def redo(self):
        self._function_redo()


class FunctionCall:
    def __init__(self, function_name, *function_parameters):
        self._function_name = function_name
        self._function_parameters = function_parameters

    def call(self):
        self._function_name(*self._function_parameters)

    def __call__(self):
        self.call()