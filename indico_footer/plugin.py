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
from indico.core import signals
from indico.core.plugins import IndicoPlugin

from .forms import SettingsForm


class FooterCustomisationPlugin(IndicoPlugin):
    """
    Footer Customisation Plugin

    A plugin to customise the Indico footer by appending links.
    """
    configurable = True
    #: form for default configuration across events
    settings_form = SettingsForm

    def init(self):
        super(FooterCustomisationPlugin, self).init()
        self.connect(signals.plugin.template_hook, self.extend_footer, sender='page-footer')

    @property
    def default_settings(self):
        return {
            'footer_links': []
        }

    def extend_footer(self, sender, **kwargs):
        for setting in self.settings.get('footer_links'):
            try:
                footer_elements.append("<a href='%s'>&nbsp;%s&nbsp;</a>" % (setting.get('link'), setting.get('name')))
            except NameError:
                footer_elements = ["<a href='%s'>%s&nbsp;</a>" % (setting.get('link'), setting.get('name'))]
        try:
            return True, 0, "</li><li>".join(footer_elements)
        except NameError:
            return None
