---
topic: DNS
last_updated: 2025-05-30
discussion: https://github.com/orgs/k8tre/discussions/5
k8tre_statements:
  spec: A TRE that deploys DNS records to allow external consumers to discover services should manage the external DNS entities together with the lifecycle operations of the corresponding services, such as deployments or upgrades. This includes removing DNS records which are no longer needed.
---

{{ spec_content(page.meta) }}

**Questions**: 

1. **What will provide in-cluster DNS?**

    The default CoreDNS will be suitable for most TRE implementers, since it allows access to services by servicename.namespace without a separate DNS server. A TRE implementer may use a different DNS implementation if it is necessary.

## Implementation Compliance

K8TRE Reference Implementation: Public and private DNS zones are managed by ExternalDNS running in the clusters. Traffic is routed to the Gateway service (with hostname gw.k8tre.internal for prod, gw.dev.k8tre.internal for dev etc.) using a series of AppGW listeners, host rewrite rules, and backend pool targets.

UCL ARC TRE: DNS records are not created by applications running on the cluster, rather by the administrators who manage the DNS records together with the lifecycle operations of the corresponding services.

FRIDGE:

Director: 