import numpy as np
import pandas as pd

# test data
df = pd.read_csv('/Users/nobuyuki/PycharmProjects/NNCchallenge/test_tpz_2sec.csv')
csv_file = 'test_tpz_2sec_at_random.csv'

np.random.seed(0)
rdf = df.sample(frac=1).reset_index(drop=True)
rdf.to_csv(csv_file, index=False)


