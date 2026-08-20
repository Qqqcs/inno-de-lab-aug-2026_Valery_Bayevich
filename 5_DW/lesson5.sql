CREATE TABLE DimCountry (
	CountryKey SERIAL PRIMARY KEY,
	CountryName VARCHAR(100) NOT NULL 
);

CREATE TABLE DimCity (
	CityKey SERIAL PRIMARY KEY,
	CityName VARCHAR(100) NOT NULL,
	CountryKey INT NOT NULL,
	
	FOREIGN KEY (CountryKey)
		REFERENCES DimCountry(CountryKey)
);

CREATE TABLE DimCustomer (
	CustomerKey SERIAL PRIMARY KEY,
	CustomerName VARCHAR(100) NOT NULL,
	Email VARCHAR(100) UNIQUE,
	PhoneNumber VARCHAR(30),
	CityKey INT NOT NULL, 
		
	FOREIGN KEY (CityKey)
		REFERENCES DimCity(CityKey)
);

CREATE TABLE DimCategory (
	CategoryKey SERIAL PRIMARY KEY,
	CategoryName VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE DimBrand (
	BrandKey SERIAL PRIMARY KEY,
	BrandName VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE DimDate (
	DateKey SERIAL PRIMARY KEY,
	FullDate DATE NOT NULL,
	Day INT NOT NULL,
	Month INT NOT NULL,
	Quarter INT NOT NULL,
	Year INT NOT NULL
);

CREATE TABLE DimSupplier (
	SupplierKey SERIAL PRIMARY KEY,
	SupplierName VARCHAR(100) UNIQUE NOT NULL,
	CityKey INT NOT NULL,
	
	FOREIGN KEY (CityKey)
		REFERENCES DimCity(CityKey)
);

CREATE TABLE DimProduct (
	ProductKey SERIAL PRIMARY KEY,
	ProductName VARCHAR(100) NOT NULL,
	CategoryKey INT NOT NULL,
	BrandKey INT NOT NULL,
	
	FOREIGN KEY (CategoryKey)
		REFERENCES DimCategory (CategoryKey),
	
	FOREIGN KEY (BrandKey)
		REFERENCES DimBrand(BrandKey)
);

CREATE TABLE FactSales(
	SaleID SERIAL PRIMARY KEY,
	OrderID INT NOT NULL,
	DateKey INT NOT NULL,
	CustomerKey INT NOT NULL,
	ProductKey INT NOT NULL,
	SupplierKey INT NOT NULL,
	Quantity INT NOT NULL,
	UnitPrice DECIMAL(10,2) NOT NULL,
	TotalAmount DECIMAL(12,2) NOT NULL,
	
	FOREIGN KEY (DateKey)
		REFERENCES DimDate(DateKey),
	
	FOREIGN KEY (CustomerKey)
		REFERENCES DimCustomer(CustomerKey),
	
	FOREIGN KEY (ProductKey)
		REFERENCES DimProduct(ProductKey),
		
	FOREIGN KEY (SupplierKey)
		REFERENCES DimSupplier(SupplierKey)
);

SELECT * FROM DimCustomer;
SELECT * FROM DimCategory;
SELECT * FROM DimBrand;
SELECT * FROM DimDate;
SELECT * FROM DimSupplier;
SELECT * FROM DimProduct;
SELECT * FROM FactSales;
SELECT * FROM DimCountry;
SELECT * FROM DimCity;