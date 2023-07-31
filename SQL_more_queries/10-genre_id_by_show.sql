-- TV_SHOWS
CREATE DATABASE hbtn_0d_tvshows;
mysql -u root -p hbtn_0d_tvshows < hbtn_0d_tvshows.sql
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
