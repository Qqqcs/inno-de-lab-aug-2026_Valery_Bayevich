SELECT
	p.ProductName,
	SUM(f.TotalAmount) AS TotalRevenue
FROM FactSales f
JOIN DimProduct p
	ON f.ProductKey = p.ProductKey
GROUP BY p.ProductName
ORDER BY TOTALREVENUE DESC; --Какие товары принесли наибольшую выручку?

SELECT
	c.CategoryName,
	SUM(f.TotalAmount) AS TotalRevenue
FROM FactSales f
JOIN DimProduct p
	ON f.ProductKey = p.ProductKey
JOIN DimCategory c
	ON p.CategoryKey = c.CategoryKey
GROUP BY c.CategoryName
ORDER BY TotalRevenue DESC; --Какая выручка по категориям товаров? 

SELECT
	b.BrandName,
	SUM(f.Quantity) AS TotalQuantity
FROM FactSales f
JOIN DimProduct p
	ON f.ProductKey = p.ProductKey
JOIN DimBrand b
	ON p.BrandKey = b.BrandKey
GROUP BY b.BrandName
ORDER BY TotalQuantity DESC; -- Какие бренды продаются лучше всего? (по количеству)

SELECT 
	d.Year,
	d.Month,
	SUM(f.TotalAmount) AS TotalRevenue
FROM FactSales f
JOIN DimDate d
	ON f.DateKey = d.DateKey
GROUP BY d.Year, d.Month
ORDER BY d.Year, d.Month; -- Как меняется выручка по месяцам?

SELECT
	co.CountryName,
	SUM(f.TotalAmount) AS TotalRevenue
FROM FactSales f
JOIN DimCustomer c
	ON f.CustomerKey = c.CustomerKey
JOIN DimCity ci
	ON c.CityKey = ci.CityKey
JOIN DimCountry co
	ON ci.CountryKey = co.CountryKey
GROUP BY co.CountryName
ORDER BY TotalRevenue DESC; -- Из каких стран покуптели приностя больше всего выручки?