class Student():
    def __init__(self, name, age, class_, spanish_grade, english_grade, social_studies_grade, science_grade):
        self.name = name
        self.age = age
        self.class_ = class_
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade

    def get_average(self):
        average = (self.spanish_grade + self.english_grade + self.social_studies_grade + self.science_grade) / 4
        return average