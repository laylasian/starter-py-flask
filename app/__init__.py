from config import Config
from flask import Flask, jsonify

#sql alchemy stuff
#db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object((set_environment_config()))

    #sql alchemy stuff
    #db.init_app(app)

    #graphql graphene stuff
    """ from app.schema import schema
     app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    ) """


    @app.route('/')
    def hello_world():
        return "greetings capsuleer!"

    #sql alchemy stuff
    """ @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove() """

    return app



def set_environment_config():
    if(Config.ENV == "PRODUCTION"):
        return 'config.ProductionConfig'
    elif (Config.ENV == "DEVELOPMENT"):
        return 'config.DevelopmentConfig'