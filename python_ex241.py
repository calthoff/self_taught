# IMPORTANT. I changed many of the variable names in this example
# so the example fits on smaller devices. Old versions of the book have longer
# variable names. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!

rock = []
country = []


def collect_songs():
    song = "Enter a song."
    ask = "Type r or c. q to quit"

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre ==("c"):
            cy = input(song)
            country.append(cy)

        else:
            print("Invalid.")
    print(rock)
    print(country)

collect_songs()
