-- List all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres g
LEFT JOIN (
	SELECT sg.genre_id
	FROM tv_shows s
	JOIN tv_show_genres sg
	ON s.id = sg.show_id
	WHERE s.title = "Dexter"
	GROUP BY sg.genre_id
) dg
ON g.id = dg.genre_id
WHERE genre_id IS NULL
ORDER BY g.name
