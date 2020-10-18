import librosa
import soundfile as sf


fname = "/Users/nobuyuki/PycharmProjects/t+pazolite/tempestissimo.wav"

y, s = librosa.load(fname, sr=8000)
sf.write("/Users/nobuyuki/PycharmProjects/t+pazolite/encorded_tempestissimo.wav", y, 8000)

