from __future__ import annotations

import argparse
import contextlib
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

WEB_DIR = Path(__file__).with_name("web")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="dutyboard",
        description="Serve the 2026 法定节假日员工排班表 web 应用",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="监听地址（默认：127.0.0.1）",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="监听端口（默认：8000）",
    )
    parser.add_argument(
        "--open",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="启动后自动打开浏览器（默认：打开，可使用 --no-open 禁用）",
    )
    return parser.parse_args()


class FrontendHandler(SimpleHTTPRequestHandler):
    """Serve files from the web/ directory with caching disabled for dev use."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


def serve(host: str, port: int, should_open: bool = True) -> None:
    if not WEB_DIR.exists():
        raise FileNotFoundError(f"前端目录不存在：{WEB_DIR}")

    with ThreadingHTTPServer((host, port), FrontendHandler) as httpd:
        url = f"http://{host}:{port}/"
        print(f"🎯 员工排班表已就绪：{url}")

        if should_open:
            with contextlib.suppress(Exception):
                webbrowser.open(url, new=2)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 已接收到退出信号，服务器关闭中…")
        finally:
            httpd.server_close()


def main() -> None:
    args = parse_args()
    serve(args.host, args.port, args.open)


if __name__ == "__main__":
    main()
