import psycopg2

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
    
    tables = [
    "CREATE TABLE Genre ( GenreName TEXT PRIMARY KEY, Description TEXT );" ,

    "CREATE TABLE Artists ( ArtistID SERIAL PRIMARY KEY, Name TEXT, Biography TEXT DEFAULT '', Genre TEXT REFERENCES Genre(GenreName) ON DELETE SET NULL, Country TEXT );" ,

    "CREATE TABLE Song ( TrackID SERIAL PRIMARY KEY, artistid Integer REFERENCES Artists(ArtistId) ON DELETE CASCADE, Title TEXT, Duration INTEGER, ReleaseDate DATE, PlayCount INTEGER, Genre TEXT REFERENCES Genre(GenreName) ON DELETE SET NULL, Lyrics TEXT DEFAULT NULL ); ",
    "CREATE TABLE AppUser ( UserID SERIAL PRIMARY KEY, Username TEXT, Email TEXT, user_Password TEXT, DateJoined DATE, PremiumMember BOOLEAN DEFAULT false ); ",
    "CREATE TABLE Playlist ( PlaylistID SERIAL PRIMARY KEY, UserID INTEGER REFERENCES AppUser(UserID) ON DELETE CASCADE, Name TEXT, CreationDate DATE, Description TEXT DEFAULT '', Likes INTEGER DEFAULT 0 ); ",
    "CREATE TABLE PlaylistSongs ( PlaylistSongID SERIAL PRIMARY KEY, PlaylistID INTEGER REFERENCES Playlist(PlaylistID) ON DELETE CASCADE, SongID INTEGER REFERENCES Song(TrackID) ON DELETE CASCADE, OrderingNumber INTEGER );"
    ]
    for table_script in tables:
        cursor.execute(table_script)
        
    connection.commit()

    # Close communication with the database
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)