class Employee:
    def __init__(self, name, hours):
        self.__name = name
        self.__hours = hours

    def get_name(self):
        return self.__name

    def hours(self):
        return self.__hours


class HourlyEmployee(Employee):
    def __init__(self, name, hours, pay=30):
        super().__init__(name, hours)
        self.pay = pay

    def weekly_pay(self, hours):
        if hours <= 40:
            pay = self.__hours * self.__pay
        else:
            pay = (40 * self.pay) + ((hours - 40) * self.pay * 1.5)
        return pay


class SalariedEmployee(Employee):
    def __init__(self, name, hours, pay=52000):
        super().__init__(name, hours)
        self.pay = pay

    def weekly_pay(self, hours):
        pay = self.pay / 52
        return pay


class Manager(Employee):
    def __init__(self, name, hours, bonus=50, pay=104000):
        super().__init__(name, hours)
        self.pay = pay
        self.bonus = bonus

    def weekly_pay(self, hours):
        pay = (self.pay / 52) + 50
        return pay


def print_salaries(staff):
    for employee in staff:
        name = employee.get_name()
        hours = int(input("Hours worked by " + name + ": "))
        pay = employee.weekly_pay(hours)
        print("{}: {:.2f}".format(name, pay))


# The main program starts here
staff = []
staff.append(HourlyEmployee("Harry Morgan", 30.0))  # 30.0 is the hourly wage
staff.append(SalariedEmployee("Sally Lin", 52000.0))  # 52000 is the annual salary
staff.append(Manager("Mary Smith", 104000.0, 50.0))  # 104000 is the annual salary,
# 50.0 is the weekly bonus

print_salaries(staff)
