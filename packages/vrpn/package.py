# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys
from spack.package import *


class Vrpn(CMakePackage):
    """VRPN the Virtual Reality Peripheral Network
       The device-independent, network-transparent system for accessing virtual reality peripherals from VR applications."""

    homepage = "https://vrpn.github.io/"
    git      = "https://github.com/vrpn/vrpn.git"

    maintainers("aumuell")

    version('master', branch='master', submodules=True)
    version('7.35', tag='v07.35', submodules=True)
    version('7.34', tag='v07.34', submodules=True)
    version('7.33', tag='v07.33', submodules=True)

    variant('mpi', 'MPI support')

    depends_on('swig')
    depends_on('python')
    depends_on('perl')
    depends_on('libusb')
    depends_on('jsoncpp')
    depends_on('hidapi', when=(sys.platform != "darwin"))
    depends_on('mpi', when='+mpi')

    def cmake_args(self):
        """Populate cmake arguments for VRPN."""
        spec = self.spec
        args = []
        args.append('-DVRPN_GPL_SERVER=TRUE')
        return args
