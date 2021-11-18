class Color:
    """Colorizes symbols"""
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'
    
    def __init__(self, r: int, g: int, b: int):
        self.rgb = r, g, b # write validation method at home

    # def _validation(number: int):
    #     return(max(min(255, number)))

    def __str__(self):
        return (f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}●{self.END}{self.MOD}')

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Can\'t compare different instances')
        return (self.rgb[0] == other.rgb[0] and self.rgb[1] == other.rgb[1] and self.rgb[2] == other.rgb[2])

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Can\'t compare different instances')
        return(self.rgb[0] + other.rgb[0], self.rgb[1] + other.rgb[1], self.rgb[2] + other.rgb[2])

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.rgb)
    
    def __mul__(self, constant: int):
        c = max(min(constant, 1), 0) 
        cl = -256 * (1 - c)
        F = (259 * (cl+ 255)) / (255 * (259 - cl))
        return Color(*list(map((lambda L: int(F * (L - 128) + 128)), self.rgb)))
    
    def __rmul__(self, constant: int):
        return self.__mul__(constant)

if __name__ == '__main__':
    orange1 = Color(255, 7, 0)
    orange2 = Color(255, 7, 0)
    print(0.3 * orange1)
