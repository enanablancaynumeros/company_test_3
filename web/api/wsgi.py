#!/usr/bin/env python3.5
from api.flask_config import create_app, init_app

app, manager = create_app()
init_app(app=app)

if __name__ == "__main__":
    app.run(host="localhost", port="8000")
