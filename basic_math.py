"""This module runs a few basic mathematical functions based off of adding and subtracting one"""


def adding_one(integer_one):
    """
        It takes a integer and adds one
        Args:
            integer_one: the integer which needs to have one added
        Returns:
            The integer + 1
    """
    return integer_one + 1


# todo look at replacing it with adding one...
def subtracting_one(integer_one):
    """
           It takes a integer and subtracts one
        Args:
            integer_one: the integer which needs to have one subtracted from it
        Returns:
            The integer + 1
    """
    return integer_one - 1


def adding(integer_one, integer_two):
    """
            It adds two numbers together
            Args:
                integer_one: The original integer
                integer_two: The integer which needs to be added to integer_one
            Returns:
                an integer with the value: integer_one+integer_two
    """
    for _ in range(integer_two):
        integer_one = adding_one(integer_one)
    return integer_one


# todo maybe add fix for this...
def subtraction(integer_one, integer_two):
    """
       It subtracts one number from another
       Args:
           integer_one: The original integer
           integer_two: The integer which needs to be subtracted from integer_one
       Returns:
           an integer with the value: integer_one-integer_two
       """

    for _ in range(integer_two):
        integer_one = subtracting_one(integer_one)
    return integer_one


def multiplication(integer_one, integer_two):
    """
       It multiplies two numbers
       Args:
           integer_one: The original integer
           integer_two: The integer which needs to be multiplied with integer_one
       Returns:
           an integer with the value: integer_one*integer_two
    """
    multiplied_value = 0
    for _ in range(integer_two):
        multiplied_value = adding(integer_one, multiplied_value)
    return multiplied_value


def integer_divide(integer_one, integer_two):
    """
      It divides one number with another number
      Args:
          integer_one: The original integer
          integer_two: The integer which needs to be divided with integer_one
      Returns:
          an integer with the value: integer_one//integer_two
   """
    for i in range(integer_one):
        integer_one = subtraction(integer_one, integer_two)
        if integer_one < 0:
            return i
    return None


def remainder(integer_one, integer_two):
    """
         It divides one number with another number and returns the remainder
         Args:
             integer_one: The original integer
             integer_two: The integer which needs to be divided with integer_one
         Returns:
             an integer with the value: integer_one%integer_two
      """
    for _ in range(integer_one):
        integer_one = subtraction(integer_one, integer_two)
        if integer_one < 0:
            return adding(integer_one, integer_two)
    return None


def power(integer_one, integer_two):
    """
       It returns the one integers to the others power
       Args:
           integer_one: The original integer
           integer_two: The integer which the power of integer_one needs to be applied
       Returns:
           an integer with the value: integer_one^integer_two
    """
    sum_variable = 1
    for _ in range(integer_two):
        sum_variable = multiplication(sum_variable, integer_one)
    return sum_variable


def root(integer_one, integer_two):
    """
       It returns the the root number of root of another number
       Args:
           integer_one: The original integer
           integer_two: The integer which the the root of integer_one needs to be calculated
       Returns:
           an integer with the value: integer_one.root(integer_two)
    """
    for i in range(integer_one):
        if power(i, integer_two) > integer_one:
            return subtraction(i, 1)
    return None


def add_to_list(original_list, value):
    """
       It returns the a list of adding a value to a list
       Args:
           original_list: the list which needs to be added
           value: The value which needs to be added to each element in the list
       Returns:
           a list with the value: [elem1+value,elem2+value]
    """
    return [map(lambda x: adding(x, value), original_list)]


def square_list(original_list):
    """
       It returns the a list which each element squared
       Args:
           original_list: the list which needs to be added
       Returns:
           a list with the value: [elem1*elem1,elem2*elem2]
    """
    return [multiplication(x, x) for x in original_list]


if __name__ == "__main__":
    print(adding_one(2))
