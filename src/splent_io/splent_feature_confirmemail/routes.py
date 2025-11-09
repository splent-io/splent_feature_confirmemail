from flask import flash, redirect, render_template, url_for
from flask_login import login_user
from splent_io.splent_feature_confirmemail import confirmemail_bp


@confirmemail_bp.route("/confirmemail", methods=["GET"])
def index():
    return render_template("confirmemail/index.html")


@confirmemail_bp.route("/confirm_user/<token>", methods=["GET"])
def confirm_user(token):
    from splent_io.splent_feature_confirmemail.services import ConfirmemailService  # ⬅️ IMPORT AQUÍ
    confirmemail_service = ConfirmemailService()

    try:
        user = confirmemail_service.confirm_user_with_token(token)
    except Exception as exc:
        flash(exc.args[0], "danger")
        return redirect(url_for("auth.show_signup_form"))

    login_user(user, remember=True)
    return redirect(url_for("public.index"))
