def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """

    sequence=[]
    if songs[0][2]<max_size:
        sequence.append(songs[0][0])
    else: return []

    remaining=songs[1:]
    remaining.sort(key=lambda x:x[2])
    cursize=songs[0][2]

    while(True):
        if len(remaining)>0 and cursize+remaining[0][2]<max_size:
            cursize+=remaining[0][2]
            sequence.append(remaining[0][0])
            remaining=remaining[1:]
        else:
            return sequence

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]

print(song_playlist(songs,12.2))