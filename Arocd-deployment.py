import subprocess
import requests
import urllib3

 

# Disable SSL/TLS certificate warnings (not recommended for production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

 

# ArgoCD server address and credentials
argocd_host = "<add host ip>"
argo_username = "<add argocd_username>"
argo_password = "<password>"

 

# Cluster details
cluster_name = "<cluster name>"
kubeconfig_path = "<path of kubeconfig file>"

 

# Authenticate to ArgoCD using the argocd CLI
auth_cmd = [
    "argocd", "login", argocd_host, "--username", argo_username, "--password", argo_password, "--insecure"
]

 

try:
    # Run the authentication command without asking for confirmation
    subprocess.run(auth_cmd, check=True, input="yes\n", encoding="utf-8")

 

    print("Successfully authenticated to ArgoCD at '{}' as '{}'.".format(argocd_host, argo_username))

 

    # Add the cluster to ArgoCD using the argocd CLI
    cluster_cmd = [
        "argocd", "cluster", "add", cluster_name, "--kubeconfig", kubeconfig_path
    ]

 

    # Run the cluster addition command without asking for confirmation
    subprocess.run(cluster_cmd, check=True, input="yes\n", encoding="utf-8")

 

    print("Cluster '{}' added successfully to ArgoCD.".format(cluster_name))

 

except subprocess.CalledProcessError:
    print("Error authenticating to ArgoCD or adding the cluster.")
