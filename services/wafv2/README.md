# wafv2

- [get-webacl-rules](#get-webacl-rules)

## get-webacl-rules

Retrieves the rules of a WebACL by name.

1. Find the WebACL Id by name.

```bash
aws wafv2 list-web-acls \
  --scope <REGIONAL|CLOUDFRONT> \
  --profile <PROFILE> \
  --region <REGION> \
  --query "WebACLs[?Name=='<WEBACL_NAME>']" \
  --output json
```

2. Get the rules with the Id from step 1.

```bash
aws wafv2 get-web-acl \
  --name <WEBACL_NAME> \
  --scope <REGIONAL|CLOUDFRONT> \
  --id <WEBACL_ID> \
  --profile <PROFILE> \
  --region <REGION> \
  --query "WebACL.Rules" \
  --output json
```

Notes:
- For `--scope CLOUDFRONT`, `--region` must be `us-east-1`.

References:
- [list-web-acls](https://docs.aws.amazon.com/cli/latest/reference/wafv2/list-web-acls.html)
- [get-web-acl](https://docs.aws.amazon.com/cli/latest/reference/wafv2/get-web-acl.html)
