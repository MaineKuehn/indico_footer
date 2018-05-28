from indico.web.forms.base import IndicoForm

from indico.web.forms.fields import MultipleItemsField
from flask import escape

from .utility import gettext as _


def custom_string_validation(value):
    """
    :param value:
    :raises ValueError
    :return:
    """
    if value != escape(value):
        raise ValueError
    return value


class SettingsForm(IndicoForm):
    footer_links = MultipleItemsField(_('Footer Links'), fields=[
        {'id': 'name', 'caption': _('Name'), 'required': True, 'coerce': custom_string_validation},
        {'id': 'link', 'caption': _('Link'), 'required': True, 'coerce': custom_string_validation}],
                                      description=_("Add further links to be added to the footer of Indico"),
                                      sortable=True)
