"""Lambda function entry point."""

# preprocessor:jinja2

from werkzeug.utils import import_string  # noqa
from lambdautils.utils import send_to_delivery_stream
from lambdautils.monitor import sentry_monitor


HANDLER = import_string('{{handler}}')
INPUT_DELIVERY_STREAM = "{{input_delivery_stream or ''}}"
OUTPUT_DELIVERY_STREAM = "{{output_delivery_stream or ''}}"


@sentry_monitor()
def lambda_handler(event, context):
    """Handle incoming requests."""
    if INPUT_DELIVERY_STREAM:
        send_to_delivery_stream(event, INPUT_DELIVERY_STREAM)
    resp = HANDLER(event, context)
    if OUTPUT_DELIVERY_STREAM:
        send_to_delivery_stream(resp, OUTPUT_DELIVERY_STREAM)
    return resp
