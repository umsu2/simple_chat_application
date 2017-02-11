import os

config = os.getenv('FLASK_CONFIG')
app = create_app(config)

if __name__ == '__main__':
    app.run()

