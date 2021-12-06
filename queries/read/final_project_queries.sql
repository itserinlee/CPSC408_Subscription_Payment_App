CREATE DATABASE IF NOT EXISTS final_project;

USE final_project;

DROP TABLE IF EXISTS payment;
DROP TABLE IF EXISTS subscription;
DROP TABLE IF EXISTS profile;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS magazine;

CREATE TABLE IF NOT EXISTS magazine (
magID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
magazineName VARCHAR(50),
cost FLOAT NOT NULL,
category VARCHAR(50),
recStatus BOOLEAN,
recCreateDate DATE DEFAULT (CURRENT_DATE)
);

-- get all magazines
SELECT *
FROM magazine;

-- get magazine by name
-- SELECT *
-- FROM magazine
-- WHERE magazineName = (%s);

-- get all science category magazines
SELECT magazineName, category
FROM magazine
WHERE category LIKE "%Science%";

-- count magazine by year
SELECT COUNT(magID) AS CountOfMag
FROM magazine
WHERE recCreateDate LIKE '2019-%';

-- SELECT COUNT(magID) AS CountOfMag
-- FROM magazine
-- WHERE recCreateDate LIKE '(%s)-%';

-- avg cost of magazine categories (group by)
SELECT category, COUNT(category) AS CountOfCategory, ROUND(AVG(cost), 2) AS AvgCost
FROM magazine
GROUP BY category
ORDER BY AvgCost DESC;

CREATE TABLE IF NOT EXISTS customer (
custID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
firstName VARCHAR(50),
lastName VARCHAR(50),
username VARCHAR(50),
password VARCHAR(50),
recCreateDate DATE DEFAULT (CURRENT_DATE)
);

-- get all customer
SELECT *
FROM customer;

-- count num of customers by user inputted year
SELECT COUNT(custID) AS CountOfCust
FROM customer
WHERE recCreateDate LIKE '2015-%';


CREATE TABLE IF NOT EXISTS profile (
custContID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
custID INTEGER NOT NULL,
phoneNum CHAR(12) NOT NULL,
zipCode CHAR(5) NOT NULL,
state CHAR(2) NOT NULL,
city VARCHAR(100) NOT NULL,
streetAddress VARCHAR(150) NOT NULL,
contactType BOOLEAN,
recUpdateDate DATE DEFAULT (CURRENT_DATE),
recStatus BOOLEAN,
startDate DATE,
endDate DATE,
CONSTRAINT FK_profile_custID FOREIGN KEY (custID) REFERENCES customer(custID)
);

SELECT *
FROM profile;

-- count number of profiles by state
SELECT COUNT(custContID) numPerState, state 
FROM profile
GROUP BY state;

-- count most common first name by state

-- number of subs per city (desc order) [2 inner joins with 3 tables]
SELECT COUNT(subID) AS NumMags, P.city
FROM subscription AS S
INNER JOIN Customer AS C ON S.custID = C.custID 
INNER JOIN Profile AS P ON C.custID = P.custID
GROUP BY P.city
ORDER BY NumMags DESC;

-- most popular category by zip code (desc order) [3 inner joins with 4 tables]
SELECT MAX(M.category) AS numOfCategory, P.zipCode AS zipCode
FROM magazine AS M
INNER JOIN subscription AS S ON M.magID = S.magID
INNER JOIN customer AS C ON S.custID = C.custID
INNER JOIN profile AS P ON C.custID = P.custID
GROUP BY zipCode
ORDER BY zipCode DESC;

-- max, avg, and min subscription days
SELECT MAX(ABS(DATEDIFF(endDate, startDate))) AS maxNumDays, 
FLOOR(AVG(ABS(DATEDIFF(endDate, startDate)))) AS avgNumDays, 
MIN(ABS(DATEDIFF(endDate, startDate))) AS minNumDays
FROM subscription;

-- max, avg, and min payments by states
SELECT p2.state AS state, 
MAX(paymentAmount) as maxPayment, 
ROUND(AVG(paymentAmount), 2) AS avgPayment, 
MIN(paymentAmount) AS minPayment
FROM payment AS p
INNER JOIN subscription AS s
ON p.subID = s.subID
INNER JOIN profile AS p2
ON s.custID = p2.custID
GROUP BY state;

CREATE TABLE IF NOT EXISTS subscription (
magID INTEGER NOT NULL,
custID INTEGER NOT NULL,
subID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
paymentCompleted BOOLEAN,
startDate DATE,
endDate DATE,
numMagsMailed INTEGER,
CONSTRAINT FK_subscription_magID FOREIGN KEY (magID) REFERENCES magazine(magID),
CONSTRAINT FK_subscription_custID FOREIGN KEY (custID) REFERENCES customer(custID)
);

SELECT *
FROM subscription;

CREATE TABLE IF NOT EXISTS payment (
cardCode INTEGER,
cardNumber VARCHAR(25),
payID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
subID INTEGER NOT NULL,
paymentAmount FLOAT NOT NULL,
paymentType BOOLEAN,
paymentDate DATE,
recCreateDate DATE DEFAULT (CURRENT_DATE),
CONSTRAINT FK_subscription_subID FOREIGN KEY (subID) REFERENCES subscription(subID)
);

SELECT *
FROM payment;