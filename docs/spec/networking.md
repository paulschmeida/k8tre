---
topic: Networking
last_updated: 2025-05-30
discussion: https://github.com/orgs/k8tre/discussions/4
k8tre_statements:
  spec: All external access to applications/services must be via the ingress/gateway. The TREs must use a network plugin/CNI that fully supports Network Policy enforcement. 
---

{{ spec_content(page.meta) }}

**Questions**: 

1. **What capabilities must a CNI must provide the cluster to be K8TRE compliant?**

    Full support for K8S Network Policies? i.e. not AWS VPC CNI or Azure CNI..?

2. **Should applications/services outside the cluster also have access to the CIDR/VPC/VNET**

    No. A K8TRE's CIDR/VPC/VNET is solely for in-cluster use only so all external access is via the ingress/gateway.
    
## Implementation Compliance

K8TRE Reference Implementation:

UCL ARC TRE: 

FRIDGE:

Director: 