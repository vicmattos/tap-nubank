"""Stream type classes for tap-nubank."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path
from typing import ClassVar

from tap_nubank.client import NubankStream

SCHEMAS_DIR = Path(__file__).parent / Path('./schemas')


class CardStatementsStream(NubankStream):
    """Define custom stream."""

    name = 'card_statements'
    primary_keys: ClassVar[list[str]] = ['id']
    replication_key = None
    schema_filepath = SCHEMAS_DIR / 'card_statements.json'

    def get_records(
        self,
        context: dict | None,
    ) -> Iterable[dict]:
        yield from self.client.get_card_statements()
