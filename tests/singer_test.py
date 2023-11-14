"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_tap_test_class

from tap_nubank.tap import TapNubank

SAMPLE_CONFIG = {
    'user': 'not important',
    'password': 'not important',
    'qrcode_uuid': 'not important',
    'is_test': True,
}


# Run standard built-in tap tests from the SDK:
TestTapNubank = get_tap_test_class(
    tap_class=TapNubank,
    config=SAMPLE_CONFIG,
)
