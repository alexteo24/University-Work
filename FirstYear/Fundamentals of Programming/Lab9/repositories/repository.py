from domain.entities import DisciplineException, StudentException, Student, Grade, Discipline, GradeException
from random import choice, randint
import names
import pickle


class RepositoryException(Exception):
    def __init__(self, message):
        self._message = message


class StudentRepository:
    def __init__(self, StudentList=None):
        if StudentList is None:
            self._StudentList = []
        else:
            self._StudentList = StudentList

    def add_student(self, new_student):
        """
        This method adds a new student (new_student) to the student repository(StudentsList)
        :param new_student: The data of the new student (ID, name)
        :return:
        """
        new_student_id = new_student.id
        for a_student in self._StudentList:
            a_student_id = a_student.id
            if a_student_id == new_student_id:
                raise StudentException('There already exists a student having this ID!')
        self._StudentList.append(new_student)

    def remove_student(self, student_id):
        """
        This method removes a student (based on his id = student_id) from the student repository(StudentsList)
        :param student_id: The id of the student to be removed
        :return:
        """
        any_removal_made = False
        for a_student in self._StudentList:
            a_student_id = a_student.id
            if a_student_id == student_id:
                any_removal_made = True
                a_student_copy = a_student
                self._StudentList.remove(a_student)
                return a_student_copy
        if not any_removal_made:
            raise StudentException('There was no student having this ID!')

    def update_student(self, updated_student):
        """
        This method updates a student's name based on his ID
        :param updated_student: The student with updated data (same ID, different name)
        :return:
        """
        updated_student_id = updated_student.id
        updated_student_name = updated_student.name
        updates_made = False
        for a_student in self._StudentList:
            if updated_student_id == a_student.id:
                updates_made = True
                a_student_copy = a_student
                index = self._StudentList.index(a_student)
                self._StudentList[index] = updated_student
                return a_student_copy
        if not updates_made:
            raise StudentException('No updates were made or no student having that ID was found!')

    @property
    def list(self):
        return self._StudentList

    def relist(self, lists):
        self._StudentList = lists


class StudentRepositoryFiles(StudentRepository):
    def __init__(self, file_name):
        super(StudentRepositoryFiles, self).__init__()
        self.__file_name = file_name
        self.create_text_file()
        self.__load_file()

    def create_text_file(self):
        try:
            file = open(self.__file_name, "x")
            file.close()
        except FileExistsError:
            pass

    def __load_file(self):
        try:
            file = open("students_repository.txt", 'r')
            line = file.readline().strip()
            while len(line) > 0:
                student_id, student_name = line.split(";")
                self._StudentList.append(Student(student_id, student_name))
                line = file.readline().strip()
        except Exception as ex:
            print(ex)

    def __save_file(self):
        try:
            file = open("students_repository.txt", 'w')
            for a_student in self._StudentList:
                student_string = a_student.id + ";" + a_student.name + "\n"
                file.write(student_string)
        except Exception as ex:
            print(ex)

    def add_student(self, student):
        added_student = super().add_student(student)
        self.__save_file()
        return added_student

    def remove_student(self, student_id):
        removed_student = super().remove_student(student_id)
        self.__save_file()
        return removed_student

    def update_student(self, updated_student):
        updated_student = super().update_student(updated_student)
        self.__save_file()
        return updated_student


class StudentRepositoryBinary(StudentRepository):

    def __init__(self, file_name):
        super(StudentRepositoryBinary, self).__init__()
        self.__file_name = file_name
        self.create_binary_file()
        self.__load_binary_file()

    def create_binary_file(self):
        try:
            file = open(self.__file_name, "x")
            file.close()
        except FileExistsError:
            pass

    def __save_binary_file(self):
        try:
            file = open(self.__file_name, 'wb')
            pickle.dump(self._StudentList, file)
            file.close()
        except Exception as e:
            print(e)

    def __load_binary_file(self):
        try:
            file = open(self.__file_name, "rb")
            self._StudentList = pickle.load(file)
        except IOError as ie:
            print(ie)
        except EOFError as eof:
            print(eof)

    def add_student(self, student):
        added_student = super().add_student(student)
        self.__save_binary_file()
        return added_student

    def remove_student(self, student_id):
        removed_student = super().remove_student(student_id)
        self.__save_binary_file()
        return removed_student

    def update_student(self, updated_student):
        updated_student = super().update_student(updated_student)
        self.__save_binary_file()
        return updated_student


class DisciplineRepository:
    def __init__(self, DisciplineList=None):
        if DisciplineList is None:
            self._DisciplineList = []
        else:
            self._DisciplineList = DisciplineList

    def add_discipline(self, new_discipline):
        """
        This method adds a new discipline (new_discipline) to the discipline repository(DisciplineList)
        :param new_discipline: The data of the new discipline (ID, name)
        :return:
        """
        new_discipline_id = new_discipline.id
        for a_discipline in self._DisciplineList:
            a_discipline_id = a_discipline.id
            if a_discipline_id == new_discipline_id:
                raise DisciplineException('There already exists a discipline having this ID!')
        self._DisciplineList.append(new_discipline)

    def remove_discipline(self, discipline_id):
        """
        This method removes a discipline (based on id = discipline_id) from the discipline repository(DisciplineList)
        :param discipline_id: The id of the discipline to be removed
        :return:
        """
        any_removal_made = False
        for a_discipline in self._DisciplineList:
            a_discipline_id = a_discipline.id
            if a_discipline_id == discipline_id:
                a_discipline_copy = a_discipline
                self._DisciplineList.remove(a_discipline)
                any_removal_made = True
                return a_discipline_copy
        if not any_removal_made:
            raise DisciplineException('There was no discipline having this ID!')

    def update_discipline(self, updated_discipline):
        """
        This method updates a discipline's name based on its ID
        :param updated_discipline: The discipline with updated data (same ID, different name)
        :return:
        """
        updated_discipline_id = updated_discipline.id
        updated_discipline_name = updated_discipline.name
        updates_made = False
        for a_discipline in self._DisciplineList:
            if updated_discipline_id == a_discipline.id:
                updates_made = True
                a_discipline_copy = a_discipline
                index = self._DisciplineList.index(a_discipline)
                self._DisciplineList[index] = updated_discipline
                return a_discipline_copy
        if not updates_made:
            raise DisciplineException('No updates were made or no discipline having that ID was found!')

    @property
    def list(self):
        return self._DisciplineList


class DisciplineRepositoryFiles(DisciplineRepository):
    def __init__(self, file_name):
        super(DisciplineRepositoryFiles, self).__init__()
        self.__file_name = file_name
        self.create_text_file()
        self.__load_file()

    def create_text_file(self):
        try:
            file = open(self.__file_name, "x")
            file.close()
        except FileExistsError:
            pass

    def __load_file(self):
        try:
            file = open(self.__file_name, 'r')
            line = file.readline().strip()
            while len(line) > 0:
                discipline_id, discipline_name = line.split(';')
                self._DisciplineList.append(Discipline(discipline_id, discipline_name))
                line = file.readline().strip()
        except Exception as ex:
            print(ex)

    def __save_file(self):
        try:
            file = open(self.__file_name, 'w')
            for a_discipline in self._DisciplineList:
                discipline_string = a_discipline.id + ";" + a_discipline.name + "\n"
                file.write(discipline_string)
        except Exception as ex:
            print(ex)

    def add_discipline(self, new_discipline):
        added_discipline = super().add_discipline(new_discipline)
        self.__save_file()
        return added_discipline

    def remove_discipline(self, discipline_id):
        removed_discipline = super().remove_discipline(discipline_id)
        self.__save_file()
        return removed_discipline

    def update_discipline(self, updated_discipline):
        updated_discipline = super().update_discipline(updated_discipline)
        self.__save_file()
        return updated_discipline


class DisciplineRepositoryBinary(DisciplineRepository):

    def __init__(self, file_name):
        super(DisciplineRepositoryBinary, self).__init__()
        self.__file_name = file_name
        self.create_binary_file()
        self.__load_binary_file()

    def create_binary_file(self):
        try:
            file = open(self.__file_name, "x")
            file.close()
        except FileExistsError:
            pass

    def __save_binary_file(self):
        try:
            file = open(self.__file_name, 'wb')
            pickle.dump(self._DisciplineList, file)
            file.close()
        except Exception as e:
            print(e)

    def __load_binary_file(self):
        try:
            file = open(self.__file_name, "rb")
            self._DisciplineList = pickle.load(file)
        except IOError as ie:
            print(ie)
        except EOFError as eof:
            print(eof)

    def add_discipline(self, new_discipline):
        added_discipline = super().add_discipline(new_discipline)
        self.__save_binary_file()
        return added_discipline

    def remove_discipline(self, discipline_id):
        removed_discipline = super().remove_discipline(discipline_id)
        self.__save_binary_file()
        return removed_discipline

    def update_discipline(self, updated_discipline):
        updated_discipline = super().update_discipline(updated_discipline)
        self.__save_binary_file()
        return updated_discipline


class GradeRepository:
    def __init__(self, GradeList=None):
        if GradeList is None:
            self._GradeList = []
        else:
            self._GradeList = GradeList

    def add_grade(self, grade):
        """
        This method adds a grade (stored in grade) to the grade repository (GradeList)
        :param grade: The grade to be added containing the required data (student_id, discipline_id, grade_value)
        :return:
        """
        self._GradeList.append(grade)

    def remove_grade_student(self, student_id):
        """
        Removes from the grade_repository (GradeList) all the grades having the student id = student_id
        :param student_id: The id of the students whose grades we want to remove
        :return:
        """
        removed_grades = []
        index = 0
        while index < len(self._GradeList):
            a_grade = self._GradeList[index]
            if a_grade.student_id == student_id:
                self._GradeList.remove(a_grade)
                removed_grades.append(a_grade)
            else:
                index += 1
        return removed_grades

    def remove_grade_discipline(self, discipline_id):
        """
        Removes from the grade_repository (GradeList) all the grades having the discipline id = discipline_id
        :param discipline_id: The id of the discipline to be removed
        :return:
        """
        removed_grades = []
        index = 0
        while index < len(self._GradeList):
            a_grade = self._GradeList[index]
            if a_grade.discipline_id == discipline_id:
                self._GradeList.remove(a_grade)
                removed_grades.append(a_grade)
            else:
                index += 1
        return removed_grades

    def remove_from_repo(self, grade):
        any_removal_made = False
        for a_grade in self._GradeList:
            if a_grade.student_id == grade.student_id and a_grade.discipline_id == grade.discipline_id and a_grade.value == grade.value:
                self._GradeList.remove(a_grade)
                any_removal_made = True
        if not any_removal_made:
            raise GradeException('No matches found!')

    @property
    def list(self):
        return self._GradeList


class GradeRepositoryFiles(GradeRepository):
    def __init__(self, file_name):
        super(GradeRepositoryFiles, self).__init__()
        self.__file_name = file_name
        self.create_text_file()
        self.__load_file()

    def create_text_file(self):
        try:
            file = open(self.__file_name, "x")
            file.close()
        except FileExistsError:
            pass

    def __load_file(self):
        try:
            file = open("grades_repository.txt", 'r')
            line = file.readline().strip()
            while len(line) > 0:
                grade_student_id, grade_discipline_id, grade_value = line.split(";")
                self._GradeList.append(Grade(grade_student_id, grade_discipline_id, grade_value))
                line = file.readline().strip()
        except Exception as ex:
            print(ex)

    def __save_file(self):
        try:
            file = open("grades_repository.txt", 'w')
            for a_grade in self._GradeList:
                grade_string = a_grade.student_id + ";" + a_grade.discipline_id + ";" + str(a_grade.value) + "\n"
                file.write(grade_string)
        except Exception as ex:
            print(ex)

    def add_grade(self, grade):
        added_grade = super().add_grade(grade)
        self.__save_file()
        return added_grade

    def remove_from_repo(self, grade):
        removed_grade = super().remove_from_repo(grade)
        self.__save_file()
        return removed_grade

    def remove_grade_discipline(self, discipline_id):
        removed_grades = super().remove_grade_discipline(discipline_id)
        self.__save_file()
        return removed_grades

    def remove_grade_student(self, student_id):
        removed_grades = super().remove_grade_student(student_id)
        self.__save_file()
        return removed_grades


class GradeRepositoryBinary(GradeRepository):

    def __init__(self, file_name):
        super(GradeRepositoryBinary, self).__init__()
        self.__file_name = file_name
        self.create_binary_file()
        self.__load_binary_file()

    def create_binary_file(self):
        try:
            file = open(self.__file_name, "x")
            file.close()
        except FileExistsError:
            pass

    def __save_binary_file(self):
        try:
            file = open(self.__file_name, 'wb')
            pickle.dump(self._GradeList, file)
            file.close()
        except Exception as e:
            print(e)

    def __load_binary_file(self):
        try:
            file = open(self.__file_name, "rb")
            self._GradeList = pickle.load(file)
        except IOError as ie:
            print(ie)
        except EOFError as eof:
            print(eof)

    def add_grade(self, grade):
        added_grade = super().add_grade(grade)
        self.__save_binary_file()
        return added_grade

    def remove_from_repo(self, grade):
        removed_grade = super().remove_from_repo(grade)
        self.__save_binary_file()
        return removed_grade

    def remove_grade_discipline(self, discipline_id):
        removed_grades = super().remove_grade_discipline(discipline_id)
        self.__save_binary_file()
        return removed_grades

    def remove_grade_student(self, student_id):
        removed_grades = super().remove_grade_student(student_id)
        self.__save_binary_file()
        return removed_grades


class StatisticRepository:
    def __init__(self):
        self._StatisticList = []

    def add_to_statistic(self, data_for_statistic):
        """
        This method data to the list for statistic (self._StatisticList)
        :param data_for_statistic: can be either a student object for failing student or a dictionary in the form of
            id (which can be either student or discipline id) and average grade
        :return:
        """
        self._StatisticList.append(data_for_statistic)

    def clear_statistic(self):
        del self._StatisticList[:]

    @property
    def list(self):
        return self._StatisticList


def test_init_students():
    student_repo = StudentRepository()
    for index in range(0, 10):
        check = True
        student_id = None
        while check:
            student_id = randint(100000, 1000000)
            student_id = str(student_id)
            check = False
            for a_student in student_repo.list:
                if student_id == a_student.id:
                    check = True
        if not check:
            student_name = names.get_full_name()
            student = Student(student_id, student_name)
            student_repo.add_student(student)
    return student_repo


def test_init_discipline():
    discipline_repo = DisciplineRepository()
    for index in range(0, 10):
        check = True
        discipline_id = None
        while check:
            check = False
            discipline_id = randint(10000, 100000)
            discipline_id = str(discipline_id)
            for a_discipline in discipline_repo.list:
                if discipline_id == a_discipline.id:
                    check = True
        if not check:
            check = True
            discipline_name = None
            while check:
                check = False
                discipline_name = choice(['Algebra', 'Geometry', 'Computer science', 'Fundamentals of programming',
                                          'Physical education', 'Economics', 'History', 'Geography', 'English',
                                          'Analysis', 'Algorithms', 'Artificial intelligence', 'Data structures',
                                          'Computer architecture', 'Computer graphics',
                                          'Computer security and reliability',
                                          'Operating systems', 'Parallel computing', 'Programming languages'])
                for a_discipline in discipline_repo.list:
                    if discipline_name == a_discipline.name:
                        check = True
            discipline = Discipline(discipline_id, discipline_name)
            discipline_repo.add_discipline(discipline)
    return discipline_repo


def test_init_grades(student_repo, discipline_repo):
    grades_repo = GradeRepository()
    for index in range(0, 10):
        student = choice(student_repo.list)
        student_id = student.id
        discipline = choice(discipline_repo.list)
        discipline_id = discipline.id
        grade_value = randint(1, 10)
        grade = Grade(student_id, discipline_id, grade_value)
        grades_repo.add_grade(grade)
    return grades_repo
