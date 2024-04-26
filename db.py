import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('hospital.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                address TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                specialization TEXT,
                contact TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY,
                patient_id INTEGER,
                doctor_id INTEGER,
                date TEXT,
                FOREIGN KEY(patient_id) REFERENCES patients(id),
                FOREIGN KEY(doctor_id) REFERENCES doctors(id))''')

conn.commit()
