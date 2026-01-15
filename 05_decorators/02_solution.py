def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling {func.__name__} with args: ({args_value}), kwargs: {{{kwargs_value}}}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("Hello")

@debug
def greet(name="user", greeting="Hello"):
    print (f"{greeting}, {name}!")

hello()
print(greet(name="Riya", greeting="Hi"))
