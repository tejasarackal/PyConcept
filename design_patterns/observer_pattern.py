from abc import ABC, abstractmethod
from collections import defaultdict
from decimal import Decimal


class Observer(ABC):
    @abstractmethod
    def update(self, observable, *args, **kwargs):
        pass

    @abstractmethod
    def remove(self, observable):
        pass


class Observable:
    def __init__(self):
        self._observers = list()

    @property
    def observers(self):
        return self._observers

    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        self.observers.remove(observer)
        observer.remove(self)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(self, *args, **kwargs)


class Employee(Observable):
    """ Publisher class that notifies its subscribers """
    def __init__(self, name, salary):
        super().__init__()
        self._name = name
        self._salary = Decimal(str(salary))

    @property
    def salary(self):
        return self._salary

    @property
    def name(self):
        return self._name

    @salary.setter
    def salary(self, new_salary):
        self._salary = Decimal(str(new_salary))
        self.notify_observers(new_salary)

    def add_observer(self, observer):
        super().add_observer(observer)
        self.notify_observers()

    def __str__(self):
        return f'{self.__class__.__name__} \nId: {id(self)}, Name: {self._name}, Salary: {self._salary}'


class Payroll(Observer):
    """ Subscriber that distributes payroll for emploees """
    def __init__(self):
        self.employee_package = defaultdict(Decimal)

    def update(self, employee: Employee, *args, **kwargs):
        self.employee_package[id(employee)] = employee.salary

    def remove(self, employee):
        del self.employee_package[id(employee)]

    def __str__(self):
        lst = [self.__class__.__name__]
        for e_id, e_salary in self.employee_package.items():
            lst.append(f'Id: {e_id}, Salary: {e_salary:.2f}')
        return '\n'.join(lst)


class TaxMan(Observer):
    """ Subscriber that calculates tax for employees """
    def __init__(self):
        self.tax_returns = defaultdict(Decimal)

    def calculate_tax(self, employee: Employee):
        self.tax_returns[id(employee)] = Decimal(str(Decimal(0.25) * employee.salary))

    def update(self, employee: Employee, *args, **kwargs):
        self.calculate_tax(employee)

    def remove(self, employee):
        del self.tax_returns[id(employee)]

    def __str__(self):
        lst = [self.__class__.__name__]
        for e_id, e_tax in self.tax_returns.items():
            lst.append(f'Id: {e_id}, Tax: {e_tax:.2f}')
        return '\n'.join(lst)


if __name__ == '__main__':
    e1 = Employee(name='T', salary=72000)
    p = Payroll()
    t = TaxMan()

    print('Initial State')
    print(f'{e1}')
    print(f'{p}')
    print(f'{t}')

    e1.add_observer(p)
    e1.add_observer(t)
    print('\nPayroll and Taxman Subscribers subscribed to Publisher Employee')
    print(f'{p}')
    print(f'{t}')

    e2 = Employee(name='N', salary=82000)
    e2.add_observer(p)
    e2.add_observer(t)
    print('\nEmployee 2 Created')
    print(f'{e2}')
    print(f'{p}')
    print(f'{t}')

    e3 = Employee(name='M', salary=92000)
    e3.add_observer(p)
    e3.add_observer(t)
    print('\nEmployee 3 Created')
    print(f'{e3}')
    print(f'{p}')
    print(f'{t}')

    e1.salary = 56000
    e3.salary = 50000
    print('\nEmployee 1 and 3 updated their salary')
    print(f'{e1}')
    print(f'{e3}')
    print(f'{p}')
    print(f'{t}')

    e3.delete_observer(p)
    e3.delete_observer(t)
    print('\nEmployee 3 unsubscribed')
    print(f'{p}')
    print(f'{t}')
