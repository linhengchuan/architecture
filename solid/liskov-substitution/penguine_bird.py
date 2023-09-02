"""
Penguine (is-a) bird. Thus we allow penguine to inherit bird class.
However there is a problem with this relationship. Penguine is not able
to fly like most birds do. We need to over write the fly function and
unimplement it. This is a sign of design flaws.
Penguine (is-a) bird is correct statement but it is against the liskov
substitution principle which test whether a class can be substituted by
its subtype(In this case bird class will ).
Solution for this problem is we do not let penguine class inherit bird
class. We create a common base class that has characteristics of both
example animal class.
"""


class bird():
    def __init__(self) -> None:
        pass

    def fly(self):
        print("Bird flew away!")


class penguine(bird):
    def __init__(self) -> None:
        super().__init__()
        pass

    def fly(self):
        # Unimplemented because penguine cant fly
        print("Error: Penguine cant fly. Liskov subs principle failed.")
        pass


class utils():
    def set_fly(birds):
        for bird in birds:
            bird.fly()


a = bird()
b = bird()
c = penguine()

utils.set_fly([a, b, c])
