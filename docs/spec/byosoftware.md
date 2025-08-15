---
topic: BYO Software
last_updated: 2025-07-07
discussion: https://github.com/orgs/k8tre/discussions/8
k8tre_statements:
  spec: K8TRE supports both "bring-your-own software and code" and curated software models, but it should be up to the TRE administrators to determine what can be run.
---

{{ spec_content(page.meta) }}

**Questions**:

1. **What is K8TRE's stance on allowing researchers to ingress "bring-your-own software and code", versus a curated software model? Will it allow both?**
    
    If it's software that runs inside the researcher's VM/workspace, it should be up to the TRE administrators to determine what can be run. If it's software that requires additional infrastructure, then this is a different question regarding compliant interfaces and prerequisites for arbitrary infrastructure interacting with a K8TRE instance.

## Implementation Compliance

K8TRE Reference Implementation: 

UCL ARC TRE: Supports Bring-your-own Software, encouraging researchers to create Docker containers outside the TRE with all their software tools in it, then ingress the image into the TRE through the airlock.

FRIDGE:

Director: 