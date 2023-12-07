import psycopg2
# from list_data import genre, artist, track, user , playlist, playlist_song

from fetch_data import genre, artist, track, user , playlist, playlist_song

import os
from dotenv import load_dotenv

load_dotenv()

DB_PASS = os.getenv('db_password')

# Database connection parameters
db_host = 'localhost'  # Replace with your database host
db_name = 'Music_460_Project'  # Replace with your database name
db_user = 'postgres'  # Replace with your database username
db_password = DB_PASS  # Replace with your database password
db_port = 5432  # Replace with your database port (default PostgreSQL port is 5432)

# Establish a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    print("Connected to PostgreSQL database")
    
    for g in genre:
        insert_script = 'INSERT INTO genre (genrename, description) VALUES (%s, %s)'
        insert_value = (g[0], g[1])
        cursor.execute(insert_script, insert_value)
    for a in artist:
        insert_script = 'INSERT INTO artists (artistid, name, biography, genre, country) VALUES (%s, %s, %s, %s, %s)'
        insert_value = (a[0], a[1], a[2], a[3], a[4])
        cursor.execute(insert_script, insert_value)
    for t in track:
        insert_script = 'INSERT INTO song (trackid, artistid, title, duration, releasedate, playcount, genre, lyrics) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        insert_value = (t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7])
        cursor.execute(insert_script, insert_value)
    for u in user:
        insert_script = 'INSERT INTO appuser (userid, username, email, user_password, datejoined, premiummember) VALUES (%s, %s, %s, %s, %s, %s)'
        insert_value = (u[0], u[1], u[2], u[3], u[4], u[5])
        cursor.execute(insert_script, insert_value)
    for p in playlist:
        insert_script = 'INSERT INTO playlist (playlistid, userid, name, creationdate, description, likes) VALUES (%s, %s, %s, %s, %s, %s)'
        insert_value = (p[0], p[1], p[2], p[3], p[4], p[5])
        cursor.execute(insert_script, insert_value)
    for ps in playlist_song:
        insert_script = 'INSERT INTO playlistsongs (playlistsongid, playlistid, songid, orderingnumber) VALUES (%s, %s, %s, %s)'
        insert_value = (ps[0], ps[1], ps[2], ps[3])
        cursor.execute(insert_script, insert_value)
    # output = cursor.fetchone()
    # print(output)

    connection.commit()

    # Close communication with the database
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)