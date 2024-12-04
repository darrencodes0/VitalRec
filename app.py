from flask import Flask, request, render_template, redirect, url_for, session
from database import user_table

app = Flask(__name__)
app.secret_key = 'savingthelives'

@app.route("/<role>/login", methods=["GET", "POST"])
def login(role):
    if role not in ["admin", "doctor", "patient", "staff"]:
        return render_template("error.html", error="Invalid role, please return and select the correct department for login"), 404  # Pass error to template

    template_name = f"login_{role}.html"

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Validate credentials and role
        found_user = user_table.find_one({
            "username": username,
            "password": password
        })

        if found_user:
            # Check if the user's role matches the requested role
            if found_user['role'] == role:
                # Store role in session
                session['role'] = role
                session['username'] = username  # Optional: Track the username
                return redirect(url_for('dashboard'))  # Redirect to a dashboard
            else:
                # User exists but the role is incorrect
                return render_template(template_name, error="You have an account but it's for a different role. Please log in with the correct role.")
        else:
            # Username or password is incorrect
            return render_template(template_name, error="Username and/or password are not correct")

    return render_template(template_name)





@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        username = request.form.get("username")
        role = request.form.get("role")
        password = request.form.get("password")

        user_table.insert_one({
           "username": username,
           "role": role,
           "password": password
        })
        return redirect(url_for('department'))

    return render_template("register.html")

@app.route("/")
def department():
    return render_template("department.html")

@app.route("/dashboard")
def dashboard():
    role = session.get('role', None)  # Get the role from the session, or None if not found
    return render_template("dashboard.html", role=role)


@app.route("/records")
def records():
    # Fetching data from the database (replace with actual database query)
    patients = [
        {"id": "P001", "first_name": "John", "last_name": "Doe", "dob": "1985-06-15", "gender": "Male", "phone_number": "555-1236", "email": "john.doe@example.com", "address": "123 Elm Street"},
        {"id": "P002", "first_name": "Jane", "last_name": "Smith", "dob": "1990-09-10", "gender": "Female", "phone_number": "555-5678", "email": "jane.smith@example.com", "address": "456 Oak Avenue"},
        {"id": "P003", "first_name": "Michael", "last_name": "Brown", "dob": "1975-02-20", "gender": "Male", "phone_number": "555-2468", "email": "michael.brown@example.com", "address": "789 Pine Road"},
        {"id": "P004", "first_name": "Emily", "last_name": "Johnson", "dob": "2000-12-05", "gender": "Female", "phone_number": "555-1357", "email": "emily.johnson@example.com", "address": "101 Maple Drive"},
        {"id": "P005", "first_name": "Chris", "last_name": "Taylor", "dob": "1988-03-25", "gender": "Male", "phone_number": "555-4321", "email": "chris.taylor@example.com", "address": "234 Birch Lane"},
        {"id": "P006", "first_name": "Sarah", "last_name": "Williams", "dob": "1995-11-10", "gender": "Female", "phone_number": "555-8766", "email": "sarah.williams@example.com", "address": "678 Cedar Street"},
        {"id": "P007", "first_name": "David", "last_name": "Wilson", "dob": "1960-08-30", "gender": "Male", "phone_number": "555-7890", "email": "david.wilson@example.com", "address": "890 Spruce Avenue"},
        {"id": "P008", "first_name": "Sophia", "last_name": "Martinez", "dob": "1982-05-14", "gender": "Female", "phone_number": "555-6543", "email": "sophia.martinez@example.com", "address": "567 Aspen Drive"},
        {"id": "P009", "first_name": "James", "last_name": "Anderson", "dob": "1993-01-22", "gender": "Male", "phone_number": "555-3457", "email": "james.anderson@example.com", "address": "321 Oakwood Blvd"},
        {"id": "P010", "first_name": "Olivia", "last_name": "Clark", "dob": "1987-09-18", "gender": "Female", "phone_number": "555-6789", "email": "olivia.clark@example.com", "address": "456 Maple Grove"},
        {"id": "P011", "first_name": "Ethan", "last_name": "Lee", "dob": "1999-12-25", "gender": "Male", "phone_number": "555-8901", "email": "ethan.lee@example.com", "address": "789 Pine Hollow"},
        {"id": "P012", "first_name": "Isabella", "last_name": "Lopez", "dob": "2005-07-05", "gender": "Female", "phone_number": "555-4322", "email": "isabella.lopez@example.com", "address": "123 Willow Way"},
        {"id": "P013", "first_name": "Matthew", "last_name": "Harris", "dob": "1973-04-12", "gender": "Male", "phone_number": "555-5679", "email": "matthew.harris@example.com", "address": "456 Birch View"},
        {"id": "P014", "first_name": "Ava", "last_name": "Walker", "dob": "1996-08-08", "gender": "Female", "phone_number": "555-8765", "email": "ava.walker@example.com", "address": "890 Cedar Hill"},
        {"id": "P015", "first_name": "William", "last_name": "Young", "dob": "1989-02-27", "gender": "Male", "phone_number": "555-1358", "email": "william.young@example.com", "address": "234 Maple Woods"},
        {"id": "P016", "first_name": "Mia", "last_name": "Allen", "dob": "1998-06-10", "gender": "Female", "phone_number": "555-2469", "email": "mia.allen@example.com", "address": "567 Oak Glen"},
        {"id": "P017", "first_name": "Alexander", "last_name": "King", "dob": "1983-10-20", "gender": "Male", "phone_number": "555-3456", "email": "alexander.king@example.com", "address": "321 Spruce Valley"},
        {"id": "P018", "first_name": "Charlotte", "last_name": "Scott", "dob": "2002-03-15", "gender": "Female", "phone_number": "555-7891", "email": "charlotte.scott@example.com", "address": "678 Aspen Court"},
        {"id": "P019", "first_name": "Daniel", "last_name": "Green", "dob": "1977-11-05", "gender": "Male", "phone_number": "555-6544", "email": "daniel.green@example.com", "address": "890 Willow Drive"},
        {"id": "P020", "first_name": "Amelia", "last_name": "Baker", "dob": "1992-07-30", "gender": "Female", "phone_number": "555-1235", "email": "amelia.baker@example.com", "address": "123 Oak Ridge"}
    ]
    
    return render_template("patient_records.html", patients=patients)


@app.route("/insurance")
def insurance():
    return render_template("insurance.html")

@app.route("/prescription")
def prescription():
    # Example prescription data (replace this with actual database query)
    prescriptions = [
        {"prescription_id": 1, "patient_id": 1, "doctor_id": 1, "medication_name": "Atorvastatin", "dosage": "10 mg", "frequency": "Once a day", "start_date": "2024-12-01", "end_date": "2025-01-01", "notes": "Take with water. Avoid grapefruit."},
        {"prescription_id": 2, "patient_id": 2, "doctor_id": 2, "medication_name": "Lisinopril", "dosage": "5 mg", "frequency": "Twice a day", "start_date": "2024-12-05", "end_date": "2025-02-05", "notes": "Monitor blood pressure daily."},
        {"prescription_id": 3, "patient_id": 2, "doctor_id": 4, "medication_name": "Gabapentin", "dosage": "300 mg", "frequency": "Three times a day", "start_date": "2024-12-03", "end_date": "2025-03-03", "notes": "May cause drowsiness. Avoid driving."},
        {"prescription_id": 4, "patient_id": 3, "doctor_id": 5, "medication_name": "Hydrocortisone cream", "dosage": "Apply sparingly", "frequency": "Twice a day", "start_date": "2024-12-06", "end_date": None, "notes": "Apply only to affected areas."},
        {"prescription_id": 5, "patient_id": 3, "doctor_id": 1, "medication_name": "Metformin", "dosage": "500 mg", "frequency": "Twice a day", "start_date": "2024-12-08", "end_date": "2025-01-08", "notes": "Take with meals."},
        {"prescription_id": 6, "patient_id": 4, "doctor_id": 6, "medication_name": "Ibuprofen", "dosage": "200 mg", "frequency": "As needed", "start_date": "2024-12-10", "end_date": None, "notes": "Do not exceed 6 tablets in 24 hours."},
        {"prescription_id": 7, "patient_id": 5, "doctor_id": 7, "medication_name": "Amoxicillin", "dosage": "500 mg", "frequency": "Three times a day", "start_date": "2024-12-12", "end_date": "2024-12-22", "notes": "Complete the full course."},
        {"prescription_id": 8, "patient_id": 5, "doctor_id": 5, "medication_name": "Clobetasol cream", "dosage": "Apply sparingly", "frequency": "Once a day", "start_date": "2024-12-15", "end_date": None, "notes": "Avoid sun exposure on treated areas."},
        {"prescription_id": 9, "patient_id": 6, "doctor_id": 8, "medication_name": "Simvastatin", "dosage": "20 mg", "frequency": "Once a day", "start_date": "2024-12-18", "end_date": "2025-01-18", "notes": "Take at bedtime."},
        {"prescription_id": 10, "patient_id": 7, "doctor_id": 9, "medication_name": "Aspirin", "dosage": "81 mg", "frequency": "Once a day", "start_date": "2024-12-20", "end_date": None, "notes": "Chew before swallowing for faster absorption."},
        {"prescription_id": 11, "patient_id": 7, "doctor_id": 3, "medication_name": "Tramadol", "dosage": "50 mg", "frequency": "Every 6 hours as needed", "start_date": "2024-12-22", "end_date": None, "notes": "May cause dizziness or sedation."},
        {"prescription_id": 12, "patient_id": 8, "doctor_id": 10, "medication_name": "Meloxicam", "dosage": "15 mg", "frequency": "Once a day", "start_date": "2024-12-25", "end_date": "2025-02-25", "notes": "Take with food to prevent stomach upset."},
        {"prescription_id": 13, "patient_id": 9, "doctor_id": 1, "medication_name": "Losartan", "dosage": "50 mg", "frequency": "Once a day", "start_date": "2024-12-27", "end_date": "2025-01-27", "notes": "Monitor blood pressure weekly."},
        {"prescription_id": 14, "patient_id": 10, "doctor_id": 4, "medication_name": "Cetirizine", "dosage": "10 mg", "frequency": "Once a day", "start_date": "2024-12-29", "end_date": None, "notes": "For allergy relief."},
        {"prescription_id": 15, "patient_id": 10, "doctor_id": 5, "medication_name": "Fluticasone nasal spray", "dosage": "1 spray each nostril", "frequency": "Twice a day", "start_date": "2025-01-02", "end_date": None, "notes": "Shake well before use."},
        {"prescription_id": 16, "patient_id": 11, "doctor_id": 6, "medication_name": "Naproxen", "dosage": "500 mg", "frequency": "Twice a day", "start_date": "2025-01-04", "end_date": "2025-01-14", "notes": "Take with a full glass of water."},
        {"prescription_id": 17, "patient_id": 12, "doctor_id": 7, "medication_name": "Prednisone", "dosage": "20 mg", "frequency": "Once a day", "start_date": "2025-01-06", "end_date": "2025-01-16", "notes": "Taper dose as instructed."},
        {"prescription_id": 18, "patient_id": 14, "doctor_id": 2, "medication_name": "Fexofenadine", "dosage": "180 mg", "frequency": "Once a day", "start_date": "2025-01-08", "end_date": None, "notes": "Avoid fruit juices within 4 hours of taking."},
        {"prescription_id": 19, "patient_id": 15, "doctor_id": 3, "medication_name": "Albuterol inhaler", "dosage": "2 puffs", "frequency": "Every 4-6 hours as needed", "start_date": "2025-01-10", "end_date": None, "notes": "Shake well before use."},
        {"prescription_id": 20, "patient_id": 20, "doctor_id": 8, "medication_name": "Omeprazole", "dosage": "20 mg", "frequency": "Once a day", "start_date": "2025-01-12", "end_date": "2025-03-12", "notes": "Take 30 minutes before meals."}
    ]
    
    # Render the pharmacy template and pass the prescriptions data
    return render_template("prescription.html", prescriptions=prescriptions)


@app.route("/appointments")
def appointments():
    # Simulating appointment data from the database (replace with actual database query)
    appointments_data = [
        {"appointment_id": 1, "patient_id": 1, "doctor_id": 1, "room_id": 1, "creation_date": '2024-12-01 09:00:00', 
         "appointment_date": '2024-12-05 10:00:00', "reason_for_visit": 'Routine check-up', "status": 'Scheduled', "notes": 'Bring previous records.'},
        {"appointment_id": 2, "patient_id": 1, "doctor_id": 2, "room_id": 2, "creation_date": '2024-12-02 14:00:00', 
         "appointment_date": '2024-12-06 11:30:00', "reason_for_visit": 'Cardiology follow-up', "status": 'Scheduled', "notes": None},
        {"appointment_id": 3, "patient_id": 2, "doctor_id": 4, "room_id": 3, "creation_date": '2024-12-03 13:00:00', 
         "appointment_date": '2024-12-07 09:00:00', "reason_for_visit": 'Neurology consultation', "status": 'Scheduled', "notes": 'Patient complains of headaches.'},
        {"appointment_id": 4, "patient_id": 2, "doctor_id": 5, "room_id": 4, "creation_date": '2024-12-04 10:00:00', 
         "appointment_date": '2024-12-08 14:00:00', "reason_for_visit": 'Dermatology check-up', "status": 'Scheduled', "notes": None},
        {"appointment_id": 5, "patient_id": 3, "doctor_id": 1, "room_id": 5, "creation_date": '2024-12-01 11:00:00', 
         "appointment_date": '2024-12-09 16:00:00', "reason_for_visit": 'Routine check-up', "status": 'Scheduled', "notes": 'Check vitals.'},
        {"appointment_id": 6, "patient_id": 3, "doctor_id": 6, "room_id": 6, "creation_date": '2024-12-02 12:00:00', 
         "appointment_date": '2024-12-10 10:00:00', "reason_for_visit": 'Orthopedic follow-up', "status": 'Completed', "notes": 'Patient recovering well.'},
        {"appointment_id": 7, "patient_id": 4, "doctor_id": 7, "room_id": 7, "creation_date": '2024-12-03 09:00:00', 
         "appointment_date": '2024-12-11 11:00:00', "reason_for_visit": 'Pediatric consultation', "status": 'Cancelled', "notes": 'Reschedule later.'},
        {"appointment_id": 8, "patient_id": 4, "doctor_id": 5, "room_id": 8, "creation_date": '2024-12-04 15:00:00', 
         "appointment_date": '2024-12-12 13:00:00', "reason_for_visit": 'Skin rash treatment', "status": 'Scheduled', "notes": None},
        {"appointment_id": 9, "patient_id": 5, "doctor_id": 8, "room_id": 9, "creation_date": '2024-12-01 10:00:00', 
         "appointment_date": '2024-12-13 09:00:00', "reason_for_visit": 'Routine check-up', "status": 'Scheduled', "notes": 'Check blood pressure.'},
        {"appointment_id": 10, "patient_id": 5, "doctor_id": 9, "room_id": 10, "creation_date": '2024-12-02 13:00:00', 
         "appointment_date": '2024-12-14 14:30:00', "reason_for_visit": 'Cardiology consultation', "status": 'Scheduled', "notes": None},
        {"appointment_id": 11, "patient_id": 6, "doctor_id": 3, "room_id": 11, "creation_date": '2024-12-03 11:00:00', 
         "appointment_date": '2024-12-15 10:00:00', "reason_for_visit": 'Neurology consultation', "status": 'Scheduled', "notes": 'MRI scheduled for next visit.'},
        {"appointment_id": 12, "patient_id": 6, "doctor_id": 10, "room_id": 12, "creation_date": '2024-12-04 14:00:00', 
         "appointment_date": '2024-12-16 15:00:00', "reason_for_visit": 'Orthopedic treatment', "status": 'Completed', "notes": 'X-ray results show progress.'},
        {"appointment_id": 13, "patient_id": 7, "doctor_id": 1, "room_id": 13, "creation_date": '2024-12-01 09:00:00', 
         "appointment_date": '2024-12-17 11:00:00', "reason_for_visit": 'Routine check-up', "status": 'Scheduled', "notes": 'Discuss medication changes.'},
        {"appointment_id": 14, "patient_id": 7, "doctor_id": 4, "room_id": 14, "creation_date": '2024-12-02 14:00:00', 
         "appointment_date": '2024-12-18 13:30:00', "reason_for_visit": 'Neurology consultation', "status": 'Cancelled', "notes": 'Patient rescheduled.'},
        {"appointment_id": 15, "patient_id": 8, "doctor_id": 5, "room_id": 15, "creation_date": '2024-12-03 10:00:00', 
         "appointment_date": '2024-12-19 10:00:00', "reason_for_visit": 'Dermatology check-up', "status": 'Scheduled', "notes": None},
        {"appointment_id": 16, "patient_id": 8, "doctor_id": 6, "room_id": 16, "creation_date": '2024-12-04 11:00:00', 
         "appointment_date": '2024-12-20 15:00:00', "reason_for_visit": 'Orthopedic consultation', "status": 'Scheduled', "notes": 'Physical therapy recommended.'},
        {"appointment_id": 17, "patient_id": 9, "doctor_id": 7, "room_id": 17, "creation_date": '2024-12-01 13:00:00', 
         "appointment_date": '2024-12-21 14:00:00', "reason_for_visit": 'Pediatric consultation', "status": 'Scheduled', "notes": None},
        {"appointment_id": 18, "patient_id": 9, "doctor_id": 2, "room_id": 18, "creation_date": '2024-12-02 14:00:00', 
         "appointment_date": '2024-12-22 16:00:00', "reason_for_visit": 'Routine check-up', "status": 'Scheduled', "notes": None},
        {"appointment_id": 19, "patient_id": 10, "doctor_id": 3, "room_id": 19, "creation_date": '2024-12-03 09:00:00', 
         "appointment_date": '2024-12-23 10:00:00', "reason_for_visit": 'Neurology consultation', "status": 'Scheduled', "notes": 'MRI required.'},
        {"appointment_id": 20, "patient_id": 10, "doctor_id": 8, "room_id": 20, "creation_date": '2024-12-04 15:00:00', 
         "appointment_date": '2024-12-24 11:30:00', "reason_for_visit": 'Routine check-up', "status": 'Completed', "notes": 'Discuss lab results.'},
        {"appointment_id": 21, "patient_id": 11, "doctor_id": 9, "room_id": 21, "creation_date": '2024-12-01 14:00:00', 
         "appointment_date": '2024-12-25 14:00:00', "reason_for_visit": 'Routine check-up', "status": 'Scheduled', "notes": 'Check blood sugar.'},
        {"appointment_id": 22, "patient_id": 12, "doctor_id": 10, "room_id": 22, "creation_date": '2024-12-02 10:00:00', 
         "appointment_date": '2024-12-26 15:00:00', "reason_for_visit": 'Follow-up on orthopedic treatment', "status": 'Scheduled', "notes": 'Patient to bring X-ray results.'}]
    return render_template("manage_appointments.html", appointments=appointments_data)

@app.route("/rooms")
def rooms():
    rooms_data = [
        {"room_number": "R101"}, {"room_number": "R102"}, {"room_number": "R103"}, {"room_number": "R104"}, {"room_number": "R105"},
        {"room_number": "R106"}, {"room_number": "R107"}, {"room_number": "R108"}, {"room_number": "R109"}, {"room_number": "R110"},
        {"room_number": "R111"}, {"room_number": "R112"}, {"room_number": "R113"}, {"room_number": "R114"}, {"room_number": "R115"},
        {"room_number": "R116"}, {"room_number": "R117"}, {"room_number": "R118"}, {"room_number": "R119"}, {"room_number": "R120"},
        {"room_number": "R121"}, {"room_number": "R122"}, {"room_number": "R123"}, {"room_number": "R124"}, {"room_number": "R125"},
        {"room_number": "R126"}, {"room_number": "R127"}, {"room_number": "R128"}, {"room_number": "R129"}, {"room_number": "R130"},
        {"room_number": "R201"}, {"room_number": "R202"}, {"room_number": "R203"}, {"room_number": "R204"}, {"room_number": "R205"},
        {"room_number": "R206"}, {"room_number": "R207"}, {"room_number": "R208"}, {"room_number": "R209"}, {"room_number": "R210"},
        {"room_number": "R211"}, {"room_number": "R212"}, {"room_number": "R213"}, {"room_number": "R214"}, {"room_number": "R215"},
        {"room_number": "R216"}, {"room_number": "R217"}, {"room_number": "R218"}, {"room_number": "R219"}, {"room_number": "R220"},
        {"room_number": "R221"}, {"room_number": "R222"}, {"room_number": "R223"}, {"room_number": "R224"}, {"room_number": "R225"},
        {"room_number": "R226"}, {"room_number": "R227"}, {"room_number": "R228"}, {"room_number": "R229"}, {"room_number": "R230"}
    ]

    return render_template("rooms.html", rooms=rooms_data)


@app.route("/doctors")
def doctors():
    doctors_data = [
        {"first_name": "Alice", "last_name": "Green", "department_name": "Cardiology", "phone_number": "555-1001", "email": "alice.green@example.com", "office_number": "C101"},
        {"first_name": "Robert", "last_name": "Taylor", "department_name": "Cardiology", "phone_number": "555-1002", "email": "robert.taylor@example.com", "office_number": "C102"},
        {"first_name": "Laura", "last_name": "Wilson", "department_name": "Neurology", "phone_number": "555-2001", "email": "laura.wilson@example.com", "office_number": "N201"},
        {"first_name": "Daniel", "last_name": "Moore", "department_name": "Neurology", "phone_number": "555-2002", "email": "daniel.moore@example.com", "office_number": "N202"},
        {"first_name": "Sophia", "last_name": "Martinez", "department_name": "Orthopedics", "phone_number": "555-3001", "email": "sophia.martinez@example.com", "office_number": "O301"},
        {"first_name": "Michael", "last_name": "Brown", "department_name": "Orthopedics", "phone_number": "555-3002", "email": "michael.brown@example.com", "office_number": "O302"},
        {"first_name": "David", "last_name": "Johnson", "department_name": "Pediatrics", "phone_number": "555-4001", "email": "david.johnson@example.com", "office_number": "P401"},
        {"first_name": "Olivia", "last_name": "Clark", "department_name": "Pediatrics", "phone_number": "555-4002", "email": "olivia.clark@example.com", "office_number": "P402"},
        {"first_name": "James", "last_name": "Anderson", "department_name": "Dermatology", "phone_number": "555-5001", "email": "james.anderson@example.com", "office_number": "D501"},
        {"first_name": "Emma", "last_name": "Walker", "department_name": "Dermatology", "phone_number": "555-5002", "email": "emma.walker@example.com", "office_number": "D502"}
    ]

    return render_template("doctors.html", doctors=doctors_data)


@app.route("/departments")
def departments():
    departments_data = [
        {"id": 1, "department_name": "Cardiology", "description": "Focuses on disorders of the heart and blood vessels.", "phone_number": "555-1000"},
        {"id": 2, "department_name": "Neurology", "description": "Specializes in treating conditions of the nervous system.", "phone_number": "555-2000"},
        {"id": 3, "department_name": "Orthopedics", "description": "Deals with the musculoskeletal system.", "phone_number": "555-3000"},
        {"id": 4, "department_name": "Pediatrics", "description": "Provides medical care for infants, children, and adolescents.", "phone_number": "555-4000"},
        {"id": 5, "department_name": "Dermatology", "description": "Focuses on skin, hair, and nail disorders.", "phone_number": "555-5000"}
    ]

    return render_template("medical_departments.html", departments=departments_data)


@app.route("/medical_history")
def medical_history():
    # Fetching data from the database (replace with actual database query)
    medical_history_data = [
        {"patient_id": 1, "condition_name": "Hypertension", "diagnosis_date": "2020-06-15", "notes": "Patient advised to monitor blood pressure regularly."},
        {"patient_id": 1, "condition_name": "Type 2 Diabetes", "diagnosis_date": "2018-09-10", "notes": "Prescribed Metformin. Regular HbA1c checks required."},
        {"patient_id": 3, "condition_name": "Osteoarthritis", "diagnosis_date": "2015-02-20", "notes": "Pain management with Ibuprofen. Recommended physiotherapy."},
        {"patient_id": 5, "condition_name": "Asthma", "diagnosis_date": "2012-08-05", "notes": "Prescribed Albuterol inhaler for emergency use."},
        {"patient_id": 7, "condition_name": "Chronic Migraines", "diagnosis_date": "2019-11-10", "notes": "Prescribed Sumatriptan. Monitor triggers and avoid stress."},
        {"patient_id": 10, "condition_name": "Hypothyroidism", "diagnosis_date": "2016-01-22", "notes": "Levothyroxine prescribed. Regular TSH level monitoring required."},
        {"patient_id": 12, "condition_name": "Eczema", "diagnosis_date": "2021-07-25", "notes": "Prescribed Hydrocortisone cream. Advised moisturizing regimen."},
        {"patient_id": 14, "condition_name": "Anemia", "diagnosis_date": "2020-04-12", "notes": "Prescribed iron supplements. Follow-up CBC test scheduled."},
        {"patient_id": 17, "condition_name": "Gastroesophageal Reflux Disease (GERD)", "diagnosis_date": "2018-10-20", "notes": "Prescribed Omeprazole. Advised dietary changes."},
        {"patient_id": 19, "condition_name": "Coronary Artery Disease", "diagnosis_date": "2017-03-15", "notes": "Patient underwent angioplasty. Follow-up with cardiologist."},
        {"patient_id": 20, "condition_name": "Chronic Back Pain", "diagnosis_date": "2015-07-30", "notes": "Prescribed Tramadol. Recommended physical therapy sessions."}
    ]
    
    return render_template("medical_history.html", medical_history=medical_history_data)


if __name__ == "__main__":
    app.run(debug=True)

    