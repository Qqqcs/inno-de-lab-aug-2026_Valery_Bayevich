SELECT 
	c.first_name || ' ' || c.last_name AS full_name,
	c.country,
COUNT(DISTINCT o.order_id) AS total_orders,
SUM(o.amount) AS total_amount
FROM customers AS c
JOIN orders AS o ON c.customer_id = o.customer_id
JOIN shippings AS s ON c.customer_id = s.customer
GROUP BY c.customer_id, c.first_name, c.last_name, c.country
HAVING 
	COUNT(DISTINCT o.order_id) >= 2
	AND COUNT(CASE WHEN s.status = 'Delivered' THEN 1 END) >= 1
	