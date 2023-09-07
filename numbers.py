class NumbersToWordsConverter:
    def __init__(self):
        self.units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        self.tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def convert_to_words(self, number):
        if number == 0:
            return "zero"
        elif number < 10:
            return self.units[number]
        elif number < 20:
            return self.teens[number - 10]
        elif number < 100:
            return self.tens[number // 10] + ("-" + self.units[number % 10] if number % 10 != 0 else "")
        elif number < 1000:
            return self.units[number // 100] + " hundred" + (" and " + self.convert_to_words(number % 100) if number % 100 != 0 else "")
        else:
            return self.convert_thousands(number)

    def convert_thousands(self, number):
        thousands = ["", "thousand", "million", "billion"]
        result = ""
        for i in range(len(thousands)):
            if number % 1000 != 0:
                result = self.convert_to_words(number % 1000) + " " + thousands[i] + " " + result
            number //= 1000
        return result.strip()


# Testes unitários
converter = NumbersToWordsConverter()


print(converter.convert_to_words(8)) 


print(converter.convert_to_words(80))  

print(converter.convert_to_words(825)) 


print(converter.convert_to_words(8769))  

print(converter.convert_to_words(8690))  
