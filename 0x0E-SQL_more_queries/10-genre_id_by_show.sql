-- List all shows that have at least one genre linked
SELECT s.title, g.id as genre_id
FROM tv_show_genres sg
	JOIN tv_shows s
	JOIN tv_genres g
WHERE sg.show_id = s.id AND sg.genre_id = g.id
ORDER BY s.title, g.id;
