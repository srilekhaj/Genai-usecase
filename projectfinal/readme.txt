Customer Support Chatbots
Description : 
GenAI powered chatbots to handle customer inquires related to payments, account balances, transaction history. This will be 24/7 support
for customers.

Table of Contents:
Installation:
1. Installing Python: 
install Python on your system. You can download it from the official Python website: https://www.python.org/downloads/

2. Setting up a Virtual Environment:
    a. Open a terminal or command prompt.
    b. Navigate to your project directory using the cd command.
    c. Create a virtual environment by running the command
    python -m venv venv_name

3. Activating the Virtual Environment:
venv_name\Scripts\activate

4. Installing Dependencies:
Run the following commands to install the required dependencies:
pip install langchain_google_genai streamlit chromadb psycopg2

5. Verifying Installation :
    Run the following commands to see the list of packages installed
    pip list
6. Preparing the Database:
setting up the Database to store customer information related to payments and bankings with the necessary table like Customers, Accounts, transaction_history, account_info and connect to PostgreSQL to fetch customer information, transaction records based on interactions with the chatbots.
Testcases:


Usage:
after successfull preparation of the database we need to connect to the PostgreSQL database.

Database Connection:
Download pgAdmin 4 with the following link (https://www.pgadmin.org/download/). 

Open pgAdmin 4
Add a New Server:
Right-click on the Server --> Create Server 

Enter the Server details:
In the "Create - Server" dialog, enter a name for your server in the "Name" field.
Switch to the "Connection" tab.

Enter Connection Details:
In the Connection tab
Hostname/address:  The IP address or hostname of the server where your PostgreSQL database is hosted. eg: localhost
Port: The port number on which PostgreSQL is running (default is usually 5432).
Maintenance database: The name of the default database to connect to initially (often called "postgres" by default).
Username: Your PostgreSQL username.
Password: Your PostgreSQL password.

Save Server Connection:
After entering the connection details, click on the "Save" button to save the server connection.

Connect to the Server:
After saving the server connection, you should see your server listed under the "Servers" node in the pgAdmin 4 interface.
Double-click on the server to connect to it.

Explore Databases and Objects:

Once connected, you can expand the server node to view databases, schemas, tables, and other objects within your PostgreSQL database.
You can perform various operations such as querying data, creating tables, running scripts, etc., directly from pgAdmin 4.

Explore Databases and Objects:

Once connected, you can expand the server node to view databases, schemas, tables, and other objects within your PostgreSQL database.

customers are limited to retrieving data from the database. They cannot execute any other actions such as inserting, deleting, or updating. The chatbot is programmed to only provide select queries.


Front-end:

we have used streamlit to create a user interface for interacting with the chatbot.
To run the streamlit application use the below command:
streamlit run app.py

this will open the app  with the link http://localhost:8501 in your web browser (the port number might differ).

just you can type your question the chatbot will respond based on your query

Code examples or usage scenarios:

what is my account balance?
Your account balance is $2000.00.

what is Bob Johnson's account balance?
Sorry I am unable to assist with your query at the moment

give me my last 4 transactions
Deposit	$1,500.00	04/08/2024

how to apply for a credit card?

To apply for a credit card, you have three options:
Visit a bank branch and fill out a credit card application form with the assistance of a bank representative.
Apply for a credit card through the bank's website by filling out an online application form and submitting it electronically.
Some banks allow you to apply for a credit card over the phone by calling their customer service or credit card application hotline.

