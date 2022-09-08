import datetime


def logger(old_function):

    def new_function(*args, **kwargs):
        date = datetime.datetime.now()
        name = old_function.__name__
        result = old_function(*args,**kwargs)
        with open('new.txt', 'w') as file:
            file.write(f'Дата и время: {date}\n'
                       f'Имя функции: {name}\n'
                       f'Аргументы: {args,kwargs}\n'
                       f'Результат: {result}\n')
        return result


    return new_function


@logger
def get_sum(a,b):
    return a+b


if __name__ == '__main__':
    get_sum(12,9)


def parametr_logger(path = "logger.txt"):
    def logger(old_function):
        def new_function(*args, **kwargs):
            date = datetime.datetime.now()
            name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open('logger.txt', 'w') as file:
                file.write(f'Дата и время: {date}\n'
                           f'Имя функции: {name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result

        return new_function
    return logger


