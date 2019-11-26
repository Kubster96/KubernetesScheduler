from kubernetes.config import load_kube_config
from kubernetes.client import CustomObjectsApi

# only for running from localhost
load_kube_config()
# if running in the cluster should use load_incluster_config()

cust = CustomObjectsApi()
nodes = cust.list_cluster_custom_object('metrics.k8s.io', 'v1beta1', 'nodes')
pods = cust.list_cluster_custom_object('metrics.k8s.io', 'v1beta1', 'pods')

print(nodes)
print(pods)
