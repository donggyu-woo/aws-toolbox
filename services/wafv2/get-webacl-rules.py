"""Get rules of a WAFv2 WebACL as JSON.

Required permissions: wafv2:ListWebACLs, wafv2:GetWebACL

Example:
  python3 get-webacl-rules.py --name my-webacl --scope CLOUDFRONT --profile prod
"""

import argparse
import json
import sys

import boto3
from botocore.exceptions import BotoCoreError, ClientError

CLOUDFRONT_REGION = "us-east-1"


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--name", required=True, help="WebACL name")
    parser.add_argument(
        "--scope", choices=["REGIONAL", "CLOUDFRONT"], default="REGIONAL", help="WebACL scope (default: REGIONAL)")
    parser.add_argument(
        "--profile", help="AWS profile name")
    parser.add_argument(
        "--region", help="AWS region")
    return parser.parse_args()


class WebACLNotFoundError(Exception):
    pass


def get_authenticated_session(profile=None, region=None):
    session = boto3.Session(profile_name=profile, region_name=region)
    session.client("sts").get_caller_identity()
    return session


def find_web_acl(client, name, scope):
    kwargs = {"Scope": scope, "Limit": 100}
    while True:
        response = client.list_web_acls(**kwargs)
        for summary in response.get("WebACLs", []):
            if summary["Name"] == name:
                return summary
        marker = response.get("NextMarker")
        if not marker:
            return None
        kwargs["NextMarker"] = marker


def get_rules(session, name, scope="REGIONAL"):
    region = CLOUDFRONT_REGION if scope == "CLOUDFRONT" else None
    client = session.client("wafv2", region_name=region)

    summary = find_web_acl(client, name, scope)
    if summary is None:
        raise WebACLNotFoundError(
            f"WebACL '{name}' not found in {client.meta.region_name} ({scope} scope)")

    response = client.get_web_acl(Name=name, Scope=scope, Id=summary["Id"])
    return response["WebACL"]["Rules"]


def main():
    args = parse_args()

    try:
        session = get_authenticated_session(args.profile, args.region)
    except (BotoCoreError, ClientError) as e:
        sys.exit(f"AWS authentication failed: {e}")

    try:
        rules = get_rules(session, args.name, args.scope)
    except (BotoCoreError, ClientError) as e:
        sys.exit(f"Failed to get WebACL rules: {e}")

    print(json.dumps(rules, indent=2, ensure_ascii=False,
                     default=lambda v: v.decode("utf-8", errors="replace")))


if __name__ == "__main__":
    main()
