from . import get_db

'''
try:
    conn = get_db()
    c = conn.cursor(dictionary=True)
    # Start a transaction
    c.execute("START TRANSACTION")

    # Insert a new user into the User table
    c.execute("INSERT INTO User (name) VALUES (?)", ('Your Name',))
    # Get the ID of the newly inserted user
    user_id = c.lastrowid

    # Insert credentials for the new user into the Credentials table
    c.execute("INSERT INTO Credentials (userid, password) VALUES (?, ?)", (user_id, 'Your Password'))

    # Commit the transaction
    conn.commit()

except Exception as e:
    # If an error occurred, rollback the transaction
    conn.rollback()
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    conn.close()
    '''