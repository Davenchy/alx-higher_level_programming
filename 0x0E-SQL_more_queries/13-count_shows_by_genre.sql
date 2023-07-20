-- list the genre and the number of shows linked to it
SELECT g.name AS genre, COUNT(g.name) AS number_of_shows
FROM tv_show_genres sg
JOIN tv_genres g
ON g.id = sg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
