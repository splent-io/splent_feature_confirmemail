from splent_framework.hooks.template_hooks import register_template_hook
from flask import url_for


def confirmemail_scripts():
    return '<script src="' + url_for('confirmemail.assets', subfolder='dist', filename='splent_feature_confirmemail.bundle.js') + '"></script>'


register_template_hook("layout.scripts", confirmemail_scripts)
