class Number:
    def __init__(self, number, base, accuracy = 10):
        self.number = number
        self.base = base
        self.alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.accuracy = accuracy

    def _to_base_int(self, num, base):
        n = num
        b = self.alpha[n % base] 
        while n >= base :
            n = n // base
            b += self.alpha[n % base] 
        return b[::-1] 
    
    def _to_base_frac(self, frac, base) :
        frac = float(f"0.{frac}")
        b = ""
        for i in range(100):
            frac *= base
            if base > 10 and int(frac) >= 10:
                b += self.alpha[int(frac)]
            else:
                b += str(int(frac))
            frac -= int(frac)
        return b[:self.accuracy]
    
    def _to_dec_frac(self, frac, base):
        c = -1
        s = 0
        for i in frac:
            s += self.alpha.index(i.upper())*base**c
            c -= 1
        return str(s)[2:]


    def validate_number(self):
        for i in str(self.number):
            if not (i.upper() in self.alpha[:self.base] or i in (',', '.')):
                    raise ValueError

    def convert(self, base_to):
        self.validate_number()
        if '.' in str(self.number) or ',' in str(self.number):
            num, frac = map(str, str(self.number).split('.' if '.' in str(self.number) else ","))
            num = int(num, self.base)
            a = self._to_base_int(num, base_to)
            b = self._to_dec_frac(frac, self.base)
            b = self._to_base_frac(b, base_to)
            number = str(a) + '.' + str(b)
            for i in range(len(number)-1, -1, -1):
                if number[i] == '0':
                    number = number[:i]
                else:
                    break
            return number
        else :
            number = str(self._to_base_int(int(str(self.number), self.base), base_to))
            return number