# Installation Guide

**AI Generated placeholder text - Not sanity checked!**

This guide explains how to install K8tre MVP.

## Prerequisites

Before installing, ensure you have:

- Kubernetes cluster v1.20+
- kubectl installed and configured
- Helm v3+ (optional)

## Installation Methods

### Method 1: Using kubectl

```bash
# Apply the manifest directly
kubectl apply -f https://github.com/yourusername/k8tre-mvp/releases/latest/download/k8tre-mvp.yaml
```

### Method 2: Using Helm

```bash
# Add the Helm repository
helm repo add k8tre https://yourusername.github.io/k8tre-mvp/charts

# Update repositories
helm repo update

# Install the chart
helm install k8tre-mvp k8tre/k8tre-mvp
```

## Verifying the Installation

To verify that K8tre MVP is installed correctly:

```bash
kubectl get pods -n k8tre-system
```

You should see the K8tre MVP pods running.
