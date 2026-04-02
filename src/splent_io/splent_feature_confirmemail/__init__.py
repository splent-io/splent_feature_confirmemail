from splent_framework.blueprints.base_blueprint import create_blueprint
from splent_framework.services.service_locator import register_service

from splent_io.splent_feature_confirmemail.services import ConfirmemailService

confirmemail_bp = create_blueprint(__name__)


def init_feature(app):
    register_service(app, "ConfirmemailService", ConfirmemailService)


def inject_context_vars(app):
    return {}


# Register signal handlers (send confirmation on user registration)
from splent_io.splent_feature_confirmemail import signals  # noqa: F401,E402
