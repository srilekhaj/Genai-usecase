select * from demotable1;
insert into demotable1 values(2, 'mario');

SELECT name FROM demotable1 WHERE id = 1;


CREATE TABLE customers (
  customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  username VARCHAR(30) UNIQUE NOT NULL, -- Username for login
  password CHAR(60) NOT NULL, -- Hashed and secured password
  email VARCHAR(100) UNIQUE NOT NULL
);


INSERT INTO customers (first_name, last_name, username, password, email) 
VALUES 
('Alice', 'Smith', 'alicesmith', 'hashed_password_here', 'alice.smith@example.com'),
('Bob', 'Johnson', 'bobjohnson', 'hashed_password_here', 'bob.johnson@example.com'),
('Charlie', 'Brown', 'charliebrown', 'hashed_password_here', 'charlie.brown@example.com'),
('David', 'Lee', 'davidlee', 'hashed_password_here', 'david.lee@example.com'),
('Eve', 'Davis', 'evedavis', 'hashed_password_here', 'eve.davis@example.com');

INSERT INTO customers (first_name, last_name, username, password, email) 
VALUES 
    ('johnny', 'doe', 'johndoe', 'hashed_password', 'johnny.doe@example.com'),
    ('janey', 'smith', 'janesmith', 'hashed_password', 'janey.smith@example.com'),
    ('alisa', 'brown', 'alicebrown', 'hashed_password', 'alisa.brown@example.com'),
    ('bobby', 'lee', 'boblee', 'hashed_password', 'bobby.lee@example.com'),
    ('saran', 'wang', 'sarahwang', 'hashed_password', 'saran.wang@example.com');

select * from customers;

select balance from accounts where customer_id = (select customer_id from customers where first_name = 'alisa');

CREATE TABLE accounts (
  account_id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES customers(customer_id) NOT NULL, -- Foreign key referencing customer
  account_number VARCHAR(20) UNIQUE NOT NULL,
  account_type VARCHAR(20) NOT NULL, -- E.g., Checking, Savings
  balance DECIMAL(12, 2) NOT NULL DEFAULT 0.00, -- Account balance
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE transactions (
  transaction_id SERIAL PRIMARY KEY,
  account_id INTEGER REFERENCES accounts(account_id) NOT NULL, -- Foreign key referencing account
  transaction_type VARCHAR(20) NOT NULL, -- E.g., Deposit, Withdrawal, Transfer
  amount DECIMAL(12, 2) NOT NULL,
  transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  description VARCHAR(255)
);

CREATE TABLE account_info (
  info_id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES customers(customer_id) NOT NULL, -- Foreign key referencing customer
  info_type VARCHAR(50) NOT NULL, -- E.g., Account Balance, Available Credit
  info_value TEXT, -- Flexible data type for various information
  last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Inserting data into the 'accounts' table
INSERT INTO accounts (customer_id, account_number, account_type, balance) 
VALUES 
(1, '666666', 'Checking', 1500.00),
(2, '777777', 'Savings', 2500.00),
(3, '888888', 'Checking', 3000.00),
(4, '999999', 'Savings', 2000.00),
(5, '1010101010', 'Checking', 500.00),
(6, '666666', 'Checking', 1500.00),
(7, '777777', 'Savings', 2500.00),
(8, '888888', 'Checking', 3000.00),
(9, '999999', 'Savings', 2000.00),
(10, '1010101010', 'Checking', 500.00);

-- Inserting data into the 'transactions' table
INSERT INTO transactions (account_id, transaction_type, amount, description) 
VALUES 
(1, 'Deposit', 500.00, 'Initial deposit'),
(2, 'Deposit', 1000.00, 'Initial deposit'),
(3, 'Deposit', 2000.00, 'Initial deposit'),
(4, 'Deposit', 1500.00, 'Initial deposit'),
(5, 'Deposit', 300.00, 'Initial deposit'),
(6, 'Deposit', 500.00, 'Initial deposit'),
(7, 'Deposit', 1000.00, 'Initial deposit'),
(8, 'Deposit', 2000.00, 'Initial deposit'),
(9, 'Deposit', 1500.00, 'Initial deposit'),
(10, 'Deposit', 300.00, 'Initial deposit');

-- Inserting data into the 'account_info' table
INSERT INTO account_info (customer_id, info_type, info_value) 
VALUES 
(1, 'Account Balance', '1500.00'),
(2, 'Account Balance', '2500.00'),
(3, 'Account Balance', '3000.00'),
(4, 'Account Balance', '2000.00'),
(5, 'Account Balance', '500.00'),
(6, 'Account Balance', '1500.00'),
(7, 'Account Balance', '2500.00'),
(8, 'Account Balance', '3000.00'),
(9, 'Account Balance', '2000.00'),
(10, 'Account Balance', '500.00');

select * from account_info;
select * from transactions;
select * from accounts;
SELECT customer_id FROM customers WHERE username='alicesmith';
SELECT balance FROM accounts WHERE customer_id = (SELECT customer_id FROM customers WHERE first_name = 'Alice' AND last_name = 'Smith');