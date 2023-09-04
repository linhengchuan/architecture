"""
Fax and Printer class implements IFaxPrinter interface class. There will
be empty methods implemented in both classes. The empty methods in Fax
and Printer class causes confusion. Other developers assumed to not look
into what is written in the methods. Thus the empty methods may be
called.
The solution would be to segregate the interface class into different groups.
IFaxPrint will be split into IFax and IPrint classes so that there will not be
empty methods in the Fax and Printer classes.
"""


class IFaxPrinter():
    def __init__(self) -> None:
        raise NotImplementedError

    def fax(self):
        raise NotImplementedError

    def print():
        raise NotImplementedError


class Fax(IFaxPrinter):
    def __init__(self) -> None:
        pass

    def fax(self):
        print("fax")

    def print(self):
        pass  # force to do something here


class Printer(IFaxPrinter):
    def __init__(self) -> None:
        pass

    def fax(self):
        pass  # force to do something here

    def print(self):
        print("print")
