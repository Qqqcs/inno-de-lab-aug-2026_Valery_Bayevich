SELECT 
	s.status,
	c.first_name,
	c.last_name
FROM CUSTOMERS c
JOIN SHIPPINGS s
ON c.customer_id = s.customer;