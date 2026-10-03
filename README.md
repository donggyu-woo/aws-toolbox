# aws-toolbox
A toolbox of Python (boto3) scripts for AWS operations.

## Authentication

Every script accepts `--profile` and `--region`. When omitted, Boto3 resolves them in its default order:

- Credentials: [Boto3 Credentials guide](https://docs.aws.amazon.com/boto3/latest/guide/credentials.html)
- Region: [Boto3 Configuration guide](https://docs.aws.amazon.com/boto3/latest/guide/configuration.html)
