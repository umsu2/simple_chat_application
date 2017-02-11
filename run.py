import os

from app import create_app

config = os.getenv('FLASK_CONFIG','dev')
app = create_app(config)

if __name__ == '__main__':
    app.run()

