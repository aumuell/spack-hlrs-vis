# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Openinventor(CMakePackage):
    """Open Inventor is an object oriented scene graph library implemented
    in C++ layered on top of OpenGL. It was originally developed by SGI."""

    homepage = "http://oss.sgi.com/projects/inventor/"
    git      = "https://github.com/aumuell/open-inventor.git"

    maintainers = ['aumuell']

    version('master', branch='master')
    version('2.1.6', tag='v2.1.6')

    #depends_on('fontconfig')
    depends_on('bison', type='build')
    depends_on('libjpeg-turbo')
    depends_on('gl')
    depends_on('libx11')
    depends_on('motif')
    depends_on('freetype')
    depends_on('libiconv')
