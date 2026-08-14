SELECT
	COUNT(*) AS count,
	country
FROM customers
GROUP BY country 
