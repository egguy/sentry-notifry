"""
sentry_notifry.models
~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by egguy, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django import forms

from sentry.models import ProjectOption
from sentry.plugins import Plugin, register
from sentry.conf import settings

import urllib
import urllib2
from django.utils import simplejson as json 
import logging


class NotifryOptionsForm(forms.Form):
    key = forms.CharField(help_text="Your Notifry key")

@register
class NotifryMessage(Plugin):
    author = 'Etienne Guilluy'
    author_url = 'https://github.com/egguy/sentry-notifry'
    title = 'Notifry'
    conf_title = 'Notifry'
    conf_key = 'notifry'
    project_conf_form = NotifryOptionsForm

    def is_configured(self, project):
        return all((self.get_option(k, project) for k in ('key',)))

    def post_process(self, group, event, is_new, is_sample, **kwargs):
        key = self.get_option('key', event.project)
        if key:
            link = '%s/%s/group/%d/' % (settings.URL_PREFIX, group.project.slug, group.id)
            self.send_payload(key, '[%s] %s' % (event.server_name, event.message), link)

    def send_payload(self, key, message, link):
        url = "https://notifrier.appspot.com/notifry"
        values = {
            'format'  : 'json',
            'source'  : key,
            'title'   : message,
            'url'     : link,
        }
        data = urllib.urlencode(values)
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        raw_response_data = response.read()
        response_data = json.loads(raw_response_data)
        if 'error' in response_data:
            logger = logging.getLogger('sentry.plugins.notifry')
            logger.error('Error: %s' % response_data['error'])
