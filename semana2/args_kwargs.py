def soma(*args):
    # If anyone call sum(1,"2"), will be error, because "2" is string
    # explanatory error
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("Only numbers (int/float)")
    return sum(args)

def describe_person(**kwargs):
    for key, value in kwargs.items():
        # capitalize the first letter
        print(f"{key.capitalize()}:{value}")
    
describe_person(name="Kaio", age=21, city="RJ")

print(soma(20,30,40))
