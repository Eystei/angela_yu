class User:
    def __init__(self, *, name: str):
        self.name = name
        self.is_logged_in = False

    def to_dict(self):
        return self.__dict__


def is_auth_decorator(func):
    def wrapper(*args):
        if args[0].is_logged_in == 1:
            func(args[0])
    return wrapper


@is_auth_decorator
def create_blog_post(user):
    print(f"This {user.name}'s new blog post")


user_buzz_yu = User(name="Buzz Yu")
user_buzz_yu.is_logged_in = True
print(user_buzz_yu.to_dict())
create_blog_post(user_buzz_yu)
