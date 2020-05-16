# In serializer_demo.py

import json
import xml.etree.ElementTree as et

class Song:
    """You create a song object and a serializer, and you convert the song to its string representation by using the .serialize() method.
     The method takes the song object as a parameter, as well as a string value representing the format you want.
     The last call uses YAML as the format, which is not supported by the serializer, so a ValueError exception is raised.

This example is short and simplified, but it still has a lot of complexity.
There are three logical or execution paths depending on the value of the format parameter.
This may not seem like a big deal, and you’ve probably seen code with more complexity than this,
 but the above example is still pretty hard to maintain."""

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)