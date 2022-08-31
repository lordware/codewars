class RomanNumerals:

    def to_roman(val):
        num = [1, 4, 5, 9, 10, 40, 50, 90,
               100, 400, 500, 900, 1000]
        rom = ["I", "IV", "V", "IX", "X", "XL",
               "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        result = ""

        while val:
            div = val // num[i]
            val %= num[i]

            while div:
                result += rom[i]
                div -= 1
            i -= 1
        return result

    def from_roman(roman_num):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        x = 0
        num = 0
        while x < len(roman_num):
            if x + 1 < len(roman_num) and roman_num[x:x + 2] in roman:
                num += roman[roman_num[x:x + 2]]
                x += 2
            else:
                num += roman[roman_num[x]]
                x += 1
        return num
