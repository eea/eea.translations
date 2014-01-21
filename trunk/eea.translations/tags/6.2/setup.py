""" EEA Translations installer
"""
import os
from os.path import join
from setuptools import setup, find_packages

name = 'eea.translations'
path = name.split('.') + ['version.txt']
version = open(join(*path)).read().strip()

setup(name=name,
      version=version,
      description="Translations for EEA website. Most translations come from "
                  "old local.eea.europa.eu website. We also have translated "
                  "logos here.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='eea translation',
      author='European Environment Agency',
      author_email='webmaster@eea.europa.eu',
      url='http://svn.eionet.europa.eu/projects/'
          'Zope/browser/trunk/eea.translations',
      license='MPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
