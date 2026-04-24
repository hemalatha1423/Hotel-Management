import mysql.connector as mycon

# Establish the database connection
con = mycon.connect(host='localhost', user='root', password="user")
cur = con.cursor()

# Create the database and use it
cur.execute("CREATE DATABASE IF NOT EXISTS hotel_management")
cur.execute("USE hotel_management")

# Create tables
cur.execute("""
    CREATE TABLE IF NOT EXISTS HOTEL (
        hotel_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        phone VARCHAR(20),
        email VARCHAR(255),
        stars INT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS STAFF (
        staff_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        hotel_id INT,
        position VARCHAR(255),
        salary DECIMAL(10, 2),
        dateofbirth DATE,
        phone VARCHAR(20),
        email VARCHAR(255),
        hire_date DATE,
        FOREIGN KEY (hotel_id) REFERENCES HOTEL(hotel_id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS ROOMTYPE (
        type_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        price_per_day DECIMAL(10, 2),
        capacity INT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS ROOM (
        room_no INT PRIMARY KEY,
        hotel_no INT,
        type_id INT,
        status VARCHAR(50),
        FOREIGN KEY (hotel_no) REFERENCES HOTEL(hotel_id),
        FOREIGN KEY (type_id) REFERENCES ROOMTYPE(type_id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS GUEST (
        guest_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        dateofbirth DATE,
        address VARCHAR(255),
        phone VARCHAR(20),
        email VARCHAR(255),
        proof VARCHAR(255)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS BOOKING (
        booking_id INT AUTO_INCREMENT PRIMARY KEY,
        guest_id INT,
        room_no INT,
        checkin_date DATE,
        checkout_date DATE,
        total_amount DECIMAL(10, 2),
        FOREIGN KEY (guest_id) REFERENCES GUEST(guest_id),
        FOREIGN KEY (room_no) REFERENCES ROOM(room_no)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS PAYMENT (
        payment_id INT AUTO_INCREMENT PRIMARY KEY,
        booking_id INT,
        amount DECIMAL(10, 2),
        payment_date DATE,
        payment_method VARCHAR(50),
        FOREIGN KEY (booking_id) REFERENCES BOOKING(booking_id)
    )
""")
con.commit()

# Function to display records
def display_records(table):
    query = f"SELECT * FROM {table}"
    cur.execute(query)
    result = cur.fetchall()
    for row in result:
        print(" | ".join(map(str, row)))

# Function to insert data into HOTEL
def insert_hotel():
    name = input("Enter Hotel Name: ")
    address = input("Enter Hotel Address: ")
    phone = input("Enter Hotel Phone: ")
    email = input("Enter Hotel Email: ")
    stars = int(input("Enter Hotel Stars: "))
    query = "INSERT INTO HOTEL (name, address, phone, email, stars) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(query, (name, address, phone, email, stars))
    con.commit()
    print("## Hotel Inserted ##")

# Function to insert data into STAFF
def insert_staff():
    name = input("Enter Staff Name: ")
    hotel_id = int(input("Enter Hotel ID: "))
    position = input("Enter Position: ")
    salary = float(input("Enter Salary: "))
    dateofbirth = input("Enter Date of Birth (YYYY-MM-DD): ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    hire_date = input("Enter Hire Date (YYYY-MM-DD): ")
    query = "INSERT INTO STAFF (name, hotel_id, position, salary, dateofbirth, phone, email, hire_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(query, (name, hotel_id, position, salary, dateofbirth, phone, email, hire_date))
    con.commit()
    print("## Staff Inserted ##")

# Function to insert data into ROOMTYPE
def insert_roomtype():
    name = input("Enter Room Type Name: ")
    description = input("Enter Description: ")
    price_per_day = float(input("Enter Price per Day: "))
    capacity = int(input("Enter Capacity: "))
    query = "INSERT INTO ROOMTYPE (name, description, price_per_day, capacity) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (name, description, price_per_day, capacity))
    con.commit()
    print("## Room Type Inserted ##")

# Function to insert data into ROOM
def insert_room():
    room_no = int(input("Enter Room Number: "))
    hotel_no = int(input("Enter Hotel Number: "))
    type_id = int(input("Enter Room Type ID: "))
    status = input("Enter Status: ")
    query = "INSERT INTO ROOM (room_no, hotel_no, type_id, status) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (room_no, hotel_no, type_id, status))
    con.commit()
    print("## Room Inserted ##")

# Function to insert data into GUEST
def insert_guest():
    name = input("Enter Guest Name: ")
    dateofbirth = input("Enter Date of Birth (YYYY-MM-DD): ")
    address = input("Enter Address: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    proof = input("Enter Proof: ")
    query = "INSERT INTO GUEST (name, dateofbirth, address, phone, email, proof) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(query, (name, dateofbirth, address, phone, email, proof))
    con.commit()
    print("## Guest Inserted ##")

# Function to insert data into BOOKING
def insert_booking():
    guest_id = int(input("Enter Guest ID: "))
    room_no = int(input("Enter Room Number: "))
    checkin_date = input("Enter Check-in Date (YYYY-MM-DD): ")
    checkout_date = input("Enter Check-out Date (YYYY-MM-DD): ")
    total_amount = float(input("Enter Total Amount: "))
    query = "INSERT INTO BOOKING (guest_id, room_no, checkin_date, checkout_date, total_amount) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(query, (guest_id, room_no, checkin_date, checkout_date, total_amount))
    con.commit()
    print("## Booking Inserted ##")

# Function to insert data into PAYMENT
def insert_payment():
    booking_id = int(input("Enter Booking ID: "))
    amount = float(input("Enter Amount: "))
    payment_date = input("Enter Payment Date (YYYY-MM-DD): ")
    payment_method = input("Enter Payment Method: ")
    query = "INSERT INTO PAYMENT (booking_id, amount, payment_date, payment_method) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (booking_id, amount, payment_date, payment_method))
    con.commit()
    print("## Payment Inserted ##")

# Function to delete a record from a table
def delete_record(table, id_column):
    record_id = int(input(f"Enter {id_column} to Delete: "))
    query = f"DELETE FROM {table} WHERE {id_column} = %s"
    cur.execute(query, (record_id,))
    con.commit()
    print(f"## {table[:-1].capitalize()} Deleted ##")

# Function to update a record in a table
def update_record(table, id_column, columns):
    record_id = int(input(f"Enter {id_column} to Update: "))
    values = [input(f"Enter New {col.replace('_', ' ').capitalize()}: ") for col in columns]
    set_clause = ", ".join([f"{col} = %s" for col in columns])
    query = f"UPDATE {table} SET {set_clause} WHERE {id_column} = %s"
    cur.execute(query, (*values, record_id))
    con.commit()
    print(f"## {table[:-1].capitalize()} Updated ##")
# Main program loop
choice = None
while choice != 0:
    print("\nHotel Management System")
    print("1. ADD HOTEL")
    print("2. DELETE HOTEL")
    print("3. UPDATE HOTEL")
    print("4. DISPLAY HOTELS")
    print("5. ADD STAFF")
    print("6. DELETE STAFF")
    print("7. UPDATE STAFF")
    print("8. DISPLAY STAFF")
    print("9. ADD ROOMTYPE")
    print("10. DELETE ROOMTYPE")
    print("11. UPDATE ROOMTYPE")
    print("12. DISPLAY ROOMTYPES")
    print("13. ADD ROOM")
    print("14. DELETE ROOM")
    print("15. UPDATE ROOM")
    print("16. DISPLAY ROOMS")
    print("17. ADD GUEST")
    print("18. DELETE GUEST")
    print("19. UPDATE GUEST")
    print("20. DISPLAY GUESTS")
    print("21. ADD BOOKING")
    print("22. DELETE BOOKING")
    print("23. UPDATE BOOKING")
    print("24. DISPLAY BOOKINGS")
    print("25. ADD PAYMENT")
    print("26. DELETE PAYMENT")
    print("27. UPDATE PAYMENT")
    print("28. DISPLAY PAYMENTS")
    print("0. EXIT")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        insert_hotel()
    elif choice == 2:
        delete_record("HOTEL", "hotel_id")
    elif choice == 3:
        update_record("HOTEL", "hotel_id", ["name", "address", "phone", "email", "stars"])
    elif choice == 4:
        display_records("HOTEL")
    elif choice == 5:
        insert_staff()
    elif choice == 6:
        delete_record("STAFF", "staff_id")
    elif choice == 7:
        update_record("STAFF", "staff_id", ["name", "hotel_id", "position", "salary", "dateofbirth", "phone", "email", "hire_date"])
    elif choice == 8:
        display_records("STAFF")
    elif choice == 9:
        insert_roomtype()
    elif choice == 10:
        delete_record("ROOMTYPE", "type_id")
    elif choice == 11:
        update_record("ROOMTYPE", "type_id", ["name", "description", "price_per_day", "capacity"])
    elif choice == 12:
        display_records("ROOMTYPE")
    elif choice == 13:
        insert_room()
    elif choice == 14:
        delete_record("ROOM", "room_no")
    elif choice == 15:
        update_record("ROOM", "room_no", ["hotel_no", "type_id", "status"])
    elif choice == 16:
        display_records("ROOM")
    elif choice == 17:
        insert_guest()
    elif choice == 18:
        delete_record("GUEST", "guest_id")
    elif choice == 19:
        update_record("GUEST", "guest_id", ["name", "dateofbirth", "address", "phone", "email", "proof"])
    elif choice == 20:
        display_records("GUEST")
    elif choice == 21:
        insert_booking()
    elif choice == 22:
        delete_record("BOOKING", "booking_id")
    elif choice == 23:
        update_record("BOOKING", "booking_id", ["guest_id", "room_no", "checkin_date", "checkout_date", "total_amount"])
    elif choice == 24:
        display_records("BOOKING")
    elif choice == 25:
        insert_payment()
    elif choice == 26:
        delete_record("PAYMENT", "payment_id")
    elif choice == 27:
        update_record("PAYMENT", "payment_id", ["booking_id", "amount", "payment_date", "payment_method"])
    elif choice == 28:
        display_records("PAYMENT")
    elif choice == 0:
        print("Exiting the program...")
    else:
        print("Invalid choice! Please try again.")
    

