class Employee:
    def __init__(self,fname,lname,address):
        self.firstname=fname
        self.lastname=lname
        self.address=address

    def display(self):
        return self.firstname[0].upper()+" "+self.lastname[0].upper(),self.address



