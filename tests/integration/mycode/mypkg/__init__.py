"""A dummy module for testing purposes."""

import json
import time
from user_agents import parse


def echo(event, context):
    """Echo handler."""
    event["ts"] = time.time()
    return event


def uaparse(event, context):
    """Echo handler."""
    header = json.loads(event["parameters"]).get("header")
    return {"device": parse(header["User-Agent"])}
