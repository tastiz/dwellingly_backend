# dwellingly_backend

Flask based Backend for Dwellingly 

## Get Set Up

1) Clone the project

```bash
git clone https://github.com/codeforpdx/dwellingly_backend.git
```

2) cd into the directory of the project

```bash
cd dwellingly_backend
```

3) Run 

```bash
pip install -r requirements.txt
```

4) Run

```bash
python3 run.py
```

5) Open up [localhost:5000](http://localhost:5000)


## General Organization

This flask project is using the blueprint model - where related views and models are grouped together.

```bash
- Home (/)
- Admin (/admin)
- Staff (/staff)
- Property Manager (/property_manager)
- Tenant (/tenant)
```


