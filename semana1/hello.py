# datetime module was imported into code
from datetime import datetime

name = "Kaio"

def greeting(name):
    # thus creating a variable to receive the module
    n = datetime.now()
    # we use strftime to standardize
    print("Hello", name, "today is", n.strftime("%Y-%m-%d %H:%M:%S"))

greeting(name)


