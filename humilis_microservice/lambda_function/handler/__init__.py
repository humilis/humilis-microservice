"""Lambda function entry point."""

# preprocessor:jinja2

import lambdautils.utils as utils
from werkzeug.utils import import_string  # noqa


handler  = import_string('{{handler}}')


@utils.sentry_monitor()
def lambda_handler(event, context):
    """Handle incoming requests."""
    return handler(event, context)
