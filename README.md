# Digital-Analytics-Project
Collect, process, analyze, and visualize data of the top hits in of the past 50 years to study how popular music evolved.

Step 1:
Billboard has an end-of-year top 100 for every year, e.g., https://www.billboard.com/charts/year-end/1970/hot-100-songs. There is a system in the URLs, which makes it easy to automatically request the html of page after page. Per year, I scraped the artist and track titles and stored them in a csv file with three variables: year, artist, and track. Billboard.com is sensitive to rapid consecutive requests, so I paused the script for about 2-3 seconds at the end of each iteration using the Python pause module.

Step 2: 
The Spotify API provides a brilliant resource with its Audio Features Endpoint: https://developer.spotify.com/console/get-audio-features-track/. The documentation that the Audio Features Endpoint requires a Track ID as an argument for each call.So I first used the Search Endpoint to get that piece of information before proceeding with the actual API call. I queried the combination of artist and track in the Search Endpoint, to make sure I was getting the right ID. After all, titles could refer to songs by multiple artists. It is possible that on rare occasions I couldn't get a Track ID. I made sure the script is able to handle such exceptions. 

Step 3:
I used the track ID information I got from step 2 to query the Audio Features Endpoint. I chose to specifically study on four audio features - danceability, engergy, loudness and acousticness. I saved the audio features to a csv file.

Step 4:
I did the data cleaning to remove duplicates and null values.

Step 5:
Data aggregation. Eventually I ended up having a dataset with one aggregated observation per relevant audio feature per year. I wanted to describe central tendency for a measure such as e.g., bpm (mean and/or median). That would allow me to sketch how music has generally changed through the years. It does not tell us much (or anything) about the diversity, the homogeneity or heterogeneity. That why I also needed the dispersion (e.g., standard deviation) that shows the variability over time decreases (i.e., an indication of homogenisation). 

Data Visualization. A time series is likely the most insightful way to visually describe the trends over time in the data.
