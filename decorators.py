PASSWORD = '12345'


# * Decorator function
def password_required(func):
    """password_required Ensures that the password given is the same as the password saved

    Args:
        func (func): function to decorate or apply the extra functionality
    """
    def wrapper():
        password = input('Cual es tu contraseña? ')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña es incorrecta. ')

    return wrapper


# * DECORATOR
@password_required
def needs_password():
    print('La contraseña es correcta')


# * Decorator function
def upper(parameter_function):
    """upper Makes the same as the keyword "upper"

    Args:
        parameter_function (func): function to decorate or apply the extra functionality
    """
    # ? *ARGS and **KWARGS are the expected arguments of the function to decorate
    #   More info here: https://bit.ly/3QC1MWC
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


# * DECORATOR
@upper
def say_my_name(name):
    return (f'Hola, {name}')


if __name__ == '__main__':
    print(say_my_name('Juan'))
    # needs_password()
