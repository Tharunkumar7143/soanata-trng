from employee import Employee
from address import Address
address1=Address("Hyderabad")
address2=Address("Guntur")

emp1=Employee("tharun","kumar","vijayawada")
emp2=Employee("tharun","kumar",[address1,address2])
print(address1.display_address())
print(address2.display_address())
print(emp1.display())
print(emp2.display())