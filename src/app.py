import os

from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def root():
        return jsonify(
            {
                "service": "my-app",
                "status": "ok",
            }
        )

    @app.get("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    return app


app = create_app()


if __name__ == "__main__":
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", "5000"))
    app.run(host=host, port=port)
