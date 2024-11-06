import streamlit as st 
import os 

# App Configuration
st.set_page_config(page_title="Rotork Vendor Data Verification App", page_icon=":bar_chart:", layout="wide")

# Setup a SQLite Database
import sqlite3
conn = sqlite3.connect('vendor_data.db')
c = conn.cursor()

# Check if Vendor Database File Exists
if not os.path.exists('vendor_data.db'):
        st.error("Vendor Database File Not Found. Please Check Vendor Database File.")
        st.stop()

# Sidebar
st.sidebar.header("Please Filter Here:")

# Main Page 
st.title("Rotork Vendor Data Verification App")

# Vendor Basic Details
st.subheader("Vendor Basic Details")
input00 = st.text_input("Vendor Name",placeholder="Vendor Name")

# Vendor Registered Address
st.subheader("Vendor Registered Address")
input01 = st.text_input(label="Address Line 01",placeholder="Address Line 01")
input02 = st.text_input("Address Line 02", placeholder="Address Line 02")
input03 = st.text_input("Address Line 03", placeholder="Address Line 03")
input04 = st.text_input("City", placeholder="City")
input05 = st.text_input("State", placeholder="State")
input06 = st.text_input("Country", placeholder="Country")
input07 = st.text_input("Postal Code", placeholder="Postal Code")

# Check if Registered Address is the same as Billing/Delivery Address
input08 = st.toggle("Is this the same as billing address?")
input09 = st.toggle("Is this the same as delivery address?")

# Vendor Billing Address
st.subheader("Vendor Billing Address")
if input08:
    input10 = input01 # Address Line 01
    input11 = input02 # Address Line 02
    input12 = input03 # Address Line 03
    input13 = input04 # City
    input14 = input05 # State
    input15 = input06 # Country
    input16 = input07 # Postal Code

else:
    input10 = st.text_input("Address Line 01",placeholder="Address Line 01",key="input10")
    input11 = st.text_input("Address Line 02",placeholder="Address Line 02",key="input11")
    input12 = st.text_input("Address Line 03",placeholder="Address Line 03",key="input12")
    input13 = st.text_input("City",placeholder="City",key="input13")
    input14 = st.text_input("State",placeholder="State",key="input14")
    input15 = st.text_input("Country",placeholder="Country",key="input15")
    input16 = st.text_input("Postal Code",placeholder="Postal Code",key="input16")

# Add Submit Button & 
if st.button("Submit"):
    # Insert Data into Database
    c.execute(f''' 
              INSERT INTO vendor_data (
                                    vendor_name, 
                                    regaddress_line_01, regaddress_line_02, regaddress_line_03,
                                    regaddress_city, regaddress_state, regaddress_country, regaddress_postal_code)
              VALUES ({input00},{input01}, {input02}, {input03},{input04}, {input05}, {input06}, {input07})
              ''')
    st.success("Data Submitted Successfully!")