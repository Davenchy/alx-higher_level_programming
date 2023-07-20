-- List all shows without Comedy genre link
SELECT s.title
FROM tv_shows s
LEFT JOIN (
	SELECT s.id
	FROM tv_shows s
	JOIN tv_show_genres sg ON s.id = sg.show_id
	JOIN tv_genres g ON g.id = sg.genre_id
	WHERE g.name = "Comedy"
) cs ON cs.id = s.id
WHERE cs.id IS NULL
ORDER BY s.title
