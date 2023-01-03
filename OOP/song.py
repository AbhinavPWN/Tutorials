"""
    this is the example of docstring in python
    help(Song)
"""


class Song:
    def __init__(self, title, artist, duration=0) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
        class to represent the album by tracking its track list

        Attributes:
        album_name:
        year:
        artist

    Methods:
        add_song():
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist('various artist')
        else:
            self.artist = artist
        self.track = []

    def add_song(self, song, position=None):
        if position is None:
            self.track.append(song)
        else:
            self.track.insert(position, song)


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_albums(self, album):
        self.albums.append(album)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(f'{artist_field}, {album_field}, {year_field}, {song_field}')

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # retrieve the artist object if there is one,
                # otherwise create a new artist object and add it to the artist list.
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_albums(new_album)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist
                # Retrieve the album object if there is one,
                # otherwise create a new album object and store it in the artist's collection.
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_albums(new_album)

        # Create a new song objects and add it to the current albums collections
        new_song = Song(song_field, new_artist)
        new_album.add_song(new_song)

        # After reading the last line of the text file we will have the albums and artist that haven't been stored - process them
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_albums(new_album)
            artist_list.append(new_artist)

    return artist_list


def create_checkfile(artist_list):
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.track:
                    print('{0.name}\t{1.name}\t{1.year}\t{2.title}'.format(
                        new_artist, new_album, new_song), file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print('There are {} artists'.format(len(artists)))

    create_checkfile(artists)
