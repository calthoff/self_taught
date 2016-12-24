
# http://tinyurl.com/zzyuspf


rock = []
country = []




def collect_songs():
    song= """Enter the
   name of your
   song."""
    genre = None
    while True:
        genre = input("Type rock
       or country to
       add a new
       song. q to
       quit")
        if genre == "q":
            break
        if genre == "rock":
            rock = input(song)
            rocks.append(rock)


        elif genre ==("country"):
            country = input(song)
            country.append(country)


        else:
            print("Invalid genre.")
    print(rocks)
    print(country)


collect_songs()
