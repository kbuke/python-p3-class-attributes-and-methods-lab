class Song:

    count = 0
    genres = []
    artists = []
    genre_count = None
    artist_count = None

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genres)
        Song.add_to_artist_count(self.artists)
    
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
    
    @classmethod
    def add_to_genres(cls, song_genre):
        cls.genres.append(song_genre)
    
    @classmethod
    def add_to_artists(cls, singer):
        cls.artists.append(singer)
    
    @classmethod
    def add_to_genre_count(cls, genre_count):
        cls.genre_count = {i:genre_count.count(i) for i in genre_count}
    
    @classmethod
    def add_to_artist_count(cls, artist_count):
        cls.artist_count = {i:artist_count.count(i) for i in artist_count}
        

        
