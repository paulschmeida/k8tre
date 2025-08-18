---
topic: Storage
last_updated: 2025-05-30
discussion: https://github.com/orgs/k8tre/discussions/2
k8tre_statements:
  spec: PVCs from K8TRE components or applications should request from a set of pre-defined storage classes, not simply from the default storage class.  
---

{{ spec_content(page.meta) }}

## Motivation

The development of K8TRE-compliant components (e.g. apps) will be facilitated by the availability of storage in the deployment whose quality-of-service, backup policies and access modes (for example) are encoded in terms of standard Kubernetes abstractions. This will allow deployers to  match up and verify component requirements against available storage.

## Implementation Compliance

### K8TRE Reference Implementation

Use [Longhorn](https://longhorn.io/docs/1.9.0/deploy/install/install-with-kubectl/) for block distributed storage to align with FRIDGE and UCL Condenser (?).

### TREu

### FRIDGE

FRIDGE uses Longhorn for wide compatibility across different platforms. It uses NFS to do ReadWriteMany storage classes.

## FAQ

- Which storage requirements shall the K8TRE Specification assume the underlying Kubernetes platform will provide? e.g. what storageClass definitions / providers should be recommended/mandated?

- Which Persistent Volume Types/plugins will K8TRE Reference Implementation use?

    Storage classes should be defined for any K8TRE to use.
