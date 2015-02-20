# Created on 2015.02.20
#
# @author: Giovanni Cannata
#
# Copyright 2015 Giovanni Cannata
#
# This file is part of sldap3.
#
# ldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from os import path
from datetime import datetime
from platform import uname, python_version, python_build, python_compiler


version_file = open('_version.py')
exec_local = dict()
exec(version_file.read(), dict(), exec_local)
__version__ = exec_local['__version__']
__author__ = exec_local['__author__']
__email__ = exec_local['__email__']
__license__ = exec_local['__license__']
__url__ = exec_local['__url__']
__description__ = exec_local['__description__']
__long_description__ = exec_local['__long_description__']
__package_name__ = exec_local['__package_name__']
__package_folder__ = exec_local['__package_folder__']
__status__ = exec_local['__status__']

version_file.close()

project_version_file = open(path.join(__package_folder__, __package_name__, 'version.py'), 'w+')
project_version_file.write('\n'.join([
    '# THIS FILE IS AUTO-GENERATED. PLEASE DO NOT MODIFY IT!!!'
    '# version file for ' + __package_name__,
    '# generated on ' + datetime.now().__str__(),
    '# on system ' + str(uname()),
    '# with Python ' + python_version() + ' - ' + str(python_build()) + ' - ' + python_compiler(),
    '#',
    '__version__ = ' + "'" + __version__ + "'",
    '__author__ = ' + "'" + __author__ + "'",
    '__email__ = ' + "'" + __email__ + "'",
    '__url__ = ' + "'" + __url__ + "'",
    '__description__ = ' + "'" + __description__ + "'",
    '__status__ = ' + "'" + __status__ + "'",
    '__license__ = ' + "'" + __license__ + "'"]))

project_version_file.close()

setup(name=__package_name__,
      version=__version__,
      packages=['sldap3',
                'sldap3.core'],
      package_dir={'': __package_folder__},
      install_requires=['pyasn1 >= 0.1.7',
                        'ldap3 >= 0.9.7.5'],
      license=__license__,
      author=__author__,
      author_email=__email__,
      description=__description__,
      long_description=__long_description__,
      keywords='python3 python2 ldap server',
      url=__url__,
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'Operating System:: MacOS:: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP']
      )
