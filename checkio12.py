def max(*args, **kwargs):
    key = kwargs.get("key", None)
    max_value = None
    if key:
        if len(args) == 1:
            for arg in args[0]:
                if key(arg) > max_value:
                    max_value = arg
        else:
            for arg in args:
                if key(arg) > max_value:
                    max_value = arg
    else:
        if len(args) == 1:
            for arg in args[0]:
                if arg > max_value:
                    max_value = arg
        else:
            for i in args:
                if i > max_value:
                    max_value = i
    return max_value


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    
    if key:
        min_value = key(args[0][0])
        if len(args) == 1:
            for arg in args[0]:
                if key(arg) < min_value:
                    min_value = arg
        else:
            for arg in args:
                if key(arg) < min_value:
                    min_value = arg
    else:
        min_value = args[0]
        if len(args) == 1:
            for arg in args[0]:
                if arg < min_value:
                    min_value = arg
        else:
            for i in args:
                if i < min_value:
                    min_value = i
    return min_value


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
