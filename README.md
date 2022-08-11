# Shipments APP vue + django (MVP)

## Project setup python 3.9 and npm 8.11.0
```
python3 --version
npm -v
```

### Create env
```
virtualenv --python=python3 venv
source venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Make migration and collect static files
```
python manage.py colleddtstatic
python manage.py migrate
```

### Run frontend app dev 
```
cd shipments_fronted/
npm install
npm run serve
npm run build
```
### Run backend app dev 
```
cd .. (main catalog shipment-app)
python manage.py runserver
```

### Index url: 
```
http://127.0.0.1:8000/
```