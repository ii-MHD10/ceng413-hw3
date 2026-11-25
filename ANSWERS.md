1\. What is the difference between a readiness and a liveness probe?



A liveness probe checks whether the application is alive and working. If it fails repeatedly, Kubernetes restarts the container. A readiness probe checks whether the application is ready to receive traffic. In my project, /health is used for liveness, while /ready checks the Redis connection.



2\. Why is a Secret not the same as encryption?



A Kubernetes Secret is used to store sensitive information separately from application code and configuration. Secret data is normally represented using Base64 encoding, which is not encryption. Anyone with sufficient permissions can decode it. Encryption at rest and proper access control are needed for better security.



3\. What happens when a container crosses its memory limit?



When a container exceeds its memory limit, it may be terminated by the operating system with an OOMKilled status. Kubernetes can then restart the container according to its restart policy. In my project, the application has a memory request of 64Mi and a memory limit of 256Mi.

## Bonus: Readiness Probe Failure

I changed the readiness probe path from /ready to /not-found.
The new Pod was running but showed 0/1 readiness.
Kubernetes reported an HTTP 404 readiness probe failure.
After restoring the correct path, all three application
replicas became ready again.

## AI Assistant Usage

I used ChatGPT to understand Kubernetes concepts, prepare
YAML manifests, troubleshoot commands, and explain test results.




## Bonus: Readiness Probe Failure

I changed the readiness probe path from /ready to /not-found.
The new Pod was running but showed 0/1 readiness.
Kubernetes reported an HTTP 404 readiness probe failure.
After restoring the correct path, all three application replicas became ready again.

## AI Assistant Usage

I used ChatGPT to understand Kubernetes concepts, prepare YAML manifests, troubleshoot commands, and explain testing results.

