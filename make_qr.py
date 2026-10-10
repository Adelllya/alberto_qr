#!/usr/bin/env python3
"""QR для гостевого меню Alberto bar.

Пример:
    python3 make_qr.py https://alberto-qr.vercel.app

Генерирует qr.png (для печати) и qr.svg (вектор) в корне репозитория.
"""
import sys
import segno

DEFAULT_URL = "https://alberto-qr.vercel.app"


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    qr = segno.make(url, error="h")
    qr.save("qr.png", scale=12, border=4, dark="#92400E", light="#FFFFFF")
    qr.save("qr.svg", scale=12, border=4, dark="#92400E", light="#FFFFFF")
    print(f"QR -> {url}\n  qr.png\n  qr.svg")


if __name__ == "__main__":
    main()
