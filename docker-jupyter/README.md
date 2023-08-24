
# Docker configurations

1. Make sure your docker application is allowed to take as much CPU and RAM as you can give it.


# Getting everything up

1. Get into this folder in the bash 
```
cd <FOLDER LOCATION>
```

2. Build everything

```
docker-compose build
```

3. Run Everything

```
docker-compsoe up
```

- can run everything without output like this

```
docker-compose up -d
```

4. Open your browser at http://localhost:8888/home 


# Taking everything down

```
docker-compose down --volume
```