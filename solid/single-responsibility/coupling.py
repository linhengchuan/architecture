"""
For the student class, the save function is tightly coupled to saving to db layer.
This is tight coupling because we cannot easily change to other saving application which is bad.
Ideally the student class should only contain simple student functions.
Have another repository class and refer to class within the student class to remove the tight coupling.
If we need to change the save database type, we only need to change and compile repository class.
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
