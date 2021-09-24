# Flask base project

This project has the base structure for fast development of Flask project with at least thsi characteristics:

- Flask app
- Restful API
- JWT auth
- Cross Origin Resource Sharing (CORS) handling
- Postgrest DB connection
- Docker
- Gunicorn
- Error handling

With the following tree directory
```
├── app.py                                
├── config.py              
├── DB.py               
├── Dockerfile                       
├── functions.py                                      
├── gunicorn.config.py                          
├── model                                             
│   ├── enum.py                                 
├── requirements.txt
└── wsgi.py
```

## First steps
- Install dependencies (I recommend to use a virtual enviroment)
```shell
pip install -r requirements.txt
```
### Run locally
- Flask server
```shell
export FLASK_ENV=development
python wsgi.py # or flask run --port 5000 --reload
```
- Gunicorn server
```shell
gunicorn -c gunicorn.config.py -b 0.0.0.0:5000 wsgi:app --reload
```
### Simple deploy using Docker and Gunicorn (Docker installation is needed)
```shell
docker build --tag my-flask-app .
dcoker run -d -p 5000:5000 my-flask-app
```

### json db credential format
```json
{
    "host": "0.0.0.0",
    "port": "5000",
    "user": "your_user",
    "password": "your_password",
    "dbname": "db_name"
}
```

### TODO:
- Add swagger documentation
- Type hinting and validation
- Unit tests
- Blueprint structure
- Improve project structure