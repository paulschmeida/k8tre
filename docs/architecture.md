# K8TRE Architecture

![High-Level K8TRE Architecture](img/K8TRE-high-level.png)

## How the K8TRE Reference Implementation meets the K8TRE Specification

### BYO Software

### Container Runtimes

The K8TRE Reference Implementation uses the default high- and low-level container runtimes in the EKS, AKS, K3S Kubernetes distributions. 

### Databases

### DNS

### GitOps

### Load Balancers

### Networking

Cilium is the CNI used by the K8TRE Reference Implementation. All external access to applications/services is via the ingress object/load-balancer.

### Secrets

### Storage