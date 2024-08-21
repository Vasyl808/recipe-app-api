# recipe-app-api
Recipe API project


## Running Docker Service


### Cloning Code

Use Git to clone your project:

```sh
git clone <project ssh url>
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
