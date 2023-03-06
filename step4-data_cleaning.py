import pandas as pd

df = pd.read_csv('spotify-audio-features.csv', delimiter=';')

print(df.info())

print(df.shape)

print(df.isnull().sum())

isolatemissing = pd.isnull(df['track id'])
print(df[isolatemissing])

isolatemissing1 = pd.isnull(df['danceability'])
print(df[isolatemissing1])

df = df.dropna()

print(df.shape)

print(df.duplicated().sum())

print(df[df.duplicated()])

df = df.drop_duplicates()

print(df.shape)

df.to_csv('spotify-clean.csv', sep=';', index=False)
