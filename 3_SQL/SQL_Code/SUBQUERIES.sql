SELECT
	c.first_name,
	c.last_name,
	SUM(o.amount) AS amount
FROM customers AS c
JOIN orders AS o
ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY amount desc
LIMIT 1;
