from datetime import datetime

def greeting(name):
    current_time = datetime.now()
    print("Hello", name, ", today is", current_time.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    name = input("Type your name: ")
    greeting(name)

if __name__ == "__main__":
    main()
