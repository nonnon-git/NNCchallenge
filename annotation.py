import csv
import glob


sound_dir = '/Users/nobuyuki/PycharmProjects/trimmed_validation/*.wav'
tpz_dir = '/Users/nobuyuki/PycharmProjects/trimmed_validation_tpz/*.wav'
sound_paths = glob.glob(sound_dir)
tpz_paths = glob.glob(tpz_dir)


csv_file = 'test_tpz.csv'
with open(csv_file, "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['x: music', 'y: tpz_or_not'])
    for path in sound_paths:
        csv_writer.writerow([path, 0])
    for path in tpz_paths:
        csv_writer.writerow([path, 1])

