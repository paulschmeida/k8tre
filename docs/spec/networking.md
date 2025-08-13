---
topic: Networking
date: 2025-05-30
discussion: https://github.com/orgs/k8tre/discussions/4
k8tre-statements:
  spec: The TRE's CIDR/VPC/VNET is solely for in-cluster use; all external access to applications/services must be via the ingress controller/load-balancer. The TRE's must use a network plugin/CNI that fully supports Network Policy enforcement. 
---

{{ spec_content(page.meta) }}

**Questions**: 

1. **What capabilities must a CNI must provide the cluster to be K8TRE compliant?**

    Full support for K8S Network Policies? i.e. not AWS VPC CNI or Azure CNI..?

2. **Should a K8TRE's CIDR be solely for in-cluster use only, or should applications/services outside the cluster also have access to the CIDR/VPC/VNET**

    No. A K8TRE's CIDR/VPC/VNET is solely for in-cluster use only so all external access is via the ingress/load-balancer
