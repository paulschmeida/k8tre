# Introduction

Each page in this folder contains a K8TRE Specification statement pertaining to a particular topic within the K8TRE Specification. They have been derived from [k8tre GitHub Org Discussions](https://github.com/orgs/k8tre/discussions), as well as discussion within the K8TRE working group, and reviewed by GitHub Pull Request for publication to this site.

There a few important clarifications regarding the interpretation of these Specification statements:

1. **Scope** - The K8TRE Specification applies to Kubernetes-based TRE **codebases**. It is written for an audience of K8TRE codebase developers and defines what a K8TRE-compliant codebase must provide. This includes the K8TRE Reference Implementation as well as other codebases such as the UCL ARC TRE and the FRIDGE TRE.

2. **Technology Neutrality** - Beyond its explicit reliance on Kubernetes, the specification is technology-agnostic. However, it may prescribe in detail the capabilities that must be provided by a codebase.

3. **Applicability** – These statements are directed at those developing K8TRE-compliant codebases. They do not apply to administrators or operators running a TRE built on such a codebase (a "deployment").

## Design Principles

1. The K8TRE Specification will define the capabilities that must be provided by the underlying Kubernetes platform.
2. Whilst the Specification encourages Kubernetes best-practice, it will not impose particular implementation choices where many competing options exist. The Specification should leave room for TRE developers to make independent implementation choices based on their own organisational/business requirements, whilst still allowing acceptable choices to comply with the Specification.
3. Widespread compliance with the K8TRE Specification should result in different TRE developers in the TRE community being able to deploy each other's components in their own TREs with minimal changes to code, only changes to configuration. In other words, increased portability of open-source TRE components and applications.