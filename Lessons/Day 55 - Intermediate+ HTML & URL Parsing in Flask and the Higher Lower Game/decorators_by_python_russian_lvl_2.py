"""Link: https://www.youtube.com/watch?v=5oFZBkEnXnk&ab_channel=PythonRussian"""
import decorators_by_python_russian


@decorators_by_python_russian.typed(int)
def calculate(a, b, c):
    return a + b + c


@decorators_by_python_russian.typed(str)
def convert(a, b):
    return a + b


if __name__ == '__main__':
    print(calculate(1, 3, True))
    print(convert("1", "True"))
