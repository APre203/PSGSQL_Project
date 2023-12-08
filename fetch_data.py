import pandas as pd
csv_file = "final.csv"
csv_df = pd.read_csv(csv_file, delimiter=",", encoding='utf-8')
csv_df = csv_df.drop(['danceability','energy','key','mode','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','pivot'],axis=1)

csv_df = csv_df.sample(frac=1)
csv_df.reset_index(drop=True, inplace=True)


genre = []
artist_name = []

################################

# CHANGE VALUES TO GET DIFFERENT RESULTS
NUMBER = 100 # Number of songs looked at in the csv file
PLAYLISTS = NUMBER//2 # Number of playlists
USERS = NUMBER//4 # Number of users generated 
PLAYLIST_SONGS = 10 # Number of playlist songs looked at

################################

def get_genre(csv_file=csv_df, number=NUMBER): # Returns the genre of the first # songs and a description for them
  g = []
  i = 0
  for index, row in csv_file.iterrows():
    if i > number:
      break
    if row["artist_genre"].lower() not in g:
      g.append(row["artist_genre"])
    i += 1
  g = map(lambda x: (x, f'This is genre: {x}'), g)
  return list(g)
# genre = get_genre()
# print(genre)


def get_artist(csv_file=csv_df, number=NUMBER): # Returns the artist of the first # songs and their name, id, bio, genre, country -> RETURNS THE FIRST INSTANCE OF ARTIST FOUND (GENRE AND COUNTRY WILL BE DECIDED FROM THAT )
  artist_map = {}
  checker = []
  artist = []
  i = 0
  for index, row in csv_file.iterrows():
    if i > number:
      break
    a = row["artist_individual"]
    # aid = "artist:" + row["artist_id"][15:]
    g = row["artist_genre"]
    c = row["country"]
    if a.lower() not in checker:
      aid = i+1
      artist_map[a.lower()] = aid
      artist.append((aid, a, f'{a} is from {c} and plays music in the {g} genre', g, c)) # aid, name, bio, genre, country
      checker.append(a.lower())
    i += 1

  return artist, artist_map
# artist = get_artist()
# print(artist)


# ALBUM
# def get_album(csv_file=csv_df, number=NUMBER): #albumid, albumbname, releasedate, genre, artistid, totalsongs



def get_song(artist_map, csv_file=csv_df, number=NUMBER): #returns the first # songs and their id, title, duration, releasedate, playcount, genre, lyrics(no lyrics)
  checker = []
  songs = []
  i = 0
  for index, row in csv_file.iterrows():
    if i > number:
      break
    
    aid = artist_map[row["artist_individual"].lower()]
    t = row["track_name"]
    tid = "track:" + row["uri"][14:]
    dur = row["duration"]
    release = str(pd.to_datetime(row["release_date"]))

    play = row["streams"]
    genre = row["artist_genre"]
    lyrics = "No lyrics present as of right now"


    if tid.lower() not in checker:
      tid = i+1#"track:" + row["uri"][14:]
      # print(aid, row["artist_individual"])
      songs.append((tid, aid, t,int(float(dur)),release,int(float(play)),genre,lyrics)) # tid, artistid, title, duration, releasedate, playcount, genre, lyrics
      checker.append(tid)
    i += 1
  return songs
# songs = get_song()
# print(songs)

import random
from datetime import datetime, timedelta
import string

def generate_random_user_id(length):
    characters = string.ascii_letters + string.digits  # combining letters and digits
    user_id = ''.join(random.choice(characters) for _ in range(length))
    return user_id

def generate_random_username(words, min_length, max_length):
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(random.randint(min_length, max_length)))
    for _ in range(words):
        username += '_' + ''.join(random.choice(letters) for _ in range(random.randint(min_length, max_length)))
    return username


def get_user(csv_file=csv_df, number=NUMBER): #returns the first #//4 users with their id, username, email, password, datejoined, premiummember
  user_count = []
  username_count = []
  email_count = []
  password_count = []
  user = []
  for i in range(0, USERS):
    random_number = random.random()
    
    start_date = datetime(2010, 1, 1)  # Change the start date as needed
    end_date = datetime(2022, 12, 31)

    delta = end_date - start_date
    delta_days = delta.days
    random_days = random.randint(0, delta_days)
    random_date_joined = start_date + timedelta(days=random_days)


    uid = i+1
    username = generate_random_username(2, 5, 10)
    #creates new username if this one is taken
    while(username in username_count):
      username = generate_random_username(2, 5, 10)
    username_count.append(username)

    email = generate_random_user_id(12)
    #creates new email if this one is taken
    while(email in email_count):
      email = generate_random_user_id(12)
    email_count.append(email)
    email = email + "@gmail.com"
    
    password = generate_random_user_id(8)
    #creates new password if this one is taken
    while(password in password_count):
      password = generate_random_user_id(8)
    password_count.append(password)
    
    date_joined = str(random_date_joined)[:11]
    premium_member = random_number > 0.8

    user.append((uid, username, email, password, date_joined, premium_member))

  return user

# users = get_user()
# print(users)

#MUST HAVE A MAIN FUNCTION TO BRING EVERYTHING TOGETHER
def get_playlist(csv_file=csv_df, number=NUMBER): # playlistid, userid, name, creationdate, description, likes
  playlist_count = []
  playlist = []
  name_count = []
  users = [i+1 for i in range(0, USERS)]
  for i in range(0, PLAYLISTS):
    pid = i+1
    uid = random.choice(users)
    
    name = generate_random_username(2, 3, 8)
    #creates new username if this one is taken
    while(name in name_count):
      name = generate_random_username(2, 3, 8)
    name_count.append(name)
    
    
    start_date = datetime(2010, 1, 1)  # Change the start date as needed
    end_date = datetime(2022, 12, 31)

    delta = end_date - start_date
    delta_days = delta.days
    random_days = random.randint(0, delta_days)
    random_date_joined = start_date + timedelta(days=random_days)
    creation_date = str(random_date_joined)[:11]
    
    description = f'Description for playlist {pid}'
    likes = random.randint(0,10000)
    playlist.append((pid,uid, name, creation_date,description,int(float(likes)))) #playlistid, userid, name, creationdate, description, likes
  return playlist

# get_playlist()

def get_playlistsong(csv_file=csv_df, number=NUMBER): #playlistsongid, playlistid, tid, orderingnumber
  # order = {} # keeps track of orders in each playlist
  playlistsongs = []
  tracks = [i+1 for i in range(0, NUMBER)]
  psid = 1
  for i in range(0, PLAYLISTS): # i is the playlistid
    number_of_songs = random.randint(1,PLAYLIST_SONGS)
    count_tracks = []
    for o in range(0,number_of_songs): #plsong is the playlistsongid
      ordernumber = o+1
      pid = i+1 
      tid = random.choice(tracks)
      while tid in count_tracks:
        tid = random.choice(tracks)
      # ordernumber = order.get(pid,0) + 1
      # order[pid] = order.get(pid,0) + 1

      playlistsongs.append((psid, pid, tid, int(float(ordernumber))))
      psid += 1
  return playlistsongs

# get_playlistsong()

def main():
  genre = get_genre()
  artist, artist_map = get_artist()
  track = get_song(artist_map)
  user = get_user()
  playlist = get_playlist()
  playlist_song = get_playlistsong()


  return genre, artist, track, user, playlist, playlist_song

genre, artist, track, user, playlist, playlist_song = main()
