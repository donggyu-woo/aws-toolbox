# aws-toolbox
A toolbox of reusable AWS CLI commands and Python (boto3) scripts.

## Usage

```bash
uv run services/<service>/<script>.py --help
```

Without uv, install `boto3` and run the script with `python`.

AWS CLI commands are listed in `services/<service>/README.md`.

## Authentication

Every script accepts `--profile` and `--region`. When omitted, Boto3 resolves them in its default order:

- Credentials: [Boto3 Credentials guide](https://docs.aws.amazon.com/boto3/latest/guide/credentials.html)
- Region: [Boto3 Configuration guide](https://docs.aws.amazon.com/boto3/latest/guide/configuration.html)
