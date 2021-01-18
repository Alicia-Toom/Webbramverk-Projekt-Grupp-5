from functools import wraps

def dec(arg):
    def decorator(func):
        @wraps(func)
        def wrapper(a, b):
            return arg + func(a, b)
        return wrapper
    return decorator

@dec('greet_user')
def something(greeting, name):
    return f'{greeting}, {name}!'


def main():
    print(something.__name__)


if __name__ == '__main__':
    main()