# Kubernetes custom scheduler

## Replicate current error

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
./createSchedulerDeployment2.sh
```

Check all in minikube:

```bash
kubectl get all --namespace=kube-system
```

Check error in scheduler pod in <kube-scheduler-name> insert name of scheduler pod:

```bash
kubectl logs <kube-scheduler-name> --namespace=kube-system
```
