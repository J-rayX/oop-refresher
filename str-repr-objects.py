class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      
    def __str__(self):
        return "Employee is  {name} and Employee salary is {salary}".format(name=self.name, salary=self.salary)      

  def __repr__(self):
        return "Employee is  {name} and Employee salary is {salary}".format(name=self.name, salary=self.salary)      
        

emp1 = Employee("Amar Howard", 30000)
print(emp1)
