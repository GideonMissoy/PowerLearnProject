SELECT * FROM crowd_disasters
WHERE fatalities > 100;

SELECT * FROM human_stampedes WHERE fatalities > 50;

SELECT country, COUNT(*) AS num_stampedes
FROM human_stampedes
GROUP BY country
ORDER BY num_stampedes DESC;

