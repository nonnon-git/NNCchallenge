import wave
import struct
from scipy import fromstring, int16
from scipy.io.wavfile import read
import numpy as np
import os
import math
import glob

# 一応既に同じ名前のディレクトリがないか確認。
file = os.path.exists("/Users/nobuyuki/PycharmProjects/trimmed_validation_tpz_2sec")

if not file:
    # 保存先のディレクトリの作成
    os.mkdir("/Users/nobuyuki/PycharmProjects/trimmed_validation_tpz_2sec")


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
        # 出力データを生成
        outf = '/Users/nobuyuki/PycharmProjects/trimmed_validation_tpz_2sec/' + os.path.basename(filename).split('.', 1)[0] + '_' + str(i) + '.wav'
        start_cut = int(i * frames)
        end_cut = int(i * frames + frames)
        Y = X[start_cut:end_cut]
        outd = struct.pack("h" * len(Y), *Y)

        # 書き出し
        ww = wave.open(outf, 'wb')
        ww.setnchannels(ch)
        ww.setsampwidth(width)
        ww.setframerate(fr)
        ww.writeframes(outd)
        ww.close()


# ___settings___
sound_dir1 = '/Users/nobuyuki/PycharmProjects/trimmed_audiostock1_2sec/*.wav'
sound_dir2 = '/Users/nobuyuki/PycharmProjects/trimmed_audiostock2_2sec/*.wav'
sound_dir3 = '/Users/nobuyuki/PycharmProjects/trimmed_audiostock1_2sec/audiostock_42554_1_5.wav'

img_dir1 = '/Users/nobuyuki/PycharmProjects/trimmed_validation_12sec/*.wav'
img_dir2 = '/Users/nobuyuki/PycharmProjects/trimmed_validation_tpz_12sec/*.wav'
img_dir3 = '/Users/nobuyuki/PycharmProjects/trimmed_tpz_12sec/*.wav'

#sample_dir = '/Users/nobuyuki/PycharmProjects/sample/audiostock_42554.wav'
out_dir = 'trimmed_validation_tpz_2sec'  # 出力ディレクトリ
types = ['*.wav']
cut_time = 2
paths = glob.glob(sound_dir1)
# img_dir 内のアイテムのパスのリストを取得

# ___main___
# print(paths)
# for file in paths:
#     cut_wav(file, cut_time)


# references
# http://tacky0612.hatenablog.com/entry/2017/11/21/164409
# https://qiita.com/futurebone/items/b3723899235a977f5796
# https://teratail.com/questions/113349

# print(sound_dir1)
# wr = wave.open(sound_dir1, 'rb')
# # waveファイルが持つ性質を取得
# ch = wr.getnchannels()
# # モノラルなら1、ステレオなら２
# width = wr.getsampwidth()
# # サンプルサイズをバイト長で返す
# fr = wr.getframerate()
# # サンプリングレートを返す
# fn = wr.getnframes()
# # オーディオフレーム数を返す
# wr.close()
# print(ch, width, fr, fn)

# >>> ['/Users/nobuyuki/PycharmProjects/t+pazolite/encorded_tpz.wav']
# >>> 1 2 8000 192000
# >>> ['/Users/nobuyuki/PycharmProjects/t+pazolite/encorded_tpz.wav']
# >>> 1 2 8000 86400171


# def checking_data_size(filename):
#     error_list = []
#     for path in filename:
#         wr = wave.open(path, 'rb')
#         # waveファイルが持つ性質を取得
#         ch = wr.getnchannels()
#         # モノラルなら1、ステレオなら２
#         width = wr.getsampwidth()
#         # サンプルサイズをバイト長で返す
#         fr = wr.getframerate()
#         # サンプリングレートを返す
#         fn = wr.getnframes()
#         # オーディオフレーム数を返す
#         wr.close()
#         print(ch, width, fr, fn)
#         if (ch, width, fr, fn) != (1, 2, 8000, 16000):
#             error_list.append(ch, width, fr, fn)
#     return error_list
#
#
# print(checking_data_size(paths))


rate, data = read(sound_dir3)
print(data)
print(type(data))
print(data.shape)
print(data.size)