# dwellingly_backend

Flask based Backend API for Dwellingly 

## Get Set Up
This project relies on Docker and Docker-Compose 

1) Download Docker here:

Windows: https://docs.docker.com/docker-for-windows/

Mac:https://docs.docker.com/docker-for-mac/ 

Linux:

2) Download Docker-Compose here:
https://docs.docker.com/compose/install/


3) Clone the project

```bash
git clone https://github.com/codeforpdx/dwellingly_backend.git
```

4) cd into the directory of the project

```bash
cd dwellingly_backend
```

5) Run 

```bash
sudo docker-compose up --build 

```

6) Open up [localhost:5000](http://localhost:5000)

## General Organization

This flask project is using the flaskRestful model - where resources and models are separated into their respective packages. 

```bash
- Home (/)
- About (/about)
- Sign Up (/signup)
- Login (/login)
- Terms and Conditions (/termsandconditions)
- Forgot Password (/password)


- Admin (/admin)
- Staff (/staff)
- Property Manager (/property_manager)
- Tenant (/tenant)
```


