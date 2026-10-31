# class Person:
#     def __init__(self, first="John", last="Doe", country="Somewhere", job="SWE"):
#         self.first = first
#         self.last = last
#         self.country = country
#         self.job = job
#         self.skills = []

#     def output(self):
#         return f"Full name: {self.first}, {self.last} Country: {self.country} Job title: {self.job}"
    
#     def add_skills(self, *skill):
#         self.skills.append(skill)

# class Student(Person):
#     def __init__(self, first="John", last="Doe", country="Somewhere", job="SWE", gender="Male"):
#         self.gender = gender
#         super().__init__(first, last, country, job)

#     def output(self):
#         gender = 'He' if self.gender == 'Male' else 'She'
#         return f"{self.first} {self.last} {gender} lives in {self.country}"

# def main():
#     # person = Person("Ibrahim", "Hussain", "Somalia")
#     # person.add_skills("HTML","CSS", "JS")
#     # print(person.output(), "\n", person.skills)
#     # print(type(person.skills))
#     # anonymous = Person()
#     # print(anonymous.output())
#     # student1 = Student("Axmed", "Jamac", "Somalia", "Data Analyst")
#     # student1.add_skills("Excel", "Power BI", "SQL", "Python")
#     # print(student1.output(), "\n", student1.skills)

#     # student2 = Student("Xasan", "Cali", "Kenya")
#     # print(student2.output())


# if __name__ == "__main__":
#     main()