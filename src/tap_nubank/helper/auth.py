import argparse
from collections.abc import Sequence

from pynubank import Nubank


def _get_uuid_from_qrcode_auth(nu: Nubank) -> str:
    uuid, qr_code = nu.get_qr_code()
    qr_code.print_ascii(invert=True)
    input(
        'Authenticate in app at "Profile" > "Security" > "Browser Access"\n\
        After authorizing, press Enter'
    )
    return uuid


def main(user: str, password: str):
    nu = Nubank()
    uuid = _get_uuid_from_qrcode_auth(nu)
    print(uuid)


def cli(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-p', '--password')
    args = parser.parse_args(argv)
    main(args.user, args.password)
    return 0


if __name__ == '__main__':
    raise SystemExit(cli())
