---
topic: Load Balancers
date: 2025-05-30
discussion: https://github.com/orgs/k8tre/discussions/3
k8tre-statements:
  spec: External load balancers may be provisioned automatically by Kubernetes controllers, or managed manually outside the cluster. External load balancers should be Network Load Balancers (Layer 4) to facilitate end-to-end TLS encryption.
---

### Load Balancers

*Questions*: 

1. Where should load balancers be used in the K8TRE?
2. Should a K8TRE be permitted to use a non-controller-provisioned external load balancer?
3. Should one LB per app be discouraged on account of costs i.e. should K8TRE encourage use of ingress controller + services for load balancing?

    1. Mandate one in front of the cluster ingress controller? 
    2. Yes - as long as there is one..?
    3. ?
