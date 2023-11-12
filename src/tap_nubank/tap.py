"""Nubank tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_nubank.streams import NubankStream
from tap_nubank.streams import CardStatementsStream

STREAM_TYPES = [
    CardStatementsStream,
]


class TapNubank(Tap):
    """Nubank tap class."""

    name = "tap-nubank"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "user",
            th.StringType,
            required=True,
            description="The flag to mock responses from API",
        ),
        th.Property(
            "password",
            th.StringType,
            required=True,
            secret=True,
            description="The flag to mock responses from API",
        ),
        th.Property(
            "qrcode_uuid",
            th.StringType,
            required=True,
            secret=True,
            description="The flag to mock responses from API",
        ),
        th.Property(
            "is_test",
            th.BooleanType,
            description="The flag to mock responses from API",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.NubankStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapNubank.cli()
