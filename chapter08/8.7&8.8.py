def make_album(artist, name, number=None):
    album = {'artist':artist, 'name':name}
    if number:
        album['number'] = number
    return album

a = make_album('a', 'b', 5)
b = make_album('c', 'd')
print(a,b)

while True:
    artist = input('Type in the artist:')
    name = input('Type in the album name:')
    x = make_album(artist, name)
    print(x)