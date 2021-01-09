# add.mul.sub.abs
# Fourcal
# setdata


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second


class MoreFourCal(FourCal):
    pass


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = MoreFourCal(3, 4)
print(a.first)
print(a.second)

a.setdata(1, 0)

print(a.first)
print(a.second)

print(a.sub())
