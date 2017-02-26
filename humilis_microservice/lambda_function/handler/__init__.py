"""Lambda function entry point."""

# preprocessor:jinja2

from werkzeug.utils import import_string  # noqa


handler  = import_string('{{handler}}')


def lambda_handler(event, context):
    """Handle incoming requests."""
    return handler(event, context)
