"""A dummy module for testing purposes."""

import time


def handler(event, context):
    """Echo handler."""
    event["ts"] = time.time()
    return event
