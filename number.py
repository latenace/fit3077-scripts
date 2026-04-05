class Number :
    def __init__(self, value):
        if isinstance(value, int):
            self.is_integer = True
            self.is_float = False
            self.is_complex = False
            self.INT_VALUE = value
            self.FLOAT_VALUE = 0.0
            self.REAL_PART = 0.0
            self.IMAGINARY_PART = 0.0
            
        elif isinstance(value, float):
            self.is_integer = False
            self.is_float = True
            self.is_complex = False
            self.INT_VALUE = 0
            self.FLOAT_VALUE = value
            self.REAL_PART = 0.0
            self.IMAGINARY_PART = 0.0
        
        else:
             is_integer = False
             is_float = False
             is_complex = True
             self.INT_VALUE = 0
             self.FLOAT_VALUE = 0.0
             self.REAL_PART = 0.0
             self.IMAGINARY_PART = 0.0
    
    def add(self, number):
        result = None;
        # two integers
        if (self.is_integer and number.is_integer):
            result = Number(self.INT_VALUE + number.INT_VALUE)
        
        # integer and float
        elif (self.is_integer and number.is_float):
            result = Number(self.INT_VALUE + number.FLOAT_VALUE)

        # integer and complex
        elif (self.is_integer and number.is_complex):
            result = Number(self.INT_VALUE + number.REAL_PART + number.IMAGINARY_PART)
        
        # float and integer
        elif (self.is_float and number.is_integer):
             result = Number(self.FLOAT_VALUE + number.INT_VALUE)

        # two floats
        elif (self.is_float and number.is_float):
             result = Number(self.FLOAT_VALUE + number.FLOAT_VALUE)
        
        return(result)
    
a = Number(2)
b = Number(1.5)

print(a.add(a).INT_VALUE)
print(a.add(b).FLOAT_VALUE)