-- select city and the average temp from temperatures table and order by desc avg_temp
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC
