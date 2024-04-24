# 8-8. User Albums: Start with your program from Exercise 8-7.
# Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
# Be sure to include a quit value in the while loop.


def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'album': album_title}
    return album


while True:
    print("\nPlease enter an album’s artist and title.")
    print("(enter 'q' at any time to quit)")

    artist = input("Please enter album's artist: ")
    if artist == 'q':
        break

    title = input("Please enter album's title: ")
    if title == 'q':
        break

    temp = make_album(artist, title)
    print(temp)
