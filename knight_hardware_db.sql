USE MASTER;

GO

DROP DATABASE IF EXISTS KnightHardwareDB

GO

CREATE DATABASE KnightHardwareDB

GO

USE KnightHardwareDB;

CREATE TABLE Customers (
    CustomerNumber int PRIMARY KEY,
    CustomerName VARCHAR(150),
    City VARCHAR(50),
    State VARCHAR(50)
);

CREATE TABLE Parts (
    PartNumber VARCHAR(12) PRIMARY KEY,
    PartDescription VARCHAR(100),
    InventoryOnHand int,
    Price DECIMAL(10, 2)
);

CREATE TABLE Orders (
    OrderNumber int PRIMARY KEY,
    CustomerNumber int,
    OrderDate DATE,
    FOREIGN KEY (CustomerNumber)
    REFERENCES Customers(CustomerNumber)
);

CREATE TABLE OrderDetails (
    OrderNumber int,
    PartNumber VARCHAR(12),
    NumberOrdered int,
    PRIMARY KEY (OrderNumber, PartNumber),

    FOREIGN KEY (OrderNumber)
    REFERENCES Orders(OrderNumber),

    FOREIGN KEY (PartNumber)
    REFERENCES Parts(PartNumber)
);

INSERT INTO Customers VALUES
(148, 'Als Appliance and Sport', 'Fillmore', 'FL'),
(282, 'Brookings Direct', 'Grove', 'FL'),
(356, 'Fergusons', 'Northfield', 'FL'),
(408, 'The Everything Shop', 'Crystal', 'FL'),
(608, 'Johnsons Department Store', 'Sheldon', 'FL');

INSERT INTO Parts VALUES
('AT94', 'Iron', 50, 24.95),
('DR93', 'Gas Range', 8, 495),
('KT03', 'Dishwasher', 8, 595),
('DW11', 'Washer', 12, 399.99),
('KL62', 'Dryer', 12, 349.95),
('BV06', 'Home Gym', 45, 794.95),
('CD52', 'Microwave Oven', 32, 165),
('KV29', 'Treadmill', 9, 1390);

INSERT INTO Orders VALUES
(21608, 148, '2017-10-20'),
(21610, 356, '2017-10-19'),
(21613, 408, '2017-10-22'),
(21614, 282, '2017-10-21'),
(21617, 608, '2017-10-23'),
(21619, 148, '2017-10-23'),
(21623, 608, '2017-10-21');

INSERT INTO OrderDetails VALUES
(21608, 'AT94', 11),
(21610, 'DR93', 1),
(21610, 'DW11', 1),
(21613, 'KL62', 4),
(21614, 'KT03', 2),
(21617, 'BV06', 2),
(21617, 'CD52', 4),
(21619, 'DR93', 1),
(21623, 'KV29', 2);