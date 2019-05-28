#!/usr/bin/env python
"""
sentry-notifry
==============

Integrate sentry with notifry for receiving notification to your phone

:copyright: (c) 2011 by the egguy, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


tests_require = [
        'nose==1.3.7',
]

install_requires = [
        'sentry>=3.8.0',
]

setup(
    name='sentry-notifry',
    version='0.0.1',
    author='Etienne Guilluy',
    author_email='etienne.guilluy@gmail.com',
    url='https://github.com/egguy/sentry-notifry',
    description='A Sentry extension which integrates with Notifry.',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
