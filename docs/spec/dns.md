---
topic: DNS
date: 2025-05-30
discussion: https://github.com/orgs/k8tre/discussions/5
k8tre-statements:
  spec: A TRE that exposes services to consumers outside of its Kubernetes cluster must employ a Kubernetes-native approach for deploying DNS records that allow external consumers to discover these services. The management of these the external DNS entities should be performed together with lifecycle operations, such as deployments or upgrades, of their corresponding services within the TRE.
---

{{ spec_content(page.meta) }}

**Questions**: 

1. **What will provide in-cluster DNS?**

    The default CoreDNS is acceptable, since it allows access to services by servicename.namespace without a separate DNS server. Other

2. **Do we need to consider external DNS too - if so, what will provide this?**

    K8TRE implementers should consider using a Kubernetes-native solution for automatically managing entries (creating, updating, deleting) in off-cluster external DNS zones based on annotations on ingress objects. This allows these entries to be managed as part of the application's lifecycle on/in K8TRE.
