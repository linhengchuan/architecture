"""
Initially ProjectWork class only takes in 
"""

class ProjectWork():
    from typing import overload
    @overload
    def calculate_success_rate_a(self, member: 'Employee'): # only for illustration purpose, python type check does not restrict data type.
        print("Employee function")
        return member.get_skill_level()
    
    @overload
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