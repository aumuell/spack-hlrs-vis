# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

from .opencover import Opencover
from .opencover import HlrsCovisePackage


class Oddlot(HlrsCovisePackage):
    """OddLOT: The OpenDRIVE Designer for Lanes, Objects and Tracks."""

    homepage = "https://www.hlrs.de/oddlot"

    depends_on('proj@:7')
    depends_on('xerces-c')
    depends_on('libtiff')
    depends_on('libpng')
    depends_on('libjpeg-turbo')
    depends_on('boost')
    depends_on('opencrg', type='build') # static library only
    depends_on('eigen')
    depends_on('glew')
    depends_on('qt+opengl@5')

    def cmake_args(self):
        """Populate cmake arguments for OddLOT."""

        args = HlrsCovisePackage.cmake_covise_args(self)

        args.append('-DCOVISE_BUILD_ONLY_ODDLOT=ON')

        return self.cmake_disable_implicit_deps(args)
