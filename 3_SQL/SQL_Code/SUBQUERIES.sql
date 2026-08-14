SELECT
    c.first_name,
    c.last_name,
    o.amount
FROM customers AS c
JOIN orders AS o
    ON o.customer_id = c.customer_id
WHERE o.amount = (
    SELECT MAX(amount)
    FROM orders
);