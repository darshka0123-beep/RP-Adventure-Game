import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load data with streamlit caching
@st.cache_data
def load_data():
    return pd.read_csv('bts.csv')

songData = load_data()

# Bts music info data set csv

favSong = "Spring Day"
st.write("My favorite BTS song is **" + favSong + "**.")

# st.write(songData.head())
# st.write(songData["eng_track_title"])

# Filter Data
st.write("\nThe data for my favorite song is:\n")

# Create a new variable to store your favorite album data
favSongbooleanlist = songData["eng_track_title"] == favSong
favSongData = songData.loc[favSongbooleanlist]
st.dataframe(favSongData)

#st.write(fav_album_boolean_list)


album_title = favSongData["eng_album_title"].iloc[0]
albumbooleanlist = songData["eng_album_title"] == album_title
albumsongdata = songData.loc[albumbooleanlist]
numofsongs = len(albumsongdata)

st.write("We will be comparing " + favSong + " to other songs in the album " + album_title)
st.write("There are " + str(numofsongs) + " songs in the album " + album_title)

st.write("...............................................................................................................")

# Shortest Song Duration
minduration = albumsongdata["spotify_track_duration_ms"].min()
st.write("The shortest song duration (ms) in this album is: " + str(minduration))
min_difference = 274097 - minduration
st.write(favSong + " is " + str(min_difference) +" longer than the shortest song in this album.")

# Longest Song Duration
maxduration = albumsongdata["spotify_track_duration_ms"].max()
st.write("The longest song duration (ms) in this album is: " + str(maxduration))
max_difference = maxduration - 274097
st.write(favSong + " is " + str(max_difference) + " shorter than the longest song in this album.")

# find median
median = albumsongdata["spotify_track_duration_ms"].median()
st.write("The median song duration of the data set is: " + str(median))
st.write(favSong + " is longer than the median.")

# find mean
mean = albumsongdata["spotify_track_duration_ms"].mean()
st.write("The mean song duration of the data set is: " +str(mean))
st.write(favSong + " is longer than the mean.")

st.write("............................................................................................................")

# Create graphs
#Convert duration from milliseconds to minutes
duration_in_minutes = songData["spotify_track_duration_ms"] / 60000

# Create histogram
fig1, ax1 = plt.subplots()
ax1.hist(duration_in_minutes, bins=20)
ax1.grid(True)
ax1.set_title("Track Duration of All BTS Songs Histogram")
ax1.set_xlabel("Track Duration (Minutes)")
ax1.set_ylabel("Number of Songs")

# Display histogram
st.pyplot(fig1)

# st.writes Interpretation of histogram
st.write(
    "According to the histogram, most fall under the duration between 3 to 5 minutes. The shape of the histogram is a bell curve showing it is likely normally distributed."
)

# Convert string values to float/int
songData["spotify_track_duration_ms"] = pd.to_numeric(songData["spotify_track_duration_ms"], errors="coerce")

# Convert duration from ms to minutes for cleaner numbers
duration_min = songData["spotify_track_duration_ms"] / 60000

# make the window wider and taller to give the labels space

# Create Scatterplot
fig2, ax2 = plt.subplots(figsize=(10,8))
ax2.scatter(duration_min, songData["eng_album_title"], alpha=0.7, color='purple')
ax2.grid(True)
ax2.set_title("Track Duration vs Album")
ax2.set_xlabel("Track Duration (Minutes)")
ax2.set_ylabel("Album Name")
ax2. tick_params(axis='y', labelsize=8)
plt.tight_layout()

# Display Scatterplot on Streamlit
st.pyplot(fig2)

# Displays Interpretation of scatterplot
st.write("According to the scatter plot, we can conclude there is no obvious correlation between track duration and album.")

st.write("\nThank you for reading through my data analysis!")