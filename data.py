import pandas as pd

def load(path):
    df = pd.read_csv(path,
                     header=None,
                     names=['day', 'time', 'price', 'bid', 'ask', 'vol'])
    df['date'] = pd.to_datetime(df['day'] + df['time'],
                                format='%m/%d/%Y%H:%M:%S')
    df = df.set_index('date')
    df = df.drop(['day', 'time', 'bid', 'ask'],
                 axis=1)
    df = df.drop_duplicates()
    return df
