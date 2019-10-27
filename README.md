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

Run command:

```bash
kubectl edit clusterrole system:kube-scheduler
```

And insert this text in file:

```bash
- apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    annotations:
      rbac.authorization.kubernetes.io/autoupdate: "true"
    labels:
      kubernetes.io/bootstrapping: rbac-defaults
    name: system:kube-scheduler
  rules:
  - apiGroups:
    - ""
    resourceNames:
    - kube-scheduler
    - my-scheduler
    resources:
    - endpoints
    verbs:
    - delete
    - get
    - patch
    - update
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


