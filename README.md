# GCP Auto-Scaling and Security Setup

This repository contains the implementation of a **Google Cloud Platform (GCP)** project for creating a **Virtual Machine (VM)**, configuring **auto-scaling policies**, and implementing **security measures** such as **IAM roles** and **firewall rules**. This project was completed as part of the **CSL7510 VCC Jan 2025** assignment.

---

## 📋 **Assignment Overview**

The goal of this assignment is to:
1. **Create a VM instance** on GCP.
2. **Configure auto-scaling policies** based on CPU utilization.
3. **Implement security measures**:
   - Set up **IAM roles** for restricted access.
   - Configure **firewall rules** to allow/deny traffic.

---

## 🛠️ **Architecture Design**

The architecture of this project is designed to ensure scalability, security, and efficient resource management. Below is a high-level overview of the components:

1. **VM Instance**:
   - A VM instance named `fibonaccivm` is created in the **US Central** region.
   - The VM runs an Ubuntu OS and hosts a **Flask application** that calculates Fibonacci numbers.

2. **Managed Instance Group (MIG)**:
   - An **auto-scaling group** is configured to dynamically adjust the number of VM instances based on CPU utilization.
   - The minimum number of instances is set to **1**, and the maximum is set to **5**.

3. **Firewall Rules**:
   - A firewall rule is configured to allow **HTTP traffic** on port **8080**.
   - Traffic is allowed from all IPs (`0.0.0.0/0`) for testing purposes.

4. **IAM Roles**:
   - **IAM roles** are set up to grant restricted access to specific users (e.g., `Editor` role).

---

## 🚀 **Steps to Reproduce**

### **1. Create a VM Instance**
- Log in to your GCP account and create a new project named `fibonacci`.
- Create a VM instance named `fibonaccivm` with the specified configuration, including the region, machine type, OS, and networking settings.

### **2. Install Dependencies and Run the Flask App**
- SSH into the VM and install the necessary dependencies, including Python and Flask.
- Create and run a Flask application that calculates Fibonacci numbers.

### **3. Configure Auto-Scaling**
- Create an **instance template** with the same configuration as the VM.
- Set up a **Managed Instance Group (MIG)** and configure auto-scaling based on CPU utilization, with a minimum of 1 instance and a maximum of 5 instances.

### **4. Set Up Firewall Rules**
- Allow HTTP traffic on port **8080** by creating a firewall rule that permits traffic from all IPs.

### **5. Configure IAM Roles**
- Grant access to specific users by assigning the **Editor** role in the IAM settings.

---

## 📂 **Repository Structure**

The repository is organized as follows:
- **Architecture Diagram**: A visual representation of the project's architecture.
- **Bash Script**: A script to automate the setup of the VM and installation of dependencies.
- **Flask Application**: The Python script for the Fibonacci calculation.
- **README.md**: This file, providing an overview of the project.
- **Report.pdf**: Detailed Report.

---



## 🎉 **Acknowledgments**

- **Google Cloud Platform** for providing the tools and services.
- **CSL7510 VCC Jan 2025** for the assignment guidelines.
