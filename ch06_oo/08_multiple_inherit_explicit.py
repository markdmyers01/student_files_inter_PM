class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.age})'


class Employee(Person):
    def __init__(self, name, age, salary, dept):
        Person.__init__(self, name, age)
        self.salary = salary
        self.dept = dept

    def __str__(self):
        return f'{Person.__str__(self)} Sal: {self.salary} Dept: {self.dept}'


class Commissioned:
    def __init__(self, rate):
        self.comm_rate = rate

    def __str__(self):
        return f'Rate: {self.comm_rate}'

    def my_cool_func(self):
        pass


class Salesperson(Employee, Commissioned):
    def __init__(self, name, age, salary, region, dept='Sales', rate=0.02):
        Employee.__init__(self, name, age, salary, dept)
        Commissioned.__init__(self, rate)
        self.region = region

    def __str__(self):
        emp_str = Employee.__str__(self)
        comm_str = Commissioned.__str__(self)
        return f'{emp_str}, {comm_str} - Reg: {self.region}'


s = Salesperson('William', 37, 99275.00, 'Northeast')
s.my_cool_func()
print(s)
