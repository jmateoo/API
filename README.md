This project is an API with a very simple front for loading csv files to MySQL database.

It uses docker compose for orchestrate containers but deploy it on cloud(GCP) it must use K8s.

The folder for CI/CD deploy is .github/workflows contains a YAML file for authenticate on GCP with a service account
and it tries to deploy it in Cloud Run, It's wrong because this doesn't work for orchestaring containers.

It must create a manifest for deploying it in K8s, it must add in the CI/CD pipeline: manifest(YAML) and access the cluster
through kubectl.