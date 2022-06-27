# Real estate microservices

## Requirements

    - Docker
    - Python3
    - Postman or insomnia 

## Installation

Clone the project 

```bash 
git clone https://github.com/JESSYV96/Real-Estate-Microservice.git
```

 - Run docker

 - Copy and Rename .env.example in .env and copy this code below for user_service and real_estate_service:

 ```
 SECRET_KEY=example_secret_key
 JWT_SECRET=secret
 ```    

- To run the project, move inside the folder apps

```
cd apps
```

Run this command

``` 
docker-compose up -d
```


