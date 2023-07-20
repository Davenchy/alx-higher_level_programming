-- List all genres linked to the show Dexter
SELECT g.name
FROM tv_show_genres sg
JOIN tv_shows s on s.id = sg.show_id
JOIN tv_genres g on g.id = sg.genre_id
WHERE s.title = "Dexter"
ORDER BY g.name;
