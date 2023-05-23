from statistics import mean


class Student:
    def __init__(self, last_name, first_name, all_grades):
        self.last_name = last_name
        self.first_name = first_name
        self.all_grades = all_grades

    def __str__(self):
        return f'Student: {self.last_name} {self.first_name}'

    def average_grade_for_sem(self, semester):
        grades = self.all_grades.get(semester)
        if grades:
            return mean(grades)
        return 0

    def average_grade_overall(self):
        all_grades = []
        for semester_grades in self.all_grades.values():
            all_grades.extend(semester_grades)
        if all_grades:
            return mean(all_grades)
        return 0

    def best_semester(self):
        best_semester = None
        best_mean = 0
        for semester in self.all_grades:
            semester_grades = self.all_grades[semester]
            if semester_grades:
                current_mean = mean(semester_grades)
                if current_mean > best_mean:
                    best_semester = semester
                    best_mean = current_mean
        return best_semester

    def worst_semester(self):
        best_semester = None
        best_mean = 999
        for semester in self.all_grades:
            semester_grades = self.all_grades[semester]
            if semester_grades:
                current_mean = mean(semester_grades)
                if current_mean < best_mean:
                    best_semester = semester
                    best_mean = current_mean
        return best_semester

student_grades = {
    1: [4, 4, 3, 5, 3, 5, 4, 4],
    2: [5, 3, 4, 5, 4, 4, 4, 5]
}

if __name__ == '__main__':
    student = Student('Shevchenko', 'Taras', student_grades)
    print(student)

    semester = 1
    average = student.average_grade_for_sem(semester)
    print(f'Avg grade for {semester} semester: {average}')

    overall_avg = student.average_grade_overall()
    print(f'Avg grade for all semesters: {overall_avg}')

    best_sem = student.best_semester()
    print(f'Best of all semesters: {best_sem}')

    worst_sem = student.worst_semester()
    print(f'Worst of all semesters: {worst_sem}')