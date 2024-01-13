class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(cls, genre):
        if (genre in cls.genres):
            return
        else:
            cls.genres.append(genre)

    def add_to_artists(cls, artist):
        if (artist in cls.artists):
            return
        else:
            cls.artists.append(artist)

    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] +=1
        else:
            cls.genre_count.update({genre : 1})

    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] +=1
        else:
            cls.artist_count.update({artist : 1})