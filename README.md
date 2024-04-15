# Adding Kubernetes Cluster to ArgoCD

This Python script automates the process of adding a Kubernetes cluster to ArgoCD using the argocd CLI. It simplifies the manual steps involved in authentication and cluster addition.

## Prerequisites

- Ensure you have Python installed on your system.
- Install the required Python libraries by running:

## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script.
3. Update the script with your ArgoCD server details and cluster configuration:
 - Replace `<add host ip>` with your ArgoCD server's IP address.
 - Replace `<add argocd_username>` with your ArgoCD username.
 - Replace `<password>` with your ArgoCD password.
 - Replace `<cluster name>` with the name of your Kubernetes cluster.
 - Replace `<path of kubeconfig file>` with the path to your kubeconfig file.
4. Run the script using Python:
   python3 Argocd-deployment.py


## Notes

- This script disables SSL/TLS certificate warnings, which is not recommended for production environments. Modify the script accordingly for production use.
- Ensure that the argocd CLI is installed and accessible in your system's PATH.
- Error handling is implemented to handle authentication or cluster addition failures gracefully.


