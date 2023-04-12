import argparse

from ai_service.server import run_server

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start the api")
    parser.add_argument(
        "--debug",
        action=argparse.BooleanOptionalAction,
        help="enables development mode and hot-reload",
    )
    args = parser.parse_args()

    run_server(debug=args.debug)
