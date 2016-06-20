#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for danata

You can install danata with

python setup.py install
"""
from glob import glob
import os
import sys
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

if sys.version_info[:2] < (2, 7):
    print("Danata requires Python 2.7 or later (%d.%d detected)." %
          sys.version_info[:2])
    sys.exit(-1)

# Write the version information.
sys.path.insert(0, 'danata')
import release
version = release.write_versionfile()
sys.path.pop(0)

packages=["danata",
          "danata.transform",
          "danata.external",
          "danata.readwrite",
          "danata.tests",
          "danata.testing",
          "danata.utils"]

docdirbase  = 'share/doc/danata-%s' % version
# add basic documentation
data = [(docdirbase, glob("*.txt"))]
# add examples
for d in ['basic',
          'readwrite']:
    dd = os.path.join(docdirbase,'examples', d)
    pp = os.path.join('examples', d)
    data.append((dd, glob(os.path.join(pp ,"*.py"))))
    data.append((dd, glob(os.path.join(pp ,"*.bz2"))))
    data.append((dd, glob(os.path.join(pp ,"*.gz"))))
    data.append((dd, glob(os.path.join(pp ,"*.mbox"))))
    data.append((dd, glob(os.path.join(pp ,"*.edgelist"))))

# add the tests
package_data     = {
    'danata': ['tests/*.py'],
    'danata.transform': ['tests/*.py'],
    'danata.readwrite': ['tests/*.py'],
    'danata.testing': ['tests/*.py'],
    'danata.utils': ['tests/*.py']
    }

install_requires = ['decorator>=3.4.0']

if __name__ == "__main__":

    setup(
        name             = release.name.lower(),
        version          = version,
        maintainer       = release.maintainer,
        maintainer_email = release.maintainer_email,
        author           = release.authors['Youngsung'][0],
        author_email     = release.authors['Youngsung'][1],
        description      = release.description,
        keywords         = release.keywords,
        long_description = release.long_description,
        license          = release.license,
        platforms        = release.platforms,
        url              = release.url,
        download_url     = release.download_url,
        classifiers      = release.classifiers,
        packages         = packages,
        data_files       = data,
        package_data     = package_data,
        install_requires = install_requires,
        test_suite       = 'nose.collector',
        tests_require    = ['nose>=0.10.1'],
        zip_safe         = False
    )