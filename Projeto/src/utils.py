from random import randint

#This class contains random value elements, therefore it is tested manually
class Utils:
    """
        Contains lots of usefull and common use stuff, like roll dice
    """

    @staticmethod
    def roll(d_side:int = 6, quantity: int = 1) -> int:
        """
        d_side (int) -> Defines how many sides have this dice
        quantity (int) -> Defines how many dice will be rolled. -1:Disadvantage, 1:Normal, 2:Advantage

        return (int) -> Returns roll value. -1:Invalid values
        """
        valid_d_number = [3, 4, 5, 6, 8, 10, 12, 20, 100]

        if d_side not in valid_d_number:
            return -1
        
        lower_bound = 1
        upper_bound = d_side

        values = []

        if quantity == 1:
            return randint(lower_bound, upper_bound)
        elif quantity == -1:
            values.append(randint(lower_bound, upper_bound))
            values.append(randint(lower_bound, upper_bound))
        
            return max(values)
        elif quantity == 2:
            values.append(randint(lower_bound, upper_bound))
            values.append(randint(lower_bound, upper_bound))
        
            return min(values)
        else:
            return -1

class Dice:
    def __init__(self, sides:int):
        self.sides = sides

        self.__check_valid_instance()


    def __check_valid_instance(self):
        valid_sides = [3,4,5,6,8,10,12,20,100]

        if self.sides not in valid_sides:
            raise Exception

    def __repr__(self):
        return f"d{self.sides}"
    