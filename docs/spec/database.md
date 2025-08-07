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

    Databases should be attached resources, explicitly referenced. TRE administrators may use an externally provided database service, such as AWS RDS, but where applications can use an on-cluster database, they should consider using the CNPG operator to deploy an instance of Postgres DB, rather than using a different Postgres helm chart and introducing an additional a dependency.

2. **What is K8TRE Reference Implementation doing regarding DBs?**

    The K8TRE Reference Implementation includes the CNPG operator and a default Postgres database. Applications can use the default DB, or deploy their own Postgres databases in a consistent manner using the operator.

3. **How prescriptive should K8TRE Specification be in dictating how DB's are deployed and managed on-cluster?**

    Be very light-touch, non-prescriptive beyond best practice & decoupled/microservice architecture.

