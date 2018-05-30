# -*- coding: utf-8 -*-
#
# This file is part of the Indico Footer Customisation Plugin.
# Copyright (C) 2018 Eileen Kuehn, Max Fischer
#
# This is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico Footer Customisation Plugin;if not, see <http://www.gnu.org/licenses/>.
from __future__ import unicode_literals
from indico.web.forms.base import IndicoForm

from indico.web.forms.fields import MultipleItemsField
from flask import escape

from .utility import gettext as _


def custom_string_validation(value):
    """
    Test that a string is valid for insertion into the Plugin placeholders

    :param value: string to validate
    :type value: str
    :raises ValueError: if ``value`` is not valid
    :return: valid form of ``value``
    """
    if value != escape(value):
        raise ValueError
    return value


class SettingsForm(IndicoForm):
    footer_links = MultipleItemsField(_('Footer Links'), fields=[
        {'id': 'name', 'caption': _('Name'), 'required': True, 'coerce': custom_string_validation},
        {'id': 'link', 'caption': _('Link'), 'required': True, 'coerce': custom_string_validation},
        {'id': 'target', 'caption': _('Target'), 'type': 'select', 'required': True}],
                                      description=_("Add further links to be added to the footer of Indico"),
                                      sortable=True,
                                      choices={'target': {'_self': _('_self'), '_blank': _('_blank')}})
