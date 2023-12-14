-- List all the empty value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
