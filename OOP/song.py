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

    def add_song(self, name, year, title):
        """Add a new song tp the collection of albums
        This method will add the song to an album in the collection. A  new 
        album will be created in the collections if it's doesn't already exists 


        Args:
            name (_type_): 
            year (_type_): 
            title (_type_): 
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self)
            self.add_albums(album_found)
        else:
            print('Found albums ' + name)

        album_found.add_song(title)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(f'{artist_field}, {album_field}, {year_field}, {song_field}')

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

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
