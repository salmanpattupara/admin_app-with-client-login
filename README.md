# arriba_tech⚙️

## 🖥️ Admin & Client/Customer Dashboard Overview

Build a powerful admin dashboard tailored for organizations managing clients and their customers, offering secure access, flexible subscription management, and intuitive interfaces for both admins and clients. Designed using **Django** as the backend, **Django REST Framework** for API support, and a modern front-end using **HTML/CSS/JS**.

### 📝 Installation

1. **Install Python**
2. **Install Django**
    - `pip install django`
3. **Install Django REST Framework**
    - `pip install djangorestframework`

### 🪶 Features

- **Admin Panel**
  - Secure login/logout for administrators
  - Feature-rich dashboard for full system management
  - Create and register new client accounts (unique username/password for each client)
  - Define and assign subscription plans (with set durations)
  - Monitor and control client access based on subscription status

- **Client Portal**
  - Dedicated login/logout for clients
  - Client dashboard summarizing key activities and information
  - Clients can add and manage their own customers, along with service requirements
  - Generate invoices for customer services
  - View current subscription, plan details, and remaining duration

### 🗝️ Highlights

- **Subscription Management:**  
  Admins can create various plans and set their durations. Clients’ access is strictly tied to the validity of their subscription—expired plans prevent further logins until renewed.
- **Account Security:**  
  Only admins have the authority to register and manage client accounts, maintaining consistent and secure access control.
- **User-Friendly Interface:**  
  All forms and data inputs are presented as pop-up dialogs, ensuring a clean and intuitive user experience for both admins and clients.

### 🧑‍💻 Tech Stack

- **Backend:** Django  
- **API:** Django REST Framework  
- **Frontend:** HTML, CSS, JavaScript

If you're focused on robust Python and SQL workflows with Git and want clear separation between admin controls and client/customer activities, this architecture ensures extensibility, security, and smooth management for educational or business applications.

