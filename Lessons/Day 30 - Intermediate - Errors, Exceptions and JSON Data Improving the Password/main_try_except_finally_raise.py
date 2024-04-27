# try: Something that might cause an exceptions
# except: Do this if there was an exception
# else: Do this if there were NO exceptions
# finally: Do this no matter what happens

"""
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("Something")
except KeyError as error_message:
    print(f"THE KEY {error_message} DOES NOT EXIST")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("THIS IS AN ERROR THAT I WAS MADE UP.")

"""

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("HUMAN HEIGHT SHOULD NOT BE OVER 3 METERS")

bmi = weight / height ** 2
print(bmi)
