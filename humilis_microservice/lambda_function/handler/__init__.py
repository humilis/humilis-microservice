"""Lambda function entry point."""

# preprocessor:jinja2

from werkzeug.utils import import_string  # noqa
from lambdautils.utils import send_to_delivery_stream
from lambdautils.monitor import sentry_monitor


HANDLER = import_string('{{handler}}')
INPUT_FIREHOSE_DELIVERY_STREAM = "{{input_firehose_delivery_stream}}"
OUTPUT_FIREHOSE_DELIVERY_STREAM = "{{output_firehose_delivery_stream}}"


@sentry_monitor()
def lambda_handler(event, context):
    """Handle incoming requests."""
    if INPUT_FIREHOSE_DELIVERY_STREAM:
        send_to_delivery_stream(event, INPUT_FIREHOSE_DELIVERY_STREAM)
    resp = HANDLER(event, context)
    if OUTPUT_FIREHOSE_DELIVERY_STREAM:
        send_to_delivery_stream(resp, OUTPUT_FIREHOSE_DELIVERY_STREAM)
    return resp
