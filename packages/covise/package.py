# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

from .opencover import Opencover


class Covise(Opencover):
    """Collaborative Visualization and Simulation Environment"""

    homepage = "https://www.hlrs.de/covise"

    provides('cover')

    variant('vtk', default=True, description='Read VTK data')
    variant('assimp', default=True, description='Read polygonal models in various formats')
    variant('hdf5', default=True, description='Read CGNS, NetCDF and other HDF5 based data formats')

    depends_on('python@2.7:', type=('build', 'run'))
    #depends_on('qt@5.15:+opengl+webkit') # depends on Python 2, does not work in spack > 0.19
    depends_on('qt@5.15:+opengl')

    depends_on('hdf5+cxx+hl', when='+hdf5')
    depends_on('netcdf-cxx4', when='+hdf5')
    depends_on('cgns', when='+hdf5')

    depends_on('libzip')
    depends_on('libarchive')

    depends_on('vtk', when='+vtk')

    depends_on('assimp', when='+assimp')

    depends_on('libmicrohttpd')
    #depends_on('coin3d')
    #depends_on('openssl')
    depends_on('gdal')
    depends_on('libgeotiff')
    depends_on('proj@:7.99')

    def cmake_args(self):
        """Populate cmake arguments for COVISE."""

        args = Opencover.cmake_opencover_args(self)

        return self.cmake_disable_implicit_deps(args)
