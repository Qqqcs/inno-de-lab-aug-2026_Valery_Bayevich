SELECT 
	item,
	COUNT(*) AS count,
	AVG(amount) AS avg_amount
FROM orders
GROUP BY item

