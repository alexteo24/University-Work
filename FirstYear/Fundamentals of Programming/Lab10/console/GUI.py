from tkinter import *
from tkinter import messagebox

from domain.entities import StudentException, DisciplineException, GradeException
from functionalities.functionalities import UndoRedoException


class GUI:
    def __init__(self, students_service, disciplines_service, grades_service, statistics_service, undo_redo_service):
        self.frame = None
        self.tk = Tk()
        self.__students_service = students_service
        self.__disciplines_service = disciplines_service
        self.__grades_service = grades_service
        self.__statistics_service = statistics_service
        self.__undo_redo_service = undo_redo_service

    def run_GUI(self):
        self.tk.title("Laboratory manager")
        self.frame = Frame(self.tk)
        self.frame.pack(fill='both')
        label = Label(self.frame, text="Student ID:")
        label.pack(side=LEFT)
        self.student_id_text_field = Entry(self.frame, {})
        self.student_id_text_field.pack(side=LEFT)
        label = Label(self.frame, text="Student Name:")
        label.pack(side=LEFT)
        self.student_name_text_field = Entry(self.frame, {})
        self.student_name_text_field.pack(side=LEFT)
        self.add_student_button = Button(self.frame, text="Add student", command=self.__add_student)
        self.add_student_button.pack(side=LEFT)
        self.remove_student_button = Button(self.frame, text="Remove student", command=self.__remove_student)
        self.remove_student_button.pack(side=LEFT)
        self.update_student_button = Button(self.frame, text="Update student", command=self.__update_student)
        self.update_student_button.pack(side=LEFT)
        self.search_student_button = Button(self.frame, text="Search student", command=self.__search_student)
        self.search_student_button.pack(side=LEFT)
        self.list_students_button = Button(self.frame, text="List students", command=self.__list_students)
        self.list_students_button.pack(side=LEFT)

        self.frame = Frame(self.tk)
        self.frame.pack(fill='both')
        label = Label(self.frame, text="Discipline ID:")
        label.pack(side=LEFT)
        self.discipline_id_text_field = Entry(self.frame, {})
        self.discipline_id_text_field.pack(side=LEFT)
        label = Label(self.frame, text="Discipline name:")
        label.pack(side=LEFT)
        self.discipline_name_text_field = Entry(self.frame, {})
        self.discipline_name_text_field.pack(side=LEFT)
        self.add_discipline_button = Button(self.frame, text="Add discipline", command=self.__add_discipline)
        self.add_discipline_button.pack(side=LEFT)
        self.remove_discipline_button = Button(self.frame, text="Remove discipline", command=self.__remove_discipline)
        self.remove_discipline_button.pack(side=LEFT)
        self.update_discipline = Button(self.frame, text="Update discipline", command=self.__update_discipline)
        self.update_discipline.pack(side=LEFT)
        self.search_discipline_button = Button(self.frame, text="Search discipline", command=self.__search_discipline)
        self.list_disciplines_button = Button(self.frame, text="List disciplines", command=self.__list_disciplines)
        self.list_disciplines_button.pack(side=LEFT)

        self.frame = Frame(self.tk)
        self.frame.pack(fill='both')
        label = Label(self.frame, text="Student ID:")
        label.pack(side=LEFT)
        self.student_id_grade_text_field = Entry(self.frame, {})
        self.student_id_grade_text_field.pack(side=LEFT)
        label = Label(self.frame, text="Discipline ID:")
        label.pack(side=LEFT)
        self.discipline_id_grade_text_field = Entry(self.frame, {})
        self.discipline_id_grade_text_field.pack(side=LEFT)
        label = Label(self.frame, text="Grade value:")
        label.pack(side=LEFT)
        self.grade_value_text_field = Entry(self.frame, {})
        self.grade_value_text_field.pack(side=LEFT)
        self.add_grade_button = Button(self.frame, text="Grade:", command=self.__add_grade)
        self.add_grade_button.pack(side=LEFT)
        self.list_grades_button = Button(self.frame, text="List grades", command=self.__list_grades)
        self.list_grades_button.pack(side=LEFT)

        self.frame = Frame(self.tk)
        self.frame.pack(fill='both')
        self.best_students_statistics_button = Button(self.frame, text="Best students statistics", command=self.__best_students_statistics)
        self.best_students_statistics_button.pack(side=LEFT)
        self.best_disciplines_statistics_button = Button(self.frame, text="Best disciplines statistics", command=self.__best_disciplines_statistics)
        self.best_disciplines_statistics_button.pack(side=LEFT)
        self.failing_students_statistics_button = Button(self.frame, text="Failing students statistic", command=self.__failing_students_statistics)
        self.failing_students_statistics_button.pack(side=LEFT)
        self.undo_command_button = Button(self.frame, text="Undo command", command=self.__undo_command)
        self.undo_command_button.pack(side=LEFT)
        self.redo_command_button = Button(self.frame, text="Redo command", command=self.__redo_command)
        self.redo_command_button.pack(side=LEFT)

        self.tk.lift()
        self.tk.attributes('-topmost', True)
        self.tk.after_idle(self.tk.attributes, '-topmost', False)
        self.tk.mainloop()

    def __add_student(self):
        try:
            student_id = self.student_id_text_field.get()
            student_name = self.student_name_text_field.get()
            self.__students_service.add_to_repo(student_id, student_name)
            messagebox.showinfo("Added", "Student %s has been added successfully." % student_name)
        except StudentException as se:
            messagebox.showinfo("Error", "Error adding student - "+str(se))
        except ValueError:
            messagebox.showinfo("Error", "Invalid arguments!")

    def __remove_student(self):
        student_id = self.student_id_text_field.get()
        if student_id is None:
            messagebox.showinfo("Error", "Please fill the student id!")
        else:
            if len(self.__students_service.search_student_id(student_id)) != 0:
                try:
                    self.__students_service.remove_from_repo(student_id)
                except StudentException as se:
                    messagebox.showinfo("Error", "Error updating student - "+str(se))
            else:
                messagebox.showinfo("Error", "There is no student having that id to be removed!")

    def __update_student(self):
        student_id = self.student_id_text_field.get()
        student_name = self.student_name_text_field.get()
        if student_id is None or student_name is None:
            messagebox.showinfo("Error", "Please fill both student id and student name!")
        else:
            if len(self.__students_service.search_student_id(student_id)) != 0:
                try:
                    self.__students_service.update(student_id, student_name)
                except StudentException as se:
                    messagebox.showinfo("Error", "Error updating student - %s"+str(se))
            else:
                messagebox.showinfo("Error", "There is no student having that id to be updated!")

    def __search_student(self):
        student_id = self.student_id_text_field.get()
        if student_id is None:
            student_name = self.student_name_text_field.get()
            if student_name is None:
                messagebox.showinfo("Error", "Please fill either student id or student name field!")
            else:
                search_result = self.__students_service.search_student_name(student_name)
                if len(search_result) != 0:
                    string_result = ""
                    for index in range(0, len(search_result)):
                        string_result += "Student ID: "+search_result[index].id.rjust(5) + " Student name: " + \
                                        search_result[index].name.rjust(20) + "\n"
                    messagebox.showinfo("Search result: ", string_result)
                else:
                    messagebox.showinfo("Search", "There were no students found!")
        else:
            search_result = self.__students_service.search_student_id(student_id)
            if len(search_result) != 0:
                string_result = ""
                for index in range(0, len(search_result)):
                    string_result += "Student ID:  " + search_result[index].id.rjust(5) + " Student name:  " + \
                                    search_result[index].name.rjust(20) + "\n"
                messagebox.showinfo("Search result: ", string_result)
            else:
                messagebox.showinfo("Search", "There were no students found!")

    def __list_students(self):
        students = self.__students_service.repo.list
        string_result = ""
        for a_student in students:
            string_result += "Student ID:  " + a_student.id.rjust(5) + " Student name:  " + a_student.name.rjust(20) + "\n"
        messagebox.showinfo("Students:", string_result)

    def __add_discipline(self):
        try:
            discipline_id = self.discipline_id_text_field.get()
            discipline_name = self.discipline_name_text_field.get()
            self.__disciplines_service.add_to_repo(discipline_id, discipline_name)
            messagebox.showinfo("Added", "discipline %s has been added successfully." % discipline_name)
        except DisciplineException as de:
            messagebox.showinfo("Error", "Error adding discipline - " + str(de))
        except ValueError:
            messagebox.showinfo("Error", "Invalid arguments!")

    def __remove_discipline(self):
        discipline_id = self.discipline_id_text_field.get()
        if discipline_id is None:
            messagebox.showinfo("Error", "Please fill the discipline id!")
        else:
            if len(self.__disciplines_service.search_discipline_id(discipline_id)) != 0:
                try:
                    self.__disciplines_service.remove_from_repo(discipline_id)
                except DisciplineException as de:
                    messagebox.showinfo("Error", "Error updating discipline - " + str(de))
            else:
                messagebox.showinfo("Error", "There is no discipline having that id to be removed!")

    def __update_discipline(self):
        discipline_id = self.discipline_id_text_field.get()
        discipline_name = self.discipline_name_text_field.get()
        if discipline_id is None or discipline_name is None:
            messagebox.showinfo("Error", "Please fill both discipline id and discipline name!")
        else:
            if len(self.__disciplines_service.search_discipline_id(discipline_id)) != 0:
                try:
                    self.__disciplines_service.update(discipline_id, discipline_name)
                except DisciplineException as de:
                    messagebox.showinfo("Error", "Error updating discipline - %s" + str(de))
            else:
                messagebox.showinfo("Error", "There is no discipline having that id to be updated!")

    def __search_discipline(self):
        discipline_id = self.discipline_id_text_field.get()
        if discipline_id is None:
            discipline_name = self.discipline_name_text_field.get()
            if discipline_name is None:
                messagebox.showinfo("Error", "Please fill either discipline id or discipline name field!")
            else:
                search_result = self.__disciplines_service.search_discipline_name(discipline_name)
                if len(search_result) != 0:
                    string_result = ""
                    for index in range(0, len(search_result)):
                        string_result += "Discipline ID: " + search_result[index].id.rjust(5) + " Discipline name: " + \
                                         search_result[index].name.rjust(20) + "\n"
                    messagebox.showinfo("Search result: ", string_result)
                else:
                    messagebox.showinfo("Search", "There were no disciplines found!")
        else:
            search_result = self.__disciplines_service.search_discipline_id(discipline_id)
            if len(search_result) != 0:
                string_result = ""
                for index in range(0, len(search_result)):
                    string_result = "Discipline ID:  " + search_result[index].id.rjust(5) + " Discipline name:  " + \
                                    search_result[index].name.rjust(20) + "\n"
                messagebox.showinfo("Search result: ", string_result)
            else:
                messagebox.showinfo("Search", "There were no disciplines found!")

    def __list_disciplines(self):
        disciplines = self.__disciplines_service.repo.list
        string_result = ""
        for a_discipline in disciplines:
            string_result += "Discipline ID:  " + a_discipline.id.rjust(5) + " Discipline name:  " +\
                             a_discipline.name.rjust(20) + "\n"
        messagebox.showinfo("Disciplines:", string_result)

    def __add_grade(self):
        student_id = self.student_id_grade_text_field.get()
        discipline_id = self.discipline_id_grade_text_field.get()
        grade_value = self.grade_value_text_field.get()
        if student_id is None or discipline_id is None or grade_value is None:
            messagebox.showinfo("Error", "Please make sure you filled student id, discipline id and grade value fields!")
        else:
            if len(self.__students_service.search_student_id(student_id)) != 0:
                if len(self.__disciplines_service.search_discipline_id(discipline_id)) != 0:
                    try:
                        self.__grades_service.add_to_repo(student_id, discipline_id, grade_value)
                    except GradeException as ge:
                        messagebox.showinfo("Error", "Error grading the student - "+str(ge))
                    except DisciplineException as de:
                        messagebox.showinfo("Error", "Error grading the student - "+str(de))
                    except StudentException as se:
                        messagebox.showinfo("Error", "Error grading the student - " + str(se))
                else:
                    messagebox.showinfo("Error", "There is no discipline having that id to grade a student at!")
            else:
                messagebox.showinfo("Error", "There is no student having that id to be graded!")

    def __list_grades(self):
        grades = self.__grades_service.repo.list
        string_result = ""
        for a_grade in grades:
            string_result += "Student ID:  " + str(a_grade.student_id).rjust(5) + "Discipline ID: " + \
                            str(a_grade.discipline_id).rjust(5) + "Grade value:  " + str(a_grade.value).rjust(5) + "\n"
        messagebox.showinfo("Grades: ", string_result)

    def __best_students_statistics(self):
        self.__statistics_service.create_best_students_statistic()
        best_students = self.__statistics_service.repo.list
        string_result = ""
        for a_student_and_grade in best_students:
            string_result += "Student ID:  " + str(a_student_and_grade['Student id']).rjust(5) + "    Average grade:  " +\
                             str(a_student_and_grade['average_grade']).rjust(5) + "\n"
        messagebox.showinfo("Best students: ", string_result)
        self.__statistics_service.repo.clear_statistic()

    def __best_disciplines_statistics(self):
        self.__statistics_service.create_best_disciplines_statistic()
        best_disciplines = self.__statistics_service.repo.list
        string_result = ""
        for a_discipline_and_grade in best_disciplines:
            string_result += "Discipline ID:  " + str(a_discipline_and_grade['Discipline id']).rjust(5) + "     Average grade:  "\
                             + str(a_discipline_and_grade['average_grade']).rjust(5) + "\n"
        messagebox.showinfo("Best students: ", string_result)
        self.__statistics_service.repo.clear_statistic()

    def __failing_students_statistics(self):
        self.__statistics_service.add_failing_student_statistic()
        failing_students = self.__statistics_service.repo.list
        if len(failing_students) != 0:
            string_result = ""
            for a_student in failing_students:
                string_result += "Student ID:  " + a_student.id.rjust(5) + "\n"
            messagebox.showinfo("Best students: ", string_result)
        else:
            messagebox.showinfo("Hooray!", "There are no failing students ☺")
        self.__statistics_service.repo.clear_statistic()

    def __undo_command(self):
        try:
            self.__undo_redo_service.false()
            self.__undo_redo_service.undo()
        except UndoRedoException as ure:
            messagebox.showinfo("Error", ure)
        else:
            messagebox.showinfo("Undone", "The operation has been undone successfully!")

    def __redo_command(self):
        try:
            self.__undo_redo_service.false()
            self.__undo_redo_service.redo()
        except UndoRedoException as ure:
            messagebox.showinfo("Error", ure)
        else:
            messagebox.showinfo("Undone", "The operation has been redone successfully!")
