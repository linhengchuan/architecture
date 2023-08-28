"""
There can be multiple reasons to change in single component such as Student:
1. Change in saving database type
2. Change in student id format
What we can do is split to NewStudent and StudentRepository class so that which component only have one reason to change.

"""


class Student():
    def __init__(self, id) -> None:
        self._id = id

    def save(self):
        # Save to db with sqlite
        pass

    def get_student_id(self):
        return self._id


class NewStudent():
    def __init__(self, id) -> None:
        self._id = id

    def save(self):
        StudentRepository().save(self)

    def get_student_id(self):
        return self._id


class StudentRepository():
    def save(student: 'NewStudent'):
        # Save to db with sqlite
        pass
