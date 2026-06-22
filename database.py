import sqlite3

connection = sqlite3.connect("insurance.db")

cursor = connection.cursor()


cursor.execute("""

CREATE TABLE IF NOT EXISTS customers(

customer_id TEXT PRIMARY KEY,

customer_name TEXT,

email TEXT,

phone TEXT,

policy_number TEXT

)

""")


cursor.execute("""

CREATE TABLE IF NOT EXISTS policies(

policy_id TEXT PRIMARY KEY,

customer_id TEXT,

insurance_type TEXT,

premium_amount INTEGER

)

""")


cursor.execute("""

CREATE TABLE IF NOT EXISTS claims(

claim_id TEXT PRIMARY KEY,

policy_id TEXT,

claim_amount INTEGER,

reason TEXT,

status TEXT

)

""")

connection.commit()

connection.close()

print("Database Created Successfully")