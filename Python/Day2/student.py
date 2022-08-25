class student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
    def display(self):
        return self.student_id,self.student_name
std1=student(22769,'tharun')

display1=std1.display()
print(display1)
setattr(std1,'student_class',30)
print(getattr(std1,'student_class'))
delattr(std1,'student_name')
print(hasattr(std1,"student_name"))
std1=student(22769,'tharun kumar')
display1=std1.display()
print(display1)
setattr(std1,'__studentdept',60)
print(getattr(std1,'__studentdept'))