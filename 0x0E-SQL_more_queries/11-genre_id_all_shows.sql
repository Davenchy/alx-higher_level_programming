-- Lists all shows and their genre_id
SELECT s.title, sg.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres sg
ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id;
