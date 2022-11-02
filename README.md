# A tiny example of Kubernetes application

# App

Application is a Flask web-service with simple handlers: "Hello, World!" for default page and `/health` and `/ready` for liveness and rediness probes example.

## To build and push:

```shell
docker build . --tag docker.io/<your account>/app
docker push docker.io/<your account>/app
```

## To run

```shell
kubectl apply -f k8s/all-in-one.yaml
```
