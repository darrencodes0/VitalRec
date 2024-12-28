Drop Database If Exists HospitalRecords;
Create Database HospitalRecords;

Use HospitalRecords;

CREATE TABLE Patient (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,       
    first_name VARCHAR(100) NOT NULL,               
    last_name VARCHAR(100) NOT NULL,                
    date_of_birth DATE NOT NULL,                    
    gender ENUM('Male', 'Female', 'Other') NOT NULL, 
    phone_number VARCHAR(15),                       
    email VARCHAR(100),                             
    address TEXT                                    
);

INSERT INTO Patient (first_name, last_name, date_of_birth, gender, phone_number, email, address)
VALUES
('John', 'Doe', '1985-06-15', 'Male', '555-1236', 'john.doe@example.com', '123 Elm Street'),
('Jane', 'Smith', '1990-09-10', 'Female', '555-5678', 'jane.smith@example.com', '456 Oak Avenue'),
('Michael', 'Brown', '1975-02-20', 'Male', '555-2468', 'michael.brown@example.com', '789 Pine Road'),
('Emily', 'Johnson', '2000-12-05', 'Female', '555-1357', 'emily.johnson@example.com', '101 Maple Drive'),
('Chris', 'Taylor', '1988-03-25', 'Male', '555-4321', 'chris.taylor@example.com', '234 Birch Lane'),
('Sarah', 'Williams', '1995-11-10', 'Female', '555-8766', 'sarah.williams@example.com', '678 Cedar Street'),
('David', 'Wilson', '1960-08-30', 'Male', '555-7890', 'david.wilson@example.com', '890 Spruce Avenue'),
('Sophia', 'Martinez', '1982-05-14', 'Female', '555-6543', 'sophia.martinez@example.com', '567 Aspen Drive'),
('James', 'Anderson', '1993-01-22', 'Male', '555-3457', 'james.anderson@example.com', '321 Oakwood Blvd'),
('Olivia', 'Clark', '1987-09-18', 'Female', '555-6789', 'olivia.clark@example.com', '456 Maple Grove'),
('Ethan', 'Lee', '1999-12-25', 'Male', '555-8901', 'ethan.lee@example.com', '789 Pine Hollow'),
('Isabella', 'Lopez', '2005-07-05', 'Female', '555-4322', 'isabella.lopez@example.com', '123 Willow Way'),
('Matthew', 'Harris', '1973-04-12', 'Male', '555-5679', 'matthew.harris@example.com', '456 Birch View'),
('Ava', 'Walker', '1996-08-08', 'Female', '555-8765', 'ava.walker@example.com', '890 Cedar Hill'),
('William', 'Young', '1989-02-27', 'Male', '555-1358', 'william.young@example.com', '234 Maple Woods'),
('Mia', 'Allen', '1998-06-10', 'Female', '555-2469', 'mia.allen@example.com', '567 Oak Glen'),
('Alexander', 'King', '1983-10-20', 'Male', '555-3456', 'alexander.king@example.com', '321 Spruce Valley'),
('Charlotte', 'Scott', '2002-03-15', 'Female', '555-7891', 'charlotte.scott@example.com', '678 Aspen Court'),
('Daniel', 'Green', '1977-11-05', 'Male', '555-6544', 'daniel.green@example.com', '890 Willow Drive'),
('Amelia', 'Baker', '1992-07-30', 'Female', '555-1235', 'amelia.baker@example.com', '123 Oak Ridge');


CREATE TABLE Department (
    department_id INT AUTO_INCREMENT PRIMARY KEY,   
    department_name VARCHAR(100) NOT NULL,          
	phone_number VARCHAR(15),                       
    description TEXT                               
);

INSERT INTO Department (department_name, description, phone_number)
VALUES
('Cardiology', 'Focuses on disorders of the heart and blood vessels.', '555-1000'),
('Neurology', 'Specializes in treating conditions of the nervous system.', '555-2000'),
('Orthopedics', 'Deals with the musculoskeletal system.', '555-3000'),
('Pediatrics', 'Provides medical care for infants, children, and adolescents.', '555-4000'),
('Dermatology', 'Focuses on skin, hair, and nail disorders.', '555-5000');

CREATE TABLE Room (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL               
);

INSERT INTO Room (room_number)
VALUES
('R101'), ('R102'), ('R103'), ('R104'), ('R105'),
('R106'), ('R107'), ('R108'), ('R109'), ('R110'),
('R111'), ('R112'), ('R113'), ('R114'), ('R115'),
('R116'), ('R117'), ('R118'), ('R119'), ('R120'),
('R121'), ('R122'), ('R123'), ('R124'), ('R125'),
('R126'), ('R127'), ('R128'), ('R129'), ('R130'),
('R201'), ('R202'), ('R203'), ('R204'), ('R205'),
('R206'), ('R207'), ('R208'), ('R209'), ('R210'),
('R211'), ('R212'), ('R213'), ('R214'), ('R215'),
('R216'), ('R217'), ('R218'), ('R219'), ('R220'),
('R221'), ('R222'), ('R223'), ('R224'), ('R225'),
('R226'), ('R227'), ('R228'), ('R229'), ('R230');

CREATE TABLE Doctor (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,       
    department_id INT,								
    first_name VARCHAR(100) NOT NULL,               
    last_name VARCHAR(100) NOT NULL,                
    phone_number VARCHAR(15),                       
    email VARCHAR(100),                             
    office_number VARCHAR(10),                       
    FOREIGN KEY (department_id) REFERENCES Department(department_id) ON DELETE SET NULL
);

INSERT INTO Doctor (department_id, first_name, last_name, phone_number, email, office_number)
VALUES
(1, 'Alice', 'Green', '555-1001', 'alice.green@example.com', 'C101'),
(1, 'Robert', 'Taylor', '555-1002', 'robert.taylor@example.com', 'C102'),
(2, 'Laura', 'Wilson', '555-2001', 'laura.wilson@example.com', 'N201'),
(2, 'Daniel', 'Moore', '555-2002', 'daniel.moore@example.com', 'N202'),
(3, 'Sophia', 'Martinez', '555-3001', 'sophia.martinez@example.com', 'O301'),
(3, 'Michael', 'Brown', '555-3002', 'michael.brown@example.com', 'O302'),
(4, 'David', 'Johnson', '555-4001', 'david.johnson@example.com', 'P401'),
(4, 'Olivia', 'Clark', '555-4002', 'olivia.clark@example.com', 'P402'),
(5, 'James', 'Anderson', '555-5001', 'james.anderson@example.com', 'D501'),
(5, 'Emma', 'Walker', '555-5002', 'emma.walker@example.com', 'D502');

CREATE TABLE PatientDoctor (
    patient_id INT NOT NULL,                        
    doctor_id INT NOT NULL,                         
    PRIMARY KEY (patient_id, doctor_id),            
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id) ON DELETE CASCADE
);

INSERT INTO PatientDoctor (patient_id, doctor_id)
VALUES
(1, 1), (1, 2), (1, 3),
(2, 2), (2, 4), (2, 5),
(3, 1), (3, 3), (3, 6),
(4, 4), (4, 5), (4, 7),
(5, 1), (5, 6), (5, 8),
(6, 2), (6, 3), (6, 7),
(7, 1), (7, 4), (7, 9),
(8, 2), (8, 5), (8, 10),
(9, 3), (9, 6), (9, 7),
(10, 4), (10, 8), (10, 9),
(11, 1), (11, 3), (11, 10),
(12, 2), (12, 5), (12, 6),
(13, 4), (13, 7), (13, 8),
(14, 1), (14, 2), (14, 9),
(15, 3), (15, 4), (15, 10),
(16, 5), (16, 6), (16, 7),
(17, 8), (17, 9), (17, 10),
(18, 1), (18, 2), (18, 3),
(19, 4), (19, 5), (19, 6),
(20, 7), (20, 8), (20, 9);

CREATE TABLE Appointment (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,       
    patient_id INT NOT NULL,                             
    doctor_id INT NOT NULL,                              
    room_id INT,                                         
    creation_date DATETIME NOT NULL,					
    appointment_date DATETIME NOT NULL,                 
    reason_for_visit VARCHAR(255) NOT NULL,             
    status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', 
    notes TEXT,                                         
 
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES Room(room_id) ON DELETE SET NULL
);

INSERT INTO Appointment (patient_id, doctor_id, room_id, creation_date, appointment_date, reason_for_visit, status, notes)
VALUES
(1, 1, 1, '2024-12-01 09:00:00', '2024-12-05 10:00:00', 'Routine check-up', 'Scheduled', 'Bring previous records.'),
(1, 2, 2, '2024-12-02 14:00:00', '2024-12-06 11:30:00', 'Cardiology follow-up', 'Scheduled', NULL),
(2, 4, 3, '2024-12-03 13:00:00', '2024-12-07 09:00:00', 'Neurology consultation', 'Scheduled', 'Patient complains of headaches.'),
(2, 5, 4, '2024-12-04 10:00:00', '2024-12-08 14:00:00', 'Dermatology check-up', 'Scheduled', NULL),
(3, 1, 5, '2024-12-01 11:00:00', '2024-12-09 16:00:00', 'Routine check-up', 'Scheduled', 'Check vitals.'),
(3, 6, 6, '2024-12-02 12:00:00', '2024-12-10 10:00:00', 'Orthopedic follow-up', 'Completed', 'Patient recovering well.'),
(4, 7, 7, '2024-12-03 09:00:00', '2024-12-11 11:00:00', 'Pediatric consultation', 'Cancelled', 'Reschedule later.'),
(4, 5, 8, '2024-12-04 15:00:00', '2024-12-12 13:00:00', 'Skin rash treatment', 'Scheduled', NULL),
(5, 8, 9, '2024-12-01 10:00:00', '2024-12-13 09:00:00', 'Routine check-up', 'Scheduled', 'Check blood pressure.'),
(5, 9, 10, '2024-12-02 13:00:00', '2024-12-14 14:30:00', 'Cardiology consultation', 'Scheduled', NULL),
(6, 3, 11, '2024-12-03 11:00:00', '2024-12-15 10:00:00', 'Neurology consultation', 'Scheduled', 'MRI scheduled for next visit.'),
(6, 10, 12, '2024-12-04 14:00:00', '2024-12-16 15:00:00', 'Orthopedic treatment', 'Completed', 'X-ray results show progress.'),
(7, 1, 13, '2024-12-01 09:00:00', '2024-12-17 11:00:00', 'Routine check-up', 'Scheduled', 'Discuss medication changes.'),
(7, 4, 14, '2024-12-02 14:00:00', '2024-12-18 13:30:00', 'Neurology consultation', 'Cancelled', 'Patient rescheduled.'),
(8, 5, 15, '2024-12-03 10:00:00', '2024-12-19 10:00:00', 'Dermatology check-up', 'Scheduled', NULL),
(8, 6, 16, '2024-12-04 11:00:00', '2024-12-20 15:00:00', 'Orthopedic consultation', 'Scheduled', 'Physical therapy recommended.'),
(9, 7, 17, '2024-12-01 13:00:00', '2024-12-21 14:00:00', 'Pediatric consultation', 'Scheduled', NULL),
(9, 2, 18, '2024-12-02 14:00:00', '2024-12-22 16:00:00', 'Routine check-up', 'Scheduled', NULL),
(10, 3, 19, '2024-12-03 09:00:00', '2024-12-23 10:00:00', 'Neurology consultation', 'Scheduled', 'MRI required.'),
(10, 8, 20, '2024-12-04 15:00:00', '2024-12-24 11:30:00', 'Routine check-up', 'Completed', 'Discuss lab results.'),
(11, 9, 21, '2024-12-01 14:00:00', '2024-12-25 14:00:00', 'Routine check-up', 'Scheduled', 'Check blood sugar.'),
(12, 10, 22, '2024-12-02 10:00:00', '2024-12-26 15:00:00', 'Follow-up on treatment', 'Scheduled', NULL),
(13, 1, 23, '2024-12-03 11:00:00', '2024-12-27 10:00:00', 'Cardiology consultation', 'Scheduled', NULL),
(14, 4, 24, '2024-12-04 13:00:00', '2024-12-28 11:00:00', 'Routine check-up', 'Completed', 'Vitals stable.'),
(15, 6, 25, '2024-12-01 09:00:00', '2024-12-29 12:30:00', 'Orthopedic follow-up', 'Cancelled', 'Patient rescheduled.'),
(16, 2, 26, '2024-12-02 14:00:00', '2024-12-30 09:00:00', 'Neurology consultation', 'Scheduled', NULL),
(17, 8, 27, '2024-12-03 10:00:00', '2024-12-31 15:00:00', 'Routine check-up', 'Scheduled', 'Discuss lab results.'),
(18, 5, 28, '2024-12-04 11:00:00', '2025-01-01 16:00:00', 'Dermatology check-up', 'Completed', 'Skin condition improved.'),
(19, 3, 29, '2024-12-01 09:00:00', '2025-01-02 10:00:00', 'Neurology follow-up', 'Scheduled', NULL),
(20, 7, 30, '2024-12-02 15:00:00', '2025-01-03 14:00:00', 'Pediatric consultation', 'Scheduled', NULL);

CREATE TABLE Prescription (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,                        
    doctor_id INT NOT NULL,                         
    medication_name VARCHAR(255) NOT NULL,          
    dosage VARCHAR(100) NOT NULL,                   
    frequency VARCHAR(100) NOT NULL,                
    start_date DATE NOT NULL,                       
    end_date DATE,                                  
    notes TEXT,                                     
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id) ON DELETE CASCADE
);

INSERT INTO Prescription (patient_id, doctor_id, medication_name, dosage, frequency, start_date, end_date, notes)
VALUES
(1, 1, 'Atorvastatin', '10 mg', 'Once a day', '2024-12-01', '2025-01-01', 'Take with water. Avoid grapefruit.'),
(1, 2, 'Lisinopril', '5 mg', 'Twice a day', '2024-12-05', '2025-02-05', 'Monitor blood pressure daily.'),
(2, 4, 'Gabapentin', '300 mg', 'Three times a day', '2024-12-03', '2025-03-03', 'May cause drowsiness. Avoid driving.'),
(2, 5, 'Hydrocortisone cream', 'Apply sparingly', 'Twice a day', '2024-12-06', NULL, 'Apply only to affected areas.'),
(3, 1, 'Metformin', '500 mg', 'Twice a day', '2024-12-08', '2025-01-08', 'Take with meals.'),
(3, 6, 'Ibuprofen', '200 mg', 'As needed', '2024-12-10', NULL, 'Do not exceed 6 tablets in 24 hours.'),
(4, 7, 'Amoxicillin', '500 mg', 'Three times a day', '2024-12-12', '2024-12-22', 'Complete the full course.'),
(4, 5, 'Clobetasol cream', 'Apply sparingly', 'Once a day', '2024-12-15', NULL, 'Avoid sun exposure on treated areas.'),
(5, 8, 'Simvastatin', '20 mg', 'Once a day', '2024-12-18', '2025-01-18', 'Take at bedtime.'),
(5, 9, 'Aspirin', '81 mg', 'Once a day', '2024-12-20', NULL, 'Chew before swallowing for faster absorption.'),
(6, 3, 'Tramadol', '50 mg', 'Every 6 hours as needed', '2024-12-22', NULL, 'May cause dizziness or sedation.'),
(6, 10, 'Meloxicam', '15 mg', 'Once a day', '2024-12-25', '2025-02-25', 'Take with food to prevent stomach upset.'),
(7, 1, 'Losartan', '50 mg', 'Once a day', '2024-12-27', '2025-01-27', 'Monitor blood pressure weekly.'),
(7, 4, 'Cetirizine', '10 mg', 'Once a day', '2024-12-29', NULL, 'For allergy relief.'),
(8, 5, 'Fluticasone nasal spray', '1 spray each nostril', 'Twice a day', '2025-01-02', NULL, 'Shake well before use.'),
(8, 6, 'Naproxen', '500 mg', 'Twice a day', '2025-01-04', '2025-01-14', 'Take with a full glass of water.'),
(9, 7, 'Prednisone', '20 mg', 'Once a day', '2025-01-06', '2025-01-16', 'Taper dose as instructed.'),
(9, 2, 'Fexofenadine', '180 mg', 'Once a day', '2025-01-08', NULL, 'Avoid fruit juices within 4 hours of taking.'),
(10, 3, 'Albuterol inhaler', '2 puffs', 'Every 4-6 hours as needed', '2025-01-10', NULL, 'Shake well before use.'),
(10, 8, 'Omeprazole', '20 mg', 'Once a day', '2025-01-12', '2025-03-12', 'Take 30 minutes before meals.');

CREATE TABLE MedicalHistory (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,                        
    condition_name VARCHAR(255) NOT NULL,           
    diagnosis_date DATE,                            
    notes TEXT,                                     
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id) ON DELETE CASCADE
);

INSERT INTO MedicalHistory (patient_id, condition_name, diagnosis_date, notes)
VALUES
(1, 'Hypertension', '2020-06-15', 'Patient advised to monitor blood pressure regularly.'),
(1, 'Type 2 Diabetes', '2018-09-10', 'Prescribed Metformin. Regular HbA1c checks required.'),
(3, 'Osteoarthritis', '2015-02-20', 'Pain management with Ibuprofen. Recommended physiotherapy.'),
(5, 'Asthma', '2012-08-05', 'Prescribed Albuterol inhaler for emergency use.'),
(7, 'Chronic Migraines', '2019-11-10', 'Prescribed Sumatriptan. Monitor triggers and avoid stress.'),
(10, 'Hypothyroidism', '2016-01-22', 'Levothyroxine prescribed. Regular TSH level monitoring required.'),
(12, 'Eczema', '2021-07-25', 'Prescribed Hydrocortisone cream. Advised moisturizing regimen.'),
(14, 'Anemia', '2020-04-12', 'Prescribed iron supplements. Follow-up CBC test scheduled.'),
(17, 'Gastroesophageal Reflux Disease (GERD)', '2018-10-20', 'Prescribed Omeprazole. Advised dietary changes.'),
(19, 'Coronary Artery Disease', '2017-03-15', 'Patient underwent angioplasty. Follow-up with cardiologist.'),
(20, 'Chronic Back Pain', '2015-07-30', 'Prescribed Tramadol. Recommended physical therapy sessions.');





