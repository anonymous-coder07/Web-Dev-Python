def announce(f):
    def wrapper():
        print('About to run the function.....')
        f()
        print('Ending the function.')
    return wrapper

@announce
def hello():
    print('Hello, World!')

