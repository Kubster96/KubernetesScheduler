from kubernetes.config import load_kube_config
from kubernetes.client import CustomObjectsApi

load_kube_config()

cust = CustomObjectsApi()
cust.list_cluster_custom_object('metrics.k8s.io', 'v1beta1', 'nodes')
cust.list_cluster_custom_object('metrics.k8s.io', 'v1beta1', 'pods')

print(cust)