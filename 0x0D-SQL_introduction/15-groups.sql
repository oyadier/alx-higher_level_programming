-- List records of save score
SELECT score,
COUNT(score) As number
FROM second_table
GROUP BY score ORDER BY score DESC;
