class py_solution:
    def int_to_Roman(self, number):
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4,
               1]
        syb = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV",
               "I"]
        roman_num = ''
        i = 0
        while  number > 0:
            for x in range(number // val[i]):
                roman_num += syb[i]
                number -= val[i]
            i += 1
        return roman_num

number = int(input("Type in a number to convert to roman numeral: "))
print(py_solution().int_to_Roman(number))
