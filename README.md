# PostgreSQL Project

This is our project for Fall 2023 CSE460 

 ## Response

 - For our data source, we found an open-source dataset on Kaggle which had Spotify’s Top 200 Songs streaming data from 2016 to 2022.
A link can be found here: https://www.kaggle.com/datasets/yelexa/spotify200. This dataset wasn’t comprehensive enough to populate all of our tables but helped us fill data for our genre, artist, and song tables. For our playlist, playlistsongs, and appuser tables, we used Python to generate random data to fill these tables out.

## Building Tables

 - In order to build the tables, you can use the create.sql file provided to automatically generate the 6 tables into your postgres database. This script contains the necessary references for foreign keys, default values, and cascading effects. 

## Importing Data

 - To import data into the database, we’ve provided a Python script to take the data from the Kaggle dataset and place it in your local database. First, make sure you have downloaded the Kaggle dataset above. In fetch_data.py, change the constants of NUMBER, PLAYLISTS, USERS, OR PLAYLIST_SONGS; if you’d like to adjust the amount of songs, playlists, users, or playlist songs inserted into your database. Change the value of “csv_file” to whatever path your Kaggle dataset CSV is located. Once these are updated, you can move onto the “script_sql.py” file. 

 - In this file, adjust the variables of your database to ensure that a connection is made to your postgresql database. These fields include the name of your database, the database username, the password, host, and port of your postgresql database. Once all these fields have been adjusted, run the “script_sql.py”. Upon completion, this script will fill your database with the specified amount of lines of data from “fetch_data.py”.
