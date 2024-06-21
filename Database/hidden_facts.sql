SELECT country, COUNT(*) AS num_stampedes
FROM human_stampedes
GROUP BY country
ORDER BY num_stampedes DESC
LIMIT 1;
