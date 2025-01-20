# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from .opencover import HlrsCMakePackage
from .vistle import Vistle

class VistleVr(Vistle, HlrsCMakePackage):
    """Vistle is a tool for visualization of scientific data in VR.

    This package includes the  virtual environment render module based on OpenCOVER.
    Notable features are distributed workflows and low-latency remote
    visualization."""

    depends_on('cover@2025.1:', when="@2025.1:")
    depends_on('cover@2024.1:', when="@2024.1:")
    depends_on('cover@2023.9:', when="@2023.9:")
    depends_on('cover@2021.9:')
    depends_on('cover+mpi')
    depends_on('cover+qt5', when="+qt5")
    depends_on('cover~qt5', when="~qt5")

    with when("+qt5"):
        depends_on('qt')
    with when("~qt5"):
        depends_on('qt-base')

    def cmake_args(self):
        """Populate cmake arguments for Vistle."""
        spec = self.spec

        args = Vistle.cmake_args(self)

        args.append('-DCOVISE_ARCHSUFFIX=spack')

        args.append(self.define_from_variant("VISTLE_USE_QT5", "qt5"))
        if '+qt5' in spec:
            args.append('-DCMAKE_DISABLE_FIND_PACKAGE_Qt6Core=TRUE')
        else:
            args.append('-DCMAKE_DISABLE_FIND_PACKAGE_Qt5Core=TRUE')

        return self.cmake_disable_implicit_deps(args)
