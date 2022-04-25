def uppercase_decorator(text_function):
    def wrapper():
        func = text_function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def hello_world():
    return "hello world"


if __name__ == '__main__':
    print(hello_world())
