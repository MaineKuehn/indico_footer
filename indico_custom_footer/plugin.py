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
"""
Core of the Footer Customisation Plugin

The entry point for indico is the :py:class:`˜~.FooterCustomisationPlugin`.
"""
from __future__ import unicode_literals
from indico.core.plugins import IndicoPlugin

from .forms import SettingsForm


class FooterCustomisationPlugin(IndicoPlugin):
    """
    Footer Customisation

    A plugin to customise the Indico footer by appending links.
    """
    configurable = True
    #: form for default configuration across events
    settings_form = SettingsForm
    #: global default settings
    default_settings = {'footer_links': []}

    def init(self):
        super(FooterCustomisationPlugin, self).init()
        self.template_hook('page-footer', self.extend_footer)

    def extend_footer(self, **kwargs):
        footer_elements = []
        for setting in self.settings.get('footer_links'):
            footer_elements.append("<a href='%s' target='%s'>&nbsp;%s&nbsp;</a>" % (
                setting.get('link'), setting.get('target'), setting.get('name')))
        if footer_elements:
            return "</li><li>".join(footer_elements)
