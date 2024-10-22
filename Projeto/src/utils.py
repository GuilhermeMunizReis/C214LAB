from random import randint

#This class contains random value elements, therefore it is tested manually
class Dice:
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
            values.append(randint(lower_bound, upper_bound))
        elif quantity == -1 or quantity == 2:
            values.append(randint(lower_bound, upper_bound))
            values.append(randint(lower_bound, upper_bound))
        else:
            return -1
            

