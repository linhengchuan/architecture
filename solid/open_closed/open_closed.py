"""
Initially ProjectWork class only takes in Employee class.
However there might be future addition of PartTimer class.
Thus the architecture should be design such that ProjectWork class is
close for modification but it can be extended for more features.
"""


class ProjectWork():
    from typing import overload
    # only for illustration purpose, python type check does not restrict
    # datatype.

    def calculate_success_rate_a(self, member: 'Employee'):
        print("Employee function")
        return member.get_skill_level()

    def calculate_success_rate_b(self, member: 'PartTimer'):
        print("PartTimer function")
        return member.get_skill_level()


class Employee():
    def __init__(self) -> None:
        self._skill_level = 5

    def get_skill_level(self):
        return self._skill_level


class PartTimer():
    def __init__(self) -> None:
        self._skill_level = 1

    def get_skill_level(self):
        return self._skill_level


a = ProjectWork()
b = Employee()
c = PartTimer()
a.calculate_success_rate_a(b)
a.calculate_success_rate_b(c)

"""
In the new class, we create a base class that can be inherited so that more
types of workers can be added without changing the original code.
Note: In other language, create a interface that can be implemented
by other classes.
"""


class NewProjectWork():
    from typing import overload

    # only for illustration purpose, python type check does not restrict data
    # type.
    def calculate_success_rate(self, member: 'People'):
        return member.get_skill_level()


class People():
    def __init__(self) -> None:
        self._name = ""


class NewEmployee(People):
    def __init__(self) -> None:
        super.__init__()
        self._skill_level

    def get_skill_level(self):
        return self._skill_level


class NewPartTimer():
    def __init__(self) -> None:
        super.__init__()
        self._skill_level = 1

    def get_skill_level(self):
        return self._skill_level
