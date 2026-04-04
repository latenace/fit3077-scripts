class Number :
    def __init__(self, value):
        if isinstance(value, int):
            self.is_integer = True
            self.is_float = False
            self.int_value = value
            self.float_value = 0.0
        
        else:
            isInteger = False
            isFloat = False
            self.INT_VALUE = 0
            self.FLOAT_VALUE = value
    
    def add(self, number):
        result = None;
        # two integers
        if (isinstance(self, int) and isinstance(number, int)):
            result = Number(self.INT_VALUE + number.INT_VALUE)
        
        # integer and float
        elif (isinstance(self, int) and isinstance(number, float)):
            result = Number(self.INT_VALUE + number.FLOAT_VALUE)
        
        # float and integer
        elif (isinstance(self, float) and isinstance(number, int)):
            result = Number(self.FLOAT_VALUE + number.INT_VALUE)

        # two floats
        else:
            result = number(self.FLOAT_VALUE + number.FLOAT_VALUE)
        
        return(result)