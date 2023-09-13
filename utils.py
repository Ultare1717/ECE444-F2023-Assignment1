class Utils:

    def reversed(self, number):
        if type(number) is int:
            reversed = 0
            while number != 0:
                remainder = number % 10
                reversed = reversed * 10 + remainder
                number = number // 10
            return reversed
        else:
            raise TypeError("Input must be an Integer")
    
    def formatter(self, number):
        if type(number) is int:
            binaryNumber = bin(number)[2:]
            octalNumber = oct(number)[2:]
            return binaryNumber, octalNumber
        else:
            raise TypeError("Input must be an Integer")
        