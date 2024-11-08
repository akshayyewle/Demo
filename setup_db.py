import sqlite3

# Setup Vendor Database
conn = sqlite3.connect('vendor_data.db')
c = conn.cursor()

# Create Table
c.execute('''
    CREATE TABLE vendors
          (
        id INTEGER PRIMARY KEY,
        vendor_name TEXT,
        regaddress_line01 TEXT,
        regaddress_line02 TEXT,
        regaddress_line03 TEXT,
        regaddress_city TEXT,
        regaddress_state TEXT,
        regaddress_country TEXT,
        regaddress_postal_code TEXT
    )
    ''')

conn.commit()
conn.close()