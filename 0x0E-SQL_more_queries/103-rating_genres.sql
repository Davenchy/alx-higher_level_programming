-- List all genres with the rating for each genre
SELECT g.name, SUM(rate) AS rating
FROM tv_genres g
JOIN tv_show_genres sg ON sg.genre_id = g.id
JOIN tv_shows s ON s.id = sg.show_id
JOIN tv_show_ratings r ON r.show_id = s.id
GROUP BY g.name
ORDER BY rating DESC;
