"""Stream type classes for tap-nubank."""

from __future__ import annotations

import typing as t
from pathlib import Path

from tap_nubank.client import NubankStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class CardStatementsStream(NubankStream):
    """Define custom stream."""
    name = "card_statements"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "card_statements.json"  # noqa: ERA001

    def get_records(
        self,
        context: dict | None,  # noqa: ARG002
    ) -> Iterable[dict]:
        client = self.client
        for record in client.get_card_statements():
            yield record
