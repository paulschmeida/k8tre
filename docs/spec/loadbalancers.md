---
topic: Load Balancers
date: 2025-05-30
discussion: https://github.com/orgs/k8tre/discussions/3
k8tre_statements:
  spec: Off-cluster load balancers may be provisioned by Kubernetes controllers, or provisioned manually outside the cluster. The TRE must be able to handle inbound traffic and route it to services.
---

{{ spec_content(page.meta) }}

**Questions**: 

1.  **Are load balancers mandatory for a K8TRE?**

    No - the use of an external (i.e. off-cluster) load balancer is recommended, but not mandatory unless you're using services of type `LoadBalancer`.

2.  **Should one LB per app be discouraged on account of costs i.e. should K8TRE encourage use of ingress controller + services for load balancing?**

    If one load balancer can be used to support multiple applications, then this is encouraged to reduce potentially high cloud costs.
