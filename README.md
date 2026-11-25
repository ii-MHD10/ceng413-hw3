Project Overview

This project deploys a Flask application and Redis on Kubernetes. It demonstrates service discovery, scaling, self-healing, health probes, configuration management, and resource limits.

Docker Image

iimhd10/ceng413-hw3:1.0

Deployment

Run the following commands in a Kubernetes environment:

kubectl apply -f k8s.yaml
kubectl rollout status deployment/app
kubectl get pods
kubectl get services
kubectl port-forward service/app 8000:8000

Testing

Open another terminal and run:

curl http://localhost:8000/health
curl http://localhost:8000/ready
curl "http://localhost:8000/greet?name=Student"
curl http://localhost:8000/visit

Scaling

kubectl scale deployment app --replicas=3
kubectl rollout status deployment/app
kubectl get pods

Features

Flask application with Redis.

Kubernetes Deployments and ClusterIP Services.

ConfigMap and Secret.

Liveness and readiness probes.

CPU and memory requests and limits.

Non-root application container.

Horizontal scaling and self-healing.

Readiness probe failure experiment.

Cleanup

kubectl delete -f k8s.yaml