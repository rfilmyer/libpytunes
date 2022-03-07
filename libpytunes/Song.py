from six import iteritems
import time # only for __repr__()

class Song:
    """
    Song Attributes:
    name (String)
    track_id (Integer)
    artist (String)
    album_artist (String)
    composer = None (String)
    album = None (String)
    genre = None (String)
    kind = None (String)
    size = None (Integer)
    total_time = None (Integer)
    track_number = None (Integer)
    track_count = None (Integer)
    disc_number = None (Integer)
    disc_count = None (Integer)
    year = None (Integer)
    date_modified = None (Time)
    date_added = None (Time)
    bit_rate = None (Integer)
    sample_rate = None (Integer)
    comments = None (String)
    rating = None (Integer)
    rating_computed = False (Boolean)
    album_rating = None (Integer)
    play_count = None (Integer)
    location = None (String)
    location_escaped = None (String)
    compilation = False (Boolean)
    grouping = None (String)
    lastplayed = None (Time)
    skip_count = None (Integer)
    skip_date = None (Time)
    length = None (Integer)
    persistent_id = None (String)
    album_rating_computed = False (Boolean)
    work = None (String)
    movement_name = None (String)
    movement_number = None (Integer)
    movement_count = None (Integer)
    playlist_only = None (Bool)
    apple_music = None (Bool)
    protected = None (Bool)
    """
    name = None
    track_id = None
    artist = None
    album_artist = None
    composer = None
    album = None
    genre = None
    kind = None
    size = None
    total_time = None
    track_number = None
    track_count = None
    disc_number = None
    disc_count = None
    year = None
    date_modified = None
    date_added = None
    bit_rate = None
    sample_rate = None
    comments = None
    rating = None
    rating_computed = None
    album_rating = None
    play_count = None
    skip_count = None
    skip_date = None
    location = None
    location_escaped = None
    compilation = None
    grouping = None
    lastplayed = None
    length = None
    persistent_id = None
    album_rating_computed = None
    work = None
    movement_name = None
    movement_number = None
    movement_count = None
    playlist_only = None
    apple_music = None
    protected = None

    def __iter__(self):
        for attr, value in iteritems(self.__dict__):
            yield attr, value
    
    def __str__(self):
        base_string = "{artist} - {name} | {album} ({year}) {total_time // (1000*60)} {(total_time//1000) % 60:02}"
        base_string = base_string.format(artist=self.artist, name=self.name, album=self.album, year=self.year)
        rating_string = ""
        if self.loved:
            rating_string += " \u2665" #heart symbol
        if self.rating is not None and self.rating > 0:
            star_symbol = "/u2606" if self.rating_computed else "/u2605"
            star_symbols = star_symbol * (self.rating // 20)
            rating_string += (" " + star_symbols)
        song_special_properties = []
        all_special_properties = ["apple_music", "protected", "podcast"]
        for prop in all_special_properties:
            if vars(self).get(prop):
                song_special_properties.append(prop)
        special_properties_string = ""
        if song_special_properties:
            special_properties_string += " "
            special_properties_string += "["
            special_properties_string += ", ".join(song_special_properties)
            special_properties_string += "]"

        return base_string + rating_string + special_properties_string

    def __repr__(self):
        args_for_instantiation = []
        for prop, value in vars(self).items():
            if value is not None:
                args_for_instantiation.append("{prop}={repr_value}".format(prop=prop, repr_value=repr(value)))
        return "Song(" + ", ".join(args_for_instantiation) + ")"

    def ToDict(self):
        return {key: value for (key, value) in self}
