### This project is built with Django and Docker.
Recipe API project

This project is built with Django and containerized using Docker. This guide provides step-by-step instructions for running the project locally in development mode and deploying it to production.

## Requirements

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Running the Project Locally in Development Mode

### 1. Clone the Repository

First, clone the project repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Configure the Environment

Create a `.env` file by copying from the `.env.sample` and fill in the necessary environment variables:

```bash
cp .env.sample .env
```

### 3. Build Docker Containers

Build the Docker images:

```bash
docker-compose build
```

### 4. Apply Migrations

Before starting the server, apply the migrations to set up your database schema:

```bash
docker-compose run --rm app sh -c "python python manage.py migrate"
```

### 5. Run Tests

To ensure everything is working correctly, run the tests:

```bash
docker-compose run --rm app sh -c "python manage.py test"
```

### 6. Start the Application

Once migrations and tests are successfully completed, start the application:

```bash
docker-compose up
```

This will start all the necessary containers for your project (Django, database, etc.)

### 7. Create Superuser

After the application is up and running, create a superuser for accessing the Django admin:

```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

### 8. Stopping the Application

To stop and remove the running containers:

```bash
docker-compose down
```

## Development Workflow

During development, you can make changes to the code, and they will be reflected automatically thanks to the volume settings in `docker-compose`. If you need to restart the containers, you can do so using the `docker-compose down` and `docker-compose up` commands.


## Deploying the Project

### Clone the Repository

First, clone the project repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

### Configure the Environment

Create a `.env` file by copying from the `.env.sample` and fill in the necessary environment variables:

```bash
cp .env.sample .env
```

Note: Ensure you create an `.env` file before starting the service.


### Running Service

To start the service, run:

```sh
docker-compose -f docker-compose-deploy.yml up -d
```

### Stopping Service

To stop the service, run:

```sh
docker-compose -f docker-compose-deploy.yml down
```

To stop service and **remove all data**, run:

```sh
docker-compose -f docker-compose-deploy.yml down --volumes
```


### Viewing Logs

To view container logs, run:

```sh
docker-compose -f docker-compose-deploy.yml logs
```

Add the `-f` to the end of the command to follow the log output as they come in.


### Updating App

If you push new versions, pull new changes to the server by running the following command:

```
git pull origin
```

Then, re-build the `app` image so it includes the latest code by running:

```sh
docker-compose -f docker-compose-deploy.yml build app
```

To apply the update, run:

```sh
docker-compose -f docker-compose-deploy.yml up --no-deps -d app
```

The `--no-deps -d` ensures that the dependant services (such as `proxy`) do not restart.
