# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and
# it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.


def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'album': album_title}
    return album


a = make_album('Tainy', 'Data')
print(a)

b = make_album('Boygenius', 'The Record')
print(b)

c = make_album('SZA', 'SOS')
print(c)
