# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class VistleLite(CMakePackage):
    """Vistle is a tool for visualization of scientific data in VR.

    Notable features are distributed workflows and low-latency remote
    visualization."""

    homepage = 'https://www.vistle.io'
    url = "https://github.com/vistle/vistle/releases/download/v2023.9/vistle-v2023.9.tar.gz"
    git = "https://github.com/vistle/vistle.git"

    maintainers = ['aumuell']

    version('master', branch='master', submodules=True)
    version("2024.2", sha256="1d2959ea56b6e8fcf617f9772f34801c66ce7b86e0d61dbe2813a1b6c7e16b18")
    version("2024.1.1", sha256="2bf644061d85dcc0e09b9af244da2795bcbb74e586ef35552f856d1ffbfbdc7f")
    version("2023.9", sha256="6ab328c3bb1ffb2763823792376be6b373eb5d81315771aa22746b489a0721b2")
    version('2021.10', tag='v2021.10', submodules=True)
    version('2020.9', tag='v2020.9', submodules=True)
    version('2020.8', commit='aaf99ff79145c10a6ba4754963266244b1481660', submodules=True)
    version('2020.2', commit='3efd1e7718d30718a6f7c0cddc3999928dc02a9d', submodules=True)
    version('2020.1', tag='v2020.1', submodules=True)
    version('2019.9', tag='v2019.9', submodules=True)

    variant('embree', default=True, description='Enable remote rendering')
    variant('python', default=True, description='Enable Python support')
    variant('qt', default=True, description='Build graphical workflow editor relying on Qt')
    variant('qt5', default=False, description='Build graphical workflow editor relying on Qt 5')
    variant('tui', default=True, description='Install interactive command line ineterface')
    variant('vtk', default=True, description='Enable reading VTK data')
    variant('netcdf', default=True, description='Enable reading of WRF data')
    variant('pnetcdf', default=True, description='Enable reading of e.g. MPAS data')
    variant('hdf5', default=True, description='Enable reading of HDF5 based data formats')
    variant('xdmf', default=False, description='Enable reading of SeisSol data')
    variant('osg', default=True, description='Build renderer relying on OpenSceneGraph')
    variant('assimp', default=True, description='Enable reading of polygonal models (.obj, .stl, ...)')
    variant('proj', default=True, description='Enable MapDrape module for carthographic coordinate mappings')
    variant('gdal', default=True, description='Enable IsoHeightSurface module for carthographic coordinate mappings')
    variant('cgal', default=True, description='Enable DelaunayTriangulation module for triangulations of point clouds')

    variant('multi', default=True, description='Use a process per module')
    variant('double', default=False, description='Use double precision scalars')
    variant('large', default=False, description='Use 64-bit indices')

    variant('static', default=False, description='Do not build shared libraries')
    variant('dev', default=True, description='Install internal 3rd party dependencies for linking to Vistle')
    variant('boostmpi', default=True, description='Do not use internal copy of Boost.MPI')
    variant('vtkm', default=True, description='Do not use internal copy of VTK-m')

    conflicts('%gcc@:4.99')
    depends_on('cmake@3.3:', type='build')

    depends_on('llvm-openmp', when='platform=darwin')

    extends('python', when='+python')

    depends_on('python@2.7:', when='+python', type=('build', 'link', 'run'))
    depends_on('py-installer', when='+python+xdmf', type=('build'))
    depends_on('py-ipython', when='+tui', type=('run'))

    depends_on('mpi')
    depends_on('hwloc')
    depends_on('botan')
    depends_on('boost+atomic+thread+exception+log+locale+math+random+timer+filesystem+date_time+program_options+serialization+system+iostreams+chrono+regex@1.59:')
    depends_on('boost+pic', when='+static')
    depends_on('boost+mpi', when='+boostmpi')
    depends_on('boost cxxstd=17')

    with when("+vtkm"):
        depends_on('vtk-m@2 +fpic')
        depends_on("vtk-m +64bitids", when="+large")
        depends_on("vtk-m ~64bitids", when="~large")

    depends_on('netcdf-c +hdf4') # hdf4 for MPAS
    depends_on('netcdf-cxx4', when='+netcdf')
    depends_on('parallel-netcdf', when='+pnetcdf')
    depends_on('hdf5', when='+hdf5')
    depends_on('xdmf3', when='+xdmf')

    depends_on('tbb')

    depends_on('zstd')
    depends_on('lz4')

    depends_on('zlib-api')
    depends_on('libzip')
    depends_on('libarchive')

    depends_on('vtk', when='+vtk')
    depends_on('tinyxml2', when='+vtk')

    depends_on('assimp', when='+assimp')

    depends_on('cgal', when='+cgal')
    depends_on('gdal', when='+gdal')
    depends_on('proj', when='+proj')
    depends_on('proj@:7', when='+proj@:2021.10')

    depends_on('openscenegraph@3.4:', when='+osg')
    depends_on('glew', when='+osg')
    depends_on('glu', when='+osg')

    depends_on('jpeg', when='+embree')
    depends_on('embree+ispc', when='+embree')
    depends_on('ispc', when='+embree', type='build')

    with when("+qt5"):
        depends_on('qt', when='+qt')
        depends_on('qt', when='+vr')
    with when("~qt5"):
        depends_on('qt-base', when='+qt')
        depends_on('qt-base', when='+vr')
        depends_on('qt-svg', when='+qt', type="run")

    def setup_build_environment(self, env):
        """Remove environment variables that let CMake find packages outside the spack tree."""
        env.set('ARCHSUFFIX','spack')
        env.unset('EXTERNLIBS')
        env.unset('COVISEDIR')
        env.unset('COVISEDESTDIR')
        env.unset('COVISE_PATH')

    def setup_run_environment(self, env):
        env.set('VISTLE_ROOT', self.prefix)

    def cmake_args(self):
        """Populate cmake arguments for Vistle."""
        spec = self.spec

        args = []

        args.append('-DVISTLE_PEDANTIC_ERRORS=OFF')
        args.append('-DCOVISE_ARCHSUFFIX=spack')

        if '+static' in spec:
            args.extend([
                '-DVISTLE_BUILD_SHARED=OFF',
                '-DVISTLE_MODULES_SHARED=OFF'
            ])

        args.append(self.define('VISTLE_INTERNAL_BOOST_MPI', not spec.satisfies('+boostmpi')))
        args.append(self.define('VISTLE_INTERNAL_VTKM', not spec.satisfies('+vtkm')))

        args.append(self.define_from_variant('VISTLE_MULTI_PROCESS', 'multi'))
        args.append(self.define_from_variant('VISTLE_DOUBLE_PRECISION', 'double'))
        args.append(self.define_from_variant('VISTLE_64BIT_INDICES', 'large'))

        args.append(self.define_from_variant('VISTLE_INSTALL_3RDPARTY', 'dev'))

        args.append(self.define_from_variant("VISTLE_USE_QT5", "qt5"))
        if not '+qt' in spec and not '+vr' in spec:
            args.append('-DCMAKE_DISABLE_FIND_PACKAGE_Qt5Core=TRUE')
            args.append('-DCMAKE_DISABLE_FIND_PACKAGE_Qt6Core=TRUE')
        elif '+qt5' in spec:
            args.append('-DCMAKE_DISABLE_FIND_PACKAGE_Qt6Core=TRUE')
        else:
            args.append('-DCMAKE_DISABLE_FIND_PACKAGE_Qt5Core=TRUE')

        return self.cmake_disable_implicit_deps(args)
