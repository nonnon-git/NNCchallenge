import librosa
import soundfile as sf


fname = "/Users/nobuyuki/PycharmProjects/t+pazolite/t+pazolite_musics.wav"

y, s = librosa.load(fname, sr=8000)
sf.write("/Users/nobuyuki/PycharmProjects/t+pazolite/encorded_tpz.wav", y, 8000)

