import wave
import struct
from scipy import fromstring, int16
import numpy as np
import os
import math
import pathlib
import glob


# 一応既に同じ名前のディレクトリがないか確認。
file = os.path.exists("output")
print(file)

if not file:
    # 保存先のディレクトリの作成
    os.mkdir("output")



# filenameに読み込むファイル、timeにカットする間隔
def cut_wav(filename, time):
    # timeの単位は[sec]

    # ファイルを読み出し
    wavf = filename
    wr = wave.open(wavf, 'rb')

    # waveファイルが持つ性質を取得
    ch = wr.getnchannels()
    # モノラルなら1、ステレオなら２
    width = wr.getsampwidth()
    # サンプルサイズをバイト長で返す
    fr = wr.getframerate()
    # サンプリングレートを返す
    fn = wr.getnframes()
    # オーディオフレーム数を返す
    total_time = 1.0 * fn / fr
    integer = math.floor(total_time * 100)  # 小数点以下切り捨て
    t = int(time * 100)  # 秒数[sec]
    frames = int(ch * fr * t / 100)
    num_cut = int(integer // t)
    # waveの実データを取得し、数値化
    data = wr.readframes(wr.getnframes())
    # 最大 n 個のオーディオフレームを読み込んで、 bytes オブジェクトとして返します
    wr.close()
    # nframes が正しいか確認して、ファイルが wave によって開かれていた場合は閉じます。
    X = np.frombuffer(data, dtype=int16)
    # 引数bufferとして渡されたbufferを１次元配列に変換する
    for i in range(num_cut):
        print(i)
        # 出力データを生成
        outf = 'output/' + str(i) + '.wav'
        start_cut = int(i * frames)
        end_cut = int(i * frames + frames)
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


# print("input filename = ")
# # f_name = "audiostock_47858"
# # print("cut time = ")
# # cut_time = 1.5
# # cut_wav(f_name, float(cut_time))

# directory = pathlib.Path('/Users/nobuyuki/PycharmProject/nncc_audiostock_16k_24sec_1')
# cut_time = 1.5
# for file in os.listdir(directory):
#  print(file)
    # filename = os.fsdecode(file)
    # cut_wav(filename, float(cut_time))


img_dir = '/Users/nobuyuki/PycharmProject/nncc_audiostock_16k_24sec_1'  # 入力ディレクトリ
out_dir = 'output'  # 出力ディレクトリ
types = ['*.wav']
cut_time = 1.5
paths = []
for t in types:
    paths.extend(glob.glob(os.path.join(img_dir, t)))
for file in paths:
    cut_wav(file, cut_time)