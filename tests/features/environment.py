from db_handlers.postgres_config import recreate_metadata


def before_all(context):
    recreate_metadata()
    context.host = "web"
    context.port = "8000"
    context.address = "http://{}:{}".format(context.host, context.port)
    context.config.setup_logging()


def before_scenario(context, *args):
    recreate_metadata()


def after_all(context):
    pass
