"""Python serial number generator."""

# from _typeshed import StrPath


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.original_num = start
        
    def __repr__(self):
        return f"Serial number generator starting at {self.start}."
    
    def generate(self):
        '''
        Generate new serial number each time this method is called on an instance. The next serial number generated will by 1 more than the previous serial number.
        '''
        serial_number = self.start
        self.start += 1
        return serial_number
    
    def reset(self):
        '''
        Method to reset the serial number back to the original number used to initialize this instance of SerialGenerator.
        '''
        self.start = self.original_num