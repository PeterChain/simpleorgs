

class NumberRange(object):
    """
    Number range operations
    """
    FILL_LENGTH = 5

    def __init__(self, number):
        """
        Constructor which receives the original number
        """
        self.old_number = number
    
    def next(self, step):
        """
        Increase the original number (string) by step
        units and returns it's string value
        """
        int_num = int(self.old_number)
        int_num += step
        result_str = str(int_num).zfill(self.FILL_LENGTH)
        return result_str