from setuptools import setup, find_packages
import os
from os.path import join

name = 'eea.translations'
path = name.split('.') + ['version.txt']
version = open(join(*path)).read().strip()

setup(name='eea.translations',
      version=version,
      description="Translations for EEA website. Most translations come from old local.eea.europa.eu website. We also have translated logos here.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='eea translation plone',
      author='Sasha Vincic',
      author_email='webmaster@eea.europa.eu',
      url='http://svn.eionet.europa.eu/projects/Zope/browser/trunk/eea.translations',
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
