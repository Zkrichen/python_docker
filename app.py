import psycopg2

# PostgreSQL connection parameters
dbname = 'mytest'
user = 'postgres'
password = 'admin'
host = '172.20.80.1'
port = '5432'  # Usually 5432 for PostgreSQL

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Create a cursor object using the connection
    cursor = connection.cursor()

    # Define the PostgreSQL query to create the 'person' table
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS ado (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER
        );
    '''
    
    # Execute the create table query
    cursor.execute(create_table_query)
    
    # Define the query to insert a new row into the 'person' table
    insert_query = '''
        INSERT INTO ado (name, age) VALUES (%s, %s)
    '''
    
    # Data to insert into the 'person' table
    new_person_data = ('John fiit', 30)
    
    # Execute the insert query with the new person's data
    cursor.execute(insert_query, new_person_data)
    
    # Commit the transaction
    connection.commit()
    
    print("New person added to the 'person' table.")

except psycopg2.Error as e:
    print("Error while connecting to PostgreSQL:", e)

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
