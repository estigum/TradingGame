USE TradingGame;

TRUNCATE TABLE Users;
DROP TABLE Users;
CREATE TABLE  Users
(
    userId int AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30),
    fullname VARCHAR(55),
    password VARCHAR(30),
    comment VARCHAR(200),
    createdBy VARCHAR(30),
    createdAt DATETIME,
    status INT,
    lastUpdatedBy VARCHAR(30),
    lastUpdatedAt DATETIME
);


