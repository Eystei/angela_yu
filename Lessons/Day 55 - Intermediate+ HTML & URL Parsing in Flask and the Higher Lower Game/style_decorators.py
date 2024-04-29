def center_text(func):
    def wrapper():
        return f"<div style='text-align: center'>{func()}</div>"

    return wrapper


def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def make_italic(func):
    def wrapper():
        return f"<em>{func()}</em>"

    return wrapper


def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"

    return wrapper
