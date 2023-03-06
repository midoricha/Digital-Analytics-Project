import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

df = pd.read_csv('spotify-clean.csv', delimiter=';')

dataset = []

# time series
group1 = df.groupby(['year'], as_index=False)[
    ['danceability', 'loudness', 'acousticness', 'energy']].mean()
print(group1)

plt.plot(group1['year'], group1['acousticness'], label='Acousticness mean')

plt.legend()
plt.savefig('timeseries_acousticness_mean.pdf')
plt.clf()

plt.plot(group1['year'], group1['danceability'], label='Danceability mean')

plt.legend()
plt.savefig('timeseries_danceability_mean.pdf')
plt.clf()

plt.plot(group1['year'], group1['energy'], label='Energy mean')

plt.legend()
plt.savefig('timeseries_energy_mean.pdf')
plt.clf()

plt.plot(group1['year'], group1['loudness'], label='Loudness mean')

plt.legend()
plt.savefig('timeseries_loudness_mean.pdf')
plt.clf()

group2 = df.groupby(['year'], as_index=False)[
    ['danceability', 'loudness', 'acousticness', 'energy']].std()
print(group2)

plt.plot(group2['year'], group2['acousticness'],
         label='Acousticness standard deviation')

plt.legend()
plt.savefig('timeseries_acousticness_std.pdf')
plt.clf()

plt.plot(group2['year'], group2['danceability'],
         label='Danceability standard deviation')

plt.legend()
plt.savefig('timeseries_danceability_std.pdf')
plt.clf()

plt.plot(group2['year'], group2['energy'], label='Energy standard deviation')

plt.legend()
plt.savefig('timeseries_energy_std.pdf')
plt.clf()

plt.plot(group2['year'], group2['loudness'],
         label='Loudness standard deviation')

plt.legend()
plt.savefig('timeseries_loudness_std.pdf')
plt.clf()


plt.plot(group2['year'], group2['acousticness'],
         label='Acousticness standard deviation')
plt.plot(group2['year'], group2['danceability'],
         label='Danceability standard deviation')
plt.plot(group2['year'], group2['energy'], label='Energy standard deviation')
plt.plot(group2['year'], group2['loudness'],
         label='Loudness standard deviation')

plt.legend()
plt.savefig('timeseries_all_std.pdf')
plt.clf()

# correlation
print(rp.correlation.corr_pair(df[['year', 'acousticness']]))
print(rp.correlation.corr_pair(df[['year', 'danceability']]))
print(rp.correlation.corr_pair(df[['year', 'loudness']]))
print(rp.correlation.corr_pair(df[['year', 'energy']]))

data = pd.DataFrame(group1)
data.to_csv('aggregated_mean.csv', sep=';', index=False)

data = pd.DataFrame(group2)
data.to_csv('aggregated_std.csv', sep=';', index=False)
