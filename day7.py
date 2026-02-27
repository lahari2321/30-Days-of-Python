class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
    
    def get_grade(self):
        average=self.calculate_average()
        if average>=90:
            return 'A'
        elif average>=80:
            return 'B'
        elif average>=70:
            return 'C'
        elif average>=60:
            return 'D'
        elif average>=50:
            return 'E'
        else:
            return 'F'

    def display(self):
        average=self.calculate_average()
        grade=self.get_grade()
        print(f"Name: {self.name}")
        print(f"Average: {average}")
        print(f"Grade: {grade}")

obj=Student("Lahari", [85, 90, 78, 92])
obj.display()

