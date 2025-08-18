# K8TRE Architecture

![High-Level K8TRE Architecture](img/K8TRE-high-level.png)

## How the K8TRE Reference Implementation meets the K8TRE Specification

### BYO Software

The K8TRE Reference Implementation will be agnostic to whether a deployment supports "bring-your-own software and code" versus curated software and will be offered with both options available via deployment configuration.

### Container Runtimes

The K8TRE Reference Implementation uses the default high- and low-level container runtimes in the EKS, AKS, K3S Kubernetes distributions. 

### Databases

The K8TRE Reference Implementation includes the CNPG operator and a default Postgres database. Applications can deploy their own Postgres databases in a consistent manner using the operator.

### DNS

Services within K8TRE are discoverable as normal through CoreDNS with the usual format of `<service-name>.<namespace>.svc.cluster.local`. Applications are allowed to automatically create, update and delete DNS entries required to expose their services by using ExternalDNS running in the clusters.

### GitOps

The K8TRE Reference Implementation uses ArgoCD installed on a management cluster to manage nearly all resources on the child cluster(s) it manages. Here "nearly all" means ArgoCD will not be responsible for creating/destroying workspaces. JupyterHub is responsible for creating/destroying workspaces.

### Ingress

Currently implements an NGINX Ingress Controller 

### Networking

K8TRE uses Cilium as the default Container Network Interface (CNI) to provide advanced network security through network policies. Cilium is installed before ArgoCD during cluster setup and includes Hubble for network observability.

### Secrets

### Storage