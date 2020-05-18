def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """
    def isInt(x):
        try:
            int(x)
            return True
        except ValueError:
            return False

    if not isInt(a) or not isInt(b):
        print("a and b must be integers")
        return None
    elif a == b:
        return 'Numbers are equal'
    elif a > b:
        return 'First is greater'
    else:
        return 'Second is greater'
