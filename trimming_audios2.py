import wave
import struct
from scipy import fromstring, int16
import numpy as np
import os
import math
from glob import glob

# 一応既に同じ名前のディレクトリがないか確認。
file = os.path.exists("output")
print(file)

if file == False:
    #保存先のディレクトリの作成
    os.mkdir("output")


#filenameに読み込むファイル、timeにカットする間隔
def cut_wav(filename,time):
    # timeの単位は[sec]

    # ファイルを読み出し
    wavf = filename + '.wav'
    wr = wave.open(wavf, 'r')

    # waveファイルが持つ性質を取得
    ch = wr.getnchannels()
    width = wr.getsampwidth()
    fr = wr.getframerate()
    fn = wr.getnframes()
    total_time = 1.0 * fn / fr
    integer = math.floor(total_time*100) # 小数点以下切り捨て
    t = int(time*100)  # 秒数[sec]
    frames = int(ch * fr * t /100)
    num_cut = int(integer//t)
    # waveの実データを取得し、数値化
    data = wr.readframes(wr.getnframes())
    wr.close()
    X = np.frombuffer(data, dtype=int16)

    for i in range(num_cut):
        print(i)
        # 出力データを生成
        outf = 'output/' + str(i) + '.wav'
        start_cut = int(i*frames)
        end_cut = int(i*frames + frames)
        print(start_cut)
        print(end_cut)
        Y = X[start_cut:end_cut]
        outd = struct.pack("h" * len(Y), *Y)

        # 書き出し
        ww = wave.open(outf, 'w')
        ww.setnchannels(ch)
        ww.setsampwidth(width)
        ww.setframerate(fr)
        ww.writeframes(outd)
        ww.close()


print("input filename = ")
f_name = "audiostock_47858"
print("cut time = ")
cut_time = 1.5
cut_wav(f_name,float(cut_time))


# files = glob('パス名');
# for file_name in files:
#     f_name = file_name
#     cut_wav(f_name, float(1.5))
