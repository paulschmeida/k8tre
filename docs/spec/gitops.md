---
topic: GitOps
last_updated: 2025-05-30
discussion: https://github.com/orgs/k8tre/discussions/7
k8tre_statements:
  spec: The TRE should employ GitOps practices when provisioning both K8TRE resources as well as any other required infrastructure level resources within the TRE.
---

{{ spec_content(page.meta) }}

**Questions**: 

1. Why is employing GitOps practices recommended?

    Using GitOps confers several advantages, but it is primarily recommended to ensure deployments are auditable. Using GitOps ensures deployments (infrastructure, applications, and configuration) are stored as declarative and version-controlled code. The Git history becomes a complete log of the TRE's state, which can help operators satisfy compliance and security requirements e.g. those of ISO 27001.

## Implementation Compliance

K8TRE Reference Implementation: uses ArgoCD installed on a management cluster to manage nearly all resources on the child cluster(s) it manages. Here "nearly all" means ArgoCD will not be responsible for creating/destroying workspaces. JupyterHub is responsible for creating/destroying workspaces.

UCL ARC TRE: uses GitOps to provision all TRE resources, as well as all infrastructure level resources, to both staging and production environments.

FRIDGE:

Director: 