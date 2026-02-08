# Food order

A system created to speed up ask food in restaurants , it allow the client chooses what it want without needing to go to talk to an employee ,and it show to chef what meal their are needing to do also show to client when its order is ready

## About the system:
the system has two main parts the web interface building with react end tailwindcss and the api building with python and fastapi also had apply clean architecture with objective to reinforce my understanding of it.
the basic flux is simple : 
```
    client chooses a meal -> client got a unique number ->
    meal is addition to the queue -> chef prepares the meal -> 
    the number is showed -> the client got its meal 
```


# Installing and running
A simple tutorial as how install and run the system
## Requeriments / dependencies
- Python
- Nodejs
- postgres / mysql or another relational database
- git and github

## Web Install

### installing dependencies
```bash
npm i
```
### Runing
```bash
npm run dev
```

## API Install

## creating virtual environment
```bash
python -m vitualenv env
```

## active virtual environment
```bash
source ./env/bin/active
```

## install dependencies
```bash
pip install --upgrade pip
pip install -r ./requirements/local.txt
```

## create dot env file
```bash
cp ./.env-example ./.env
```

## Configure
|var | what is it |
----- |-------------------|
|DATABASE_PASSWORD | your database password|
|DATABASE_HOST | your database host|
|DATABASE_NAME | your database name|
|DATABASE_PORT | your database port|
|DATABASE_ENGINE | your database engine|
|DATABASE_USER | your database user|

## Run migrations
```bash
alembic upgrade head   
```

## Run application
```bash
PYTHONPATH=./src/ #set python path if you are not in api folder
uvicorn api.infra.main:app
```

# More
if you want know another thing that is not here maybe it is in docs:
- [routes](./docs/routes.md)
