"""
Signal handlers for the confirmemail feature.

Connects to auth's user_registered signal to send a confirmation email
when a new user signs up.
"""
from splent_io.splent_feature_auth.services import user_registered
from splent_io.splent_feature_confirmemail.services import ConfirmemailService


@user_registered.connect
def on_user_registered(sender, user, **kwargs):
    """Send confirmation email when a new user registers."""
    try:
        service = ConfirmemailService()
        service.send_confirmation_email(user.email)
    except Exception:
        pass  # Don't block registration if email fails
