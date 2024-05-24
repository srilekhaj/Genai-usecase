from langchain_google_genai import ChatGoogleGenerativeAI
import psycopg2
from langchain_google_genai import GoogleGenerativeAIEmbeddings


llm = ChatGoogleGenerativeAI(
        google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
        model="gemini-pro",
        convert_system_message_to_human=True
        
    )


embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
    model="models/embedding-001",


)


def dbconnection(sqlresult):
    conn = psycopg2.connect(
    dbname="newbank",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
    )
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SQL query
    cur.execute(sqlresult)

    # Fetch data
    rows = cur.fetchall()
    rows = [str(row) for row in rows]
    return " ".join(rows)
    for row in rows:
        return row

    # Commit and close connection
    conn.commit()
    cur.close()
    conn.close()


def sqlquery_retriever(Query):
    #Query = Query.casefold()


    template = f'''Analyze the given query and convert the given query to an PostgreSQL query. 
    
    Query : 
    {Query} 

    The Query table names and column names are as follows :
    Table names:
    1. customers
    2. accounts
    3. transactions
    4. account_info

    Column names:
    1. customers:
    - customer_id
    - first_name
    - last_name
    - username
    - password
    - email

    2. accounts:
    - account_id
    - customer_id
    - account_number
    - account_type
    - balance
    - created_at

    3. transactions:
    - transaction_id
    - account_id
    - transaction_type
    - amount
    - transaction_date
    - description

    4. account_info:
    - info_id
    - customer_id
    - info_type
    - info_value
    - last_updated 

    Provide your response in the below format 
    PostgreSQL Query: <provide your response here in a single line also the sql code should not have single backticks or triple backticks or double backticks in beginning or end and sql word in output> 

    '''
    result = llm.invoke(template)
    res = result.content
    print(res)




    # Regular expression pattern to extract content after "Postgresql Query:"
    import re
    pattern = r'PostgreSQL Query:\s*(.*)'
    

    # Extracting content using regular expression
    result = re.search(pattern, res)
    if result:
        extracted_content = result.group(1).strip()
        sqlresult = extracted_content
        #sqlresult = sqlresult.casefold()  #fun1 #sqlresult select 
        print(sqlresult)
        sp = sqlresult.split()
        if sp[0] == 'SELECT':
            return dbconnection(sqlresult),res,1
        else:
            return "This action cannot be performed",res,0
    else:
        return "Content not found.",res,0

