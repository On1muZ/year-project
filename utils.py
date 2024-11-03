class Number:
    def __init__(self, number, base, accuracy = 10):
        self.number = number
        self.base = base
        self.alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.accuracy = accuracy

    def _to_base_int(self, num, base):
        n = abs(num)
        b = self.alpha[n % base] 
        while n >= base :
            n = n // base
            b += self.alpha[n % base] 
        return ('' if num >= 0 else '-') + b[::-1] 
    
    def _to_base_frac(self, frac, base) :
        b = ''
        accuracy = self.accuracy
        while accuracy:
            frac *= base
            frac = round(frac, accuracy)
            b += str(int(frac))
            frac -= int(frac)
            accuracy -= 1
        return b

    def convert(self, base_to):
        if '.' in str(self.number) :
            num, frac = map(str, str(self.number).split('.'))
            num = int(num, self.base)
            a = self._to_base_int(num, base_to)
            b = 0
            k = self.base
            for i in frac :
                b += self.alpha.index(i) / k
                k *= self.base
            b = self._to_base_frac(b, base_to)
            return str(a) + '.' + str(b)
        elif ',' in str(self.number):
            num, frac = map(str, str(self.number).split(','))
            num = int(num, self.base)
            a = self._to_base_int(num, base_to)
            b = 0
            k = self.base
            for i in frac :
                b += self.alpha.index(i) / k
                k *= self.base
            b = self._to_base_frac(b, base_to)
            return a + '.' + b
        else :
            return self._to_base_int(int(str(self.number), self.base), base_to)
        

if __name__ == "__main__":
    number = Number(12345, 10)
    print(number.convert(2))
    print(number.convert(8))
    print(number.convert(10))
    print(number.convert(16))