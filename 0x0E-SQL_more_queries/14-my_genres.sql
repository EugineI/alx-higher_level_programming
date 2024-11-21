-- genre for dexter
SELECT tv_genres.name AS name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE show_id = 8
ORDER BY name ASC;
