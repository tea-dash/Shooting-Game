from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("/Users/tadashikumazawa/Desktop/game/sounds/move.wav")
play(song)