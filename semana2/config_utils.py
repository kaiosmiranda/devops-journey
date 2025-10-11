# def process_config(*car, **style):
#     print("Name car is ", car)
#     print("Style car is ", style)

# process_config("Corolla", "Civic", color=["Black, Blue"], age=["2020, 2025"])

def process_config(*car, **style):
    print(f"Name car is ", car[0])

    for key, value in style.items():
        print(f"{key}: {value}")


process_config("Civic", color="Black", age="2020", revision="OK")