---
topic: Database
date: 2025-05-30
discussion: https://github.com/orgs/k8tre/discussions/9
k8tre-statements:
  spec: The TRE must offer a Kubernetes-native mechanism for deploying relational databases on the cluster, and optionally can also allow microservices to connect to off-cluster databases.
---

{{ spec_content(page.meta) }}

**Questions**:

1. **What should K8TRE Specification say about *in-cluster* DBs and what should it say about *off-cluster* DBs?**

    Databases should be attached resources, explicitly referenced

2. **What is K8TRE Reference Implementation doing regarding DBs?**

    PostrgeSQL DB needed on-cluster as part of default deployment

3. **How prescriptive should K8TRE Specification be in dictating how DB's are deployed and managed on-cluster?**

    Be very light-touch, non-prescriptive beyond best practice & decoupled/microservice architecture.
