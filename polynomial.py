import copy


class Polynomial:
    def __init__(self, coefficients):
        self.__coefficients = copy.copy(coefficients)
        while self.__coefficients and self.__coefficients[0] == 0:
            self.__coefficients.pop(0)
        self.__degree = len(self.__coefficients) - 1

    def __str__(self):
        string = ""
        for i, c in enumerate(self.__coefficients):
            if c != 0:
                if i != 0:
                    if c > 0:
                        string += " + "
                    else:
                        c = -c
                        string += " - "
                exponent = self.__degree - i
                if c != 1 or exponent == 0:
                    string += str(c)
                if exponent != 0:
                    if exponent == 1:
                        string += "X"
                    else:
                        string += "X^" + str(exponent)
        return string

    def __add__(self, polynom):
        delta = self.__degree - polynom.__degree

        if delta >= 0:

            out_coefficients = self.__coefficients[:delta]

            for i, c in enumerate(polynom.__coefficients):
                out_coefficients.append(self.__coefficients[delta + i] + c)
        elif delta < 0:
            delta = -delta
            out_coefficients = polynom.__coefficients[:delta]
            for i, c in enumerate(self.__coefficients):
                out_coefficients.append(polynom.__coefficients[delta + i] + c)

        return Polynomial(out_coefficients)

    def __mul__(self, polynom):
        out_coefficients = []
        if self.__coefficients and polynom.__coefficients:
            out_degree = self.__degree + polynom.__degree

            if self.__degree < polynom.__degree:
                coeff1 = self.__coefficients
                coeff2 = polynom.__coefficients
            else:
                coeff1 = polynom.__coefficients
                coeff2 = self.__coefficients
            for i in range(out_degree + 1):
                out_coefficient = 0
                for j, c in enumerate(coeff1):
                    c_id = i - j
                    if c_id >= 0 and c_id < len(coeff2):
                        out_coefficient += c * coeff2[c_id]
                out_coefficients.append(out_coefficient)

        return Polynomial(out_coefficients)

    def __rmul__(self, other):
        out_coefficients = [other * c for c in self.__coefficients]

        return Polynomial(out_coefficients)

    def __call__(self, value):
        if self.__coefficients:
            out_value = self.__coefficients[0]
            for c in self.__coefficients[1:]:
                out_value = out_value * value + c
        else:
            out_value = 0

        return out_value

    def __neg__(self):
        out_coefficients = []
        for c in self.__coefficients:
            out_coefficients.append(-c)
        return Polynomial(out_coefficients)

    def __sub__(self, polynom):
        delta = self.__degree - polynom.__degree

        if delta >= 0:

            out_coefficients = self.__coefficients[:delta]

            for i, c in enumerate(polynom.__coefficients):
                out_coefficients.append(self.__coefficients[delta + i] - c)
        elif delta < 0:
            delta = -delta
            out_coefficients = polynom.__coefficients[:delta]
            for i, c in enumerate(self.__coefficients):
                out_coefficients.append(polynom.__coefficients[delta + i] - c)

        return Polynomial(out_coefficients)

    @property
    def degree(self):
        return self.__degree

