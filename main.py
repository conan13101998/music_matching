import warnings
import json
import sys
import os

warnings.filterwarnings("ignore")

from music_matching import music_matching
from music_matching.recognize import FileRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("/home/doxanh/VoiceProcessing/web/controller/music_matching/config.cnf") as f:
    config = json.load(f)

if __name__ == '__main__':

    analyzer = music_matching(config)

    # # Fingerprint all the mp3's in the directory we give it
    # analyzer.fingerprint_directory("mp3", [".mp3"])
    filename = sys.argv[1]
    # Recognize audio from a file
    song = analyzer.recognize(FileRecognizer, os.path.join(os.path.dirname(filename), "/home/doxanh/VoiceProcessing/web/controller/music_matching/uploads/audio.mp3"))
    print(song["song_name"].replace("-", " "))
