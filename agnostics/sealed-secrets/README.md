# Sealed Secrets Controller

Please see <https://github.com/bitnami-labs/sealed-secrets/> for documentation.

Install `kubeseal` CLI on your development machine by following the instructions on GitHub.

## Using Sealed Secrets in k8tre

Sealed Secrets provides a way to encrypt your Kubernetes secrets so they can be safely stored in a Git repository.

### Setup

1. The Sealed Secrets controller is automatically deployed in each environment (dev, staging, production) through the kustomize configurations.
2. Each environment uses the same base configuration that deploys version v0.29.0 of the controller.

### Creating Sealed Secrets

1. Create a regular Kubernetes Secret:
   ```yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: mysecret
     namespace: mynamespace
   data:
     username: YWRtaW4=  # base64 encoded "admin"
     password: cGFzc3dvcmQ=  # base64 encoded "password"
   ```

2. Use kubeseal to encrypt it:
   ```bash
   # Fetch the certificate from your target cluster first
   kubeseal --fetch-cert > sealed-secrets-cert.pem
   
   # Encrypt your secret
   kubeseal --format yaml --cert sealed-secrets-cert.pem < secret.yaml > sealed-secret.yaml
   ```

3. The output sealed-secret.yaml will contain a SealedSecret resource that you can safely commit to your repository.

### Best Practices for k8tre

1. **Environment-Specific Secrets**: For environment-specific secrets, place sealed secrets in the appropriate environment directory:
   - `envs/dev/` for development
   - `envs/stg/` for staging
   - `envs/prod/` for production

2. **Common Secrets**: For secrets used across environments, place them in a common directory and reference them via kustomize.

3. **Secret Rotation**: When rotating secrets, create new sealed secrets and update your kustomization files.

4. **Certificate Backup**: The sealed-secrets controller generates a certificate pair. Back up the private key to ensure you can decrypt existing secrets if the controller is reinstalled.

### Example Integration with k8tre Components

To include sealed secrets in your k8tre application:

1. Create your sealed secret YAML file
2. Reference it in your component's kustomization.yaml:
   ```yaml
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   
   resources:
     - deployment.yaml
     - service.yaml
     - sealed-secret.yaml
   ```

### Accessing Secrets in Pods

Access your decrypted secrets in pods just like regular Kubernetes secrets:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  template:
    spec:
      containers:
      - name: myapp
        env:
        - name: USERNAME
          valueFrom:
            secretKeyRef:
              name: mysecret
              key: username
        - name: PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysecret
              key: password
```

### Troubleshooting

- If secrets aren't being decrypted, ensure the controller is running:
  ```bash
  kubectl get pods -n kube-system | grep sealed-secrets
  ```
- Check controller logs:
  ```bash
  kubectl logs -n kube-system sealed-secrets-controller-xxxxxx-xxxx
  ```
- Verify the secret was sealed using the correct certificate for your target cluster.