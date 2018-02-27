# Thank you so much for purchasing my book! Feel free to contact me at cory[at]theselftaughtprogrammer.io.
# If you are enjoying it, please consider leaving a review on Amazon :). Keep up the hard work!

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
