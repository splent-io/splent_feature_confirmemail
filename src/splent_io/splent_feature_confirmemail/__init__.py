from splent_framework.blueprints.base_blueprint import BaseBlueprint
from .services import ConfirmemailService

confirmemail_bp = BaseBlueprint("confirmemail", __name__, template_folder="templates")
confirmemail_service = ConfirmemailService()


def init_feature(app):
    app.confirmemail_service = confirmemail_service


def inject_context_vars(app):
    return {}


# Register signal handlers (send confirmation on user registration)
from splent_io.splent_feature_confirmemail import signals  # noqa: F401,E402
