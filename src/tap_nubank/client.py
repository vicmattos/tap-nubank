"""Custom client handling, including NubankStream base class."""

from __future__ import annotations

from collections.abc import Iterable

from pynubank import MockHttpClient
from pynubank import Nubank
from singer_sdk.streams import Stream


class NubankStream(Stream):
    """Stream class for Nubank streams."""

    @property
    def client(self) -> Nubank:
        client = Nubank() if not self.config.get('is_test') else Nubank(MockHttpClient())
        user = self.config.get('user')
        password = self.config.get('password')
        uuid = self.config.get('qrcode_uuid')
        client.authenticate_with_qr_code(user, password, uuid)
        return client

    def get_records(
        self,
        context: dict | None,
    ) -> Iterable[dict]:
        """Return a generator of record-type dictionary objects.

        The optional `context` argument is used to identify a specific slice of the
        stream if partitioning is required for the stream. Most implementations do not
        require partitioning and should ignore the `context` argument.

        Args:
            context: Stream partition or context dictionary.

        Raises:
            NotImplementedError: If the implementation is TODO
        """
        errmsg = 'The method is not yet implemented at this level. \
            Use `get_records` from the specific stream.'
        raise NotImplementedError(errmsg)
