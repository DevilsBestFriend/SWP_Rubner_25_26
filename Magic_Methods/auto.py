class Auto:

    def __init__(self, ps: int):
        if not isinstance(ps, int):
            raise TypeError("ps must be an int")
        if ps < 0:
            raise ValueError("ps must be non-negative")
        self.ps = ps

    def __repr__(self):
        return f"Auto(ps={self.ps})"

    def __str__(self):
        return f"Auto with {self.ps} PS"

    # len(a)
    def __len__(self):
        return self.ps

    # arithmetic
    def __check_other_auto(self, other):
        if isinstance(other, Auto):
            return other.ps
        if isinstance(other, int):
            return other
        raise TypeError(f"Unsupported operand type(s) for operation: 'Auto' and '{type(other).__name__}'")

    def __add__(self, other):
        other_ps = self.__check_other_auto(other)
        return self.ps + other_ps

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other_ps = self.__check_other_auto(other)
        return self.ps - other_ps

    def __rsub__(self, other):
        if isinstance(other, int):
            return other - self.ps
        if isinstance(other, Auto):
            return other.ps - self.ps
        raise TypeError(f"Unsupported operand type(s) for -: '{type(other).__name__}' and 'Auto'")

    def __mul__(self, other):
        other_ps = self.__check_other_auto(other)
        return self.ps * other_ps

    def __rmul__(self, other):
        return self.__mul__(other)

    # comparisons
    def __eq__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps == other.ps

    def __lt__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps < other.ps

    def __gt__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps > other.ps


if __name__ == "__main__":
    # Test/demo lines for all implemented magic methods
    a1 = Auto(50)
    a2 = Auto(60)

    print("a1:", a1)
    print("a2:", a2)

    # len
    print("len(a1):", len(a1))
    print("a1.__len__():", a1.__len__())

    # addition
    print("a1 + a2 =>", a1 + a2)  # expect 110
    print("a1 + 10 =>", a1 + 10)  # allow int
    print("10 + a2 =>", 10 + a2)  # radd

    # subtraction
    print("a2 - a1 =>", a2 - a1)  # expect 10
    print("a1 - 20 =>", a1 - 20)
    print("100 - a1 =>", 100 - a1)  # rsub

    # multiplication
    print("a1 * a2 =>", a1 * a2)
    print("a1 * 2 =>", a1 * 2)
    print("3 * a2 =>", 3 * a2)

    # type checking: unsupported operations should raise TypeError
    try:
        print(a1 + "bad")
    except TypeError as e:
        print("TypeError as expected for invalid add:", e)

    # comparisons
    print("a1 == a2 =>", a1 == a2)
    print("a1 < a2 =>", a1 < a2)
    print("a1 > a2 =>", a1 > a2)

    # direct attribute
    print("a1.ps =>", a1.ps)
