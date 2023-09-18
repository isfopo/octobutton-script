from Live import Song, Track


def get_track_at_index(song: Song.Song, index: int, offset: int = 0) -> Track.Track:
    return song.tracks[offset + index]
