# Kubernetes custom scheduler

## Schedule task in minikube

Download, install minikube and run:

```bash
minikube start
```

Run command:

```bash
eval $(minikube docker-env)
```

Create image:

```bash
./createSchedulerImage.sh 
```

Create deployment:

```bash
./createSchedulerDeployment.sh
```

Check all in minikube:

```bash
kubectl get all --namespace=kube-system
```

Go to testTasks directory:

```bash
cd testTasks
```
Create test pod:

```bash
./createRedisPod.sh
```

Check if pod is being created:

```bash
kubectl get pods
```


