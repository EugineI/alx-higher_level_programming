-- only comedy(genre_id = 5) shows
SELECT tv_shows.title AS title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id = 5
ORDER BY title ASC;
