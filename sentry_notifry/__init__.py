"""
sentry_notifry
~~~~~~~~~~~~~~

:copyright: (c) 2012 by egguy, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

try:
        VERSION = __import__('pkg_resources') \
                        .get_distribution('sentry_notifry').version
except Exception, e:
        VERSION = 'unknown'
