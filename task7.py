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
        return max(self.all_grades, key=lambda semester: mean(self.all_grades[semester]) if self.all_grades[semester] else None)

    def worst_semester(self):
        return min(self.all_grades, key=lambda semester: mean(self.all_grades[semester]) if self.all_grades[semester] else None)



all_grades = {
    1: [4, 4, 3, 5, 3, 5, 4, 4],
    2: [5, 3, 4, 5, 4, 4, 4, 5]
}

student = Student('Shevchenko', 'Taras', all_grades)
print(f'Student: {student}')

semester = 1
average = student.average_grade_for_sem(semester)
print(f'Avg grade for {semester} semester: {average}')

overall_avg = student.average_grade_overall()
print(f'Avg grade for all semesters: {overall_avg}')

best_sem = student.best_semester()
print(f'Best of all semesters: {best_sem}')

worst_sem = student.worst_semester()
print(f'Worst of all semesters: {worst_sem}')