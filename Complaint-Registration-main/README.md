# Complaint-Registration
This is a sample of portal where we can register complaints.

#Table of content

-[About](#about)

-[Features](#features)

-[Installation](#installation)

## About
The complaint Registration System allows users to register complaints about various issues such as traffic violations , delayed services , service quality, misuse of funds, roads and transportaion issues, healthcare issues and other concerns . the system ensures that complaints are logged , tracked and addressed by authorized peson.

## Features
 User Authentication :  Users can register and log in to the system. 
 Complaint Registration :Users can lodge complaints with relevant details and upload images if 
 needed.
 Complaint Tracking : Users can view the status of their complaints.
 Admin Dashboard: Admin can manage,view and update the status of complaints.
 Category Management: Complaints can be categorized for better organization and processing.

## Installation
1.**Clone the repository:**
    ```bash
    git clone <repository-url>
    ```

2. **Set up the database:**
    ```bash
    python manange.py makemigrations  
    python manage.py migrate
    ```
5. **Run the development server:**
    ```bash
   python manage.py runserver
   ```
6. Access the application at [http://localhost:8000](http://localhost:8000).`

 
