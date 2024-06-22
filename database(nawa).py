import sqlite3
import os
import sys

# Connect to the database (or create it)
conn = sqlite3.connect('CallADoctor.db')

# Create a cursor object
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('john', 'qwerty')")

# Create the Patient table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Patient (
    Patient_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Patient_Name TEXT NOT NULL,
    Patient_Age INTEGER NOT NULL,
    Patient_Sex TEXT NOT NULL,
    Patient_Address TEXT NOT NULL,
    Patient_PhoneNo TEXT NOT NULL,
    Patient_Email TEXT NOT NULL,
    Patient_Password TEXT NOT NULL
)
''')

# Create the Clinic table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clinic (
    Clinic_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Clinic_Name TEXT NOT NULL,
    Clinic_Location TEXT NOT NULL,
    Clinic_Password TEXT NOT NULL,
    Clinic_Approval TEXT NOT NULL
)
''')

# Create the Doctor table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Doctor (
    Doctor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Clinic_ID INTEGER,
    Doctor_Name TEXT NOT NULL,
    Doctor_Specialization TEXT NOT NULL,
    Doctor_Age INTEGER NOT NULL CHECK (Doctor_Age >= 18),
    Doctor_Gender TEXT NOT NULL,
    Doctor_Email TEXT NOT NULL,
    Doctor_Phone TEXT NOT NULL,
    Doctor_Portrait BLOB,
    FOREIGN KEY (Clinic_ID) REFERENCES Clinic(Clinic_ID)
)
''')

# Create the Records table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Records (
    Record_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Patient_ID INTEGER,
    Patient_Name TEXT,
    Doctor_ID INTEGER,
    Doctor_Name TEXT,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Description TEXT NOT NULL,
    Prescription TEXT NOT NULL,
    Appointment_ID INTEGER,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID),
    FOREIGN KEY (Appointment_ID) REFERENCES Appointments(Appointment_ID)
)
''')

# Create the Appointments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Appointments (
    Appointment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Patient_ID INTEGER,
    Patient_Name TEXT NOT NULL,
    Doctor_ID INTEGER,
    Doctor_Name TEXT NOT NULL,
    Appointment_Date DATE NOT NULL,
    Appointment_Time TIME NOT NULL,
    Appointment_Approval TEXT NOT NULL,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
)
''')

# Commit the changes
conn.commit()

def fetch_records():
    cursor.execute("SELECT * FROM Records")
    records = cursor.fetchall()
    return records
