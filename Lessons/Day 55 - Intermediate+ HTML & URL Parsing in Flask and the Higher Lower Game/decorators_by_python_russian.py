def typed_int(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Type should be 'int'")
        return func(*args)

    return wrapper


def typed_str(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError("Type should be 'str'")
        return func(*args)

    return wrapper


def typed(type_):
    def real_decorator(function):
        def wrapped(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f"Type should be '{type_}'")
            return function(*args)

        return wrapped

    return real_decorator
