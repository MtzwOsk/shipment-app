# Shipments APP vue + django (MVP)

## Project setup: python 3.9, npm 8.11.0 and yarn 1.22.19
```
python3 --version
npm -v
yarn -v
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

### Run frontend app 
```
cd shipments_fronted/

# install dependencies
npm install

# build for production with minification
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