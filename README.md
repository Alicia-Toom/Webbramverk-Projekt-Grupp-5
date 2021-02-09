# Internet Literature Database (ILDB)

  Database for books and friends, where you can rate/review and find similar books to your favorite ones.
 
### Requirements: 
```
Install requirements.txt
Docker or any other form of MongoDB
```

### Configuration: 

Set up init.py in App/Model/MongoDB/DB/db_settings
``` 
MONGO_PASSWORD = ""
MONGO_HOST = ""
MONGO_USER = ""
MONGO_PORT = ""
```
Set up init.py in App/Model/MySQL/DB/db_settings
```
SECRET_KEY = ""
```
Set upp docker-compose.yml  
Ports is set up on 27027 because 27017 is already used up on another container.  
you can change this to what ever you like, but this is the port you need in MONGO_PORT as seen above.
```
ports:
  - 27027:27017
MONGO_INITDB_ROOT_USERNAME: root
MONGO_INITDB_ROOT_PASSWORD: password
ports:
  - 8081:8081
environment:
 ME_CONFIG_MONGODB_ADMINUSERNAME: root
 ME_CONFIG_MONGODB_ADMINPASSWORD: password
```

### First time:
Start your docker container, by opening your terminal and navigate to your project directory.
```
docker-compose up
```
if you want a test user, change the value from false to true in the script.  
This will create your SQLite and Mongo database, and fill the database with books and authors.
```
run 'run_once.py'
```

### All set up and ready to go?
```
run app.py
```