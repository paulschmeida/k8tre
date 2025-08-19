Each page in the K8TRE Specification contains a specification statement, some background motivation if applicable, illustrative compliance information for a selection of Kubernetes-based TREs, and Q & A. They have been derived from [k8tre GitHub Org Discussions](https://github.com/orgs/k8tre/discussions), as well as discussion within the K8TRE working group.

References illustrative Kubernetes-based TREs include:
- the K8TRE Reference Implementation itself 
- [TREu](https://www.ucl.ac.uk/advanced-research-computing/sensitive-data-and-trusted-research-environments) – the codebase for the UCL ARC TRE
- [FRIDGE](https://dareuk.org.uk/how-we-work/ongoing-activities/dare-uk-early-adopters/fridge/)

## Interpretation of Specification Statements

1. **Scope** - The K8TRE Specification applies to Kubernetes-based TRE *codebases*. It is written for an audience of K8TRE codebase developers and defines what a K8TRE-compliant codebase Must, Should or May provide.

2. **Technology Neutrality** - Beyond its explicit reliance on Kubernetes, the specification is technology-agnostic. However, it may prescribe capabilities that must be provided by a codebase.

3. **Applicability** – These statements are directed at those developing K8TRE-compliant codebases. They are less useful to administrators or operators running a TRE built on such a codebase (a "deployment"). Instead, the TRE codebase being deployed should provide all required documentation.

## Design Principles

1. Whilst the Specification encourages Kubernetes best-practice, it will not impose particular implementation choices where many competing options exist. The Specification should leave room for TRE developers to make independent implementation choices based on their own organisational/business requirements, whilst still allowing acceptable choices to comply with the Specification.
2. Widespread compliance with the K8TRE Specification should result in different TRE developers in the TRE community being able to deploy each other's components in their own TREs with minimal changes to code, only changes to configuration. In other words, increased portability of open-source TRE components and applications.
3. The K8TRE Specification will specify, where appropriate, capabilities that must be provided by the underlying Kubernetes platform.
