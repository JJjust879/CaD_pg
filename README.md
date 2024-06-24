# Call A Doctor System

## Overview
Call A Doctor is a comprehensive healthcare management system designed to facilitate interactions between clinics, doctors, patients, and administrators. The system provides a user-friendly interface for managing medical records, doctor information, appointments, and more.

## Features

### 1. Multi-User System
- Separate login interfaces for clinics, doctors, patients, and administrators
- Secure authentication and role-based access control

### 2. Clinic Dashboard
- Central hub for clinic management
- Access to Records, Doctors, and Appointments screens
- Easy logout functionality

### 3. Records Management
- View, add, edit, and delete medical records
- Detailed record information including patient details, doctor information, and appointment data
- Sorting and searching capabilities

### 4. Doctor Management
- Comprehensive doctor profile management
- Add, edit, view, and delete doctor information
- Doctor details include name, specialization, age, gender, contact information, and portrait
- Sorting and filtering options for doctor lists

### 5. Appointment System
- Schedule, view, and manage appointments
- Approval system for appointment requests
- Sorting and filtering options for appointment lists

### 6. Admin Panel
- Manage clinic registrations

### 7. Patient Interface
- Patient registration and login 
- Appointment booking capabilities 

## Technical Details

### Backend
- SQLite database for data storage
- Python for backend logic

### Frontend
- PyQt5/PyQt6 for the graphical user interface
- Custom widgets and dialogs for enhanced user experience

### Key Components
- `startupwindow.py`: Initial interface for user role selection
- `clinic_dashboard.py`: Main interface for clinic operations
- : Main interface for patient operations
- : Main interface for doctor operations
- : Main interface for clinic operations
- : Main interface for admin operations
- : ?

## Setup and Running

1. Ensure Python 3.x is installed on your system
2. Install required dependencies:
- pip install PyQt5/6 sqlite3
3. Run the main application:
- python startupwindow.py

## Note for Developers
- The system uses a modular architecture for easy expansion and maintenance
- Consistent error handling and user feedback throughout the application
- Custom widgets (e.g., PhoneEdit) for specialized input handling
- Image handling for doctor portraits

## Future Enhancements
- Integration with external healthcare systems
- Mobile app version for patients
- Advanced reporting and analytics features
- Telemedicine capabilities

## Contributors
Justin Wong
Tan Khoon Khye
Lee Yueh Yu
Nawa Silumelume Mubukwanu
