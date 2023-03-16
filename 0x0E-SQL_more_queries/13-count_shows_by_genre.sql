-- lists genres and number of shows associated with them
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres INNER JOIN tv_show_genres ON tv_genre.id = tv_show_genres.genre_id GROUP BY tv_genre.name ORDER BY number_of_shows DESC;
