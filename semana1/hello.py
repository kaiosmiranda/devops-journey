# datetime module was imported into code
from datetime import datetime

# thus creating a variable to receive the module
n = datetime.now()

print("Hello, World!")
# we use strftime to standardize
print("Today is", n.strftime("%Y-%m-%d %H:%M:%S"))
