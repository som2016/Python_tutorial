"""
class school:
    pass


student1 = school()
student2 = school()

student1.FirstName = 'Disha' # instance or object variable
student1.LastName = 'Patani'
student1.Class = '12th'
student1. percentage = 90

student2.FirstName = 'Sraadha'
student2.LastName = 'Kapoor'
student2.Class = '12th'
student2.percentage = 89.5

print(student2.FirstName)
print(student1.FirstName)

"""

'''
class school:
    def __init__(self, FirstName, LastName, Class, Percentage):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Class = Class
        self.Percentage = Percentage


student1 = school('Disha', 'Patani', '12th', '90')
student2 = school('Sraadha', 'Kapoor', '12th', '89.5') # passing instance variable

print(student1.FirstName)
print(student2.FirstName)

'''


class school:
    profession = 'Actress'  #Class Variable

    def __init__(self, FirstName, LastName, Class, Percentage):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Class = Class
        self.Percentage = Percentage

    def fullName(self):
        return self.FirstName + ' ' + self.LastName

    def prof(self):
        self.profession = self.fullName() + ' ' + self.profession


student1 = school('Disha', 'Patani', '12th', '90')
student2 = school('Sraadha', 'Kapoor', '12th', '89.5')

print(student1.FirstName)
print(student2.FirstName)
print(student1.fullName())
print(student2.fullName())
print(student1.__dict__)
student1.prof()
print(student1.profession)
