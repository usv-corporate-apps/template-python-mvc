import os

from flask import Flask

from config import Config, DevConfig, TestConfig, ProdConfig

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    if os.environ.get('FLASK_ENV') == 'development':
        app.config.from_object(DevConfig)
    elif os.environ.get('FLASK_ENV') == 'test':
        app.config.from_object(TestConfig)
    elif os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProdConfig)
    else:
        app.config.from_object(Config)

    from . import routes
    app.register_blueprint(routes.bp)
    app.add_url_rule('/', endpoint='index')

    return app