# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from sys import platform

import re

class HlrsCMakePackage(CMakePackage):
    """Collaborative Visualization and Simulation Environment"""

    package_spec = {
        'Qt5Core': 'qt',
        'Qt5Gui': 'qt+gui',
        'Qt5Widgets': 'qt+gui',
        'Qt5OpenGL': 'qt+opengl',
        'Qt5WebEngine': 'qt+webkit',
        'Qt5WebEngineCore': 'qt+webkit',
        'Qt5WebKit': 'qt+webkit',
        'Qt5WebView': 'qt+webkit',
        'Qt6Core': 'qt-base',
        'Qt6GuiTools': 'qt-base',
        'Qt6UiTools': 'qt-tools',
        'Qt6Quick': 'qt-declarative',
        'cfitsio': 'cfitsio',
        'Boost': 'boost',
        'OPENSSL': 'openssl',
        'OpenSSL': 'openssl',
        'OpenAL': 'openal-soft',
        'Git': 'git',
        'VTK': 'vtk',
        'JPEGTURBO': 'libjpeg-turbo',
        'JPEG': 'jpeg',
        'FFMPEG': 'ffmpeg',
        'SNAPPY': 'snappy',
        'TBB': 'tbb',
        'MPI': 'mpi',
        'FLEX': 'flex',
        'BISON': 'bison',
        'SWIG': 'swig',
        'embree': 'embree',
        'SPEEX': 'speex',
        'PROJ4': 'proj',
        'PROJ': 'proj',
        'SDL': 'sdl2',
        'EIGEN': 'eigen',
        'GDAL': 'gdal',
        'GeoTIFF': 'libgeotiff',
        'VTKm': 'vtk-m',
        'Freeimage': 'freeimage',
        'FREEIMAGE': 'freeimage',
        'BLAS': 'blas',
        'LAPACK': 'lapack',
        'OpenEXR': 'openexr',
        'CUDA': 'cuda',
        'CUDAToolkit': 'cuda',
        'PythonLibs': 'python',
        'PythonInterp': 'python',
        'LibUSB1': 'libusb',
        'X11': 'libx11',
        'OpenCV': 'opencv',
        'GLUT': 'freeglut',
        'Cg': None,
        'HIDAPI': 'hidapi',
        'Alut': None,
        'ALUT': None,
        'OpenVR': None,
        'PCL': 'pcl',
        'LibVncServer': None,
        'LIBVNCSERVER': None,
        'NVML': None,
        'VRPN': 'vrpn',
        'Steereo': None,
        'FMOD': None,
        'WIRINGPI': None,
        'ARToolKit': None,
        'NATNET': None,
        'ZSPACE': None,
        'OSGCAL': 'osgcal',
        'OsgQt': None,
        'OsgEarth': 'osgearth',
        'OSGEARTH': 'osgearth',
        'OsgEphemeris': 'osgephemeris',
        'OSGEPHEMERIS': 'osgephemeris',
        'Faro': None,
        'JT': None,
        'SISL': None,
        'E57': 'libe57',
        'OVR': None,
        'SLAM6D': None,
        'WiiYourself': None,
        'PHYSX': None,
        'CUDPP': None,
        'JSBSIM': None,
        'OPENCRG': 'opencrg',
        'LAMURE': None,
        'Schism': None,
        'MidiFile': None,
        'OSC': None,
        'WMFSDK': None,
        'Surface': None,
        'PbrtParser': None,
        'Bonjour': None,
        'VolPack': None,
        'Nifti': None,
        'NORM': None,
        'Protokit': None,
        'Teem': None,
        'GDCM': None,
        'Audiofile': None,
        'OpenNURBS': 'opennurbs',
        'DRACO': 'draco3d',
        'TinyGLTF': 'tinygltf',

        #'PTHREAD': None,

        'Coin3D': 'coin3d',
        'anari': 'anari-sdk',
        'glm': 'glm',
        'Microhttpd': 'libmicrohttpd',
        'Motif': 'motif',
        'ASSIMP': 'assimp',
        'assimp': 'assimp',
        'LibArchive': 'libarchive',
        'LibZip': 'libzip',
        'NETCDF': 'netcdf-cxx4',
        'PNETCDF': 'parallel-netcdf',
        'CGNS': 'cgns',
        'HDF5': 'hdf5',
        'V8': None,
        'CEF': None,

        'Revit': None,
        'Inventor': None,
        'SoQt': None,
        'CFX': None,
        'Abaqus': None,
        'ABAQUS': None,
        'ITK': 'itk',
        'BIFBOF': None,
        'Bullet': None,
        'Xenomai': None,
        'CAL3D': 'cal3d',
        'IFCPP': None,
        'FFTW': 'fftw',
        'Xdmf': 'xdmf3',
    }

    def cmake_disable_implicit_deps(self, args):
        """Append flags to disable searching for packages in standard locations."""

        spec = self.spec

        for package in self.package_spec:
            s = self.package_spec[package]
            if not s or not spec.satisfies('^'+s):
                args.append('-DCMAKE_DISABLE_FIND_PACKAGE_'+package+'=TRUE')

        return args

    def qt_cmake_args(self):
        """Append flags to find all qt dependencies."""
        # Qt components typically install cmake config files in a single prefix,
        # so we have to point them to the cmake config files of dependencies
        qt_prefix_path = []
        re_qt = re.compile("qt-.*")
        for dep in self.spec.dependencies():
            if re_qt.match(dep.name):
                qt_prefix_path.append(self.spec[dep.name].prefix)

        # Now append all qt-* dependency prefixes into a prefix path
        args = []
        args.append(self.define("QT_ADDITIONAL_PACKAGES_PREFIX_PATH", ":".join(qt_prefix_path)))

        return args


class HlrsCovisePackage(HlrsCMakePackage):
    url = "https://github.com/hlrs-vis/covise/releases/download/v2023.9/covise-v2023.9.tar.gz"
    git = "https://github.com/hlrs-vis/covise.git"

    version('master', branch='master', submodules=True)
    version("2023.9", sha256="cdb0a9572c37f2415462fa87a2ff8a1b341ac00415299b2d31f5c8bfd1c0033a")
    version('2021.10', commit='a7efd685a62f955daa6902737db8b73c02b10c96', submodules=True)
    version('2021.9', tag='v2021.9', submodules=True)
    version('2021.7', tag='v2021.7', submodules=True)
    version('2021.1', tag='v2021.1', submodules=True)

    maintainers = ['aumuell']

    depends_on('git', type='build')
    depends_on('cmake@3.3:', type='build')

    def setup_build_environment(self, env):
        """Remove environment variables that let CMake find packages outside the spack tree."""
        env.set('ARCHSUFFIX','spack')
        env.unset('EXTERNLIBS')
        env.unset('COVISEDIR')
        env.unset('COVISEDESTDIR')
        env.unset('COVISE_PATH')

    def cmake_covise_args(self):
        """Populate cmake arguments for COVISE packages."""

        args = []

        args.append('-DCOVISE_WARNING_IS_ERROR=OFF')
        args.append('-DCOVISE_CPU_ARCH:STRING=')
        args.append('-DARCHSUFFIX:STRING=spack')
        args.append('-DQT_DEBUG_FIND_PACKAGE=ON')

        args.extend(HlrsCMakePackage.qt_cmake_args(self))

        return args



class Opencover(HlrsCovisePackage):
    """Collaborative Visualization and Simulation Environment"""

    homepage = "https://www.hlrs.de/opencover"

    provides('cover')

    variant('x11', default=not platform=='darwin', description='Use X11 Window system')
    variant('mpi', default=False, description='Enable MPI support - required for Vistle')
    variant('qt5', default=True, description='Use Qt 5 instead of 6')
    variant('cuda', default=False, description='Enable CUDA support')
    variant('embree', default=False, description='Interactive spray simulation')
    variant('opencv', default=True, description='OpenCV plug-ins')
    variant('ffmpeg', default=True, description='Video output recording')
    variant('osgearth', default=False, description='OsgEarth 3D mapping engine')
    variant('pcl', default=True, description='Enable reading of PCL point cloud files')
    variant('opennurbs', default=False, description='Enable reading of 3DM files')
    variant('virvo', default=True, description='Enable volume rendering')
    variant('drivingsim', default=True, description='Enable driving simulator features')
    variant('visionaray', default=False, description='Enable interactive ray-tracing')

    depends_on('python@2.7:', type=('build', 'run'))

    depends_on('flex', type='build')
    depends_on('bison', type='build')
    depends_on('swig', type='build')

    depends_on('xerces-c cxxstd=17')
    depends_on('curl')
    depends_on('qt+opengl+location@5.15:', when='+qt5')
    depends_on('qt-base+gui+widgets+network+opengl@6:', when='~qt5')
    depends_on('qt-tools', when='~qt5')
    depends_on('qt-declarative', when='~qt5')
    depends_on('glu')
    depends_on('glew')
    depends_on('openscenegraph@3.2:')
    depends_on('libx11', when='+x11')

    depends_on('mpi', when='+mpi')
    depends_on('cuda', when='+cuda')

    depends_on('boost +locale +icu +chrono +timer +program_options +system +thread +filesystem +iostreams +date_time +serialization +regex +atomic')
    depends_on('tbb', when='+visionaray')
    depends_on('eigen')

    depends_on('cfitsio', when='+virvo')

    depends_on('ffmpeg', when='+ffmpeg')
    depends_on('embree@3', when='+embree')
    depends_on('opencv@4.7: +aruco +objdetect +highgui +videoio', when='+opencv')
    depends_on('osgearth', when='+osgearth')

    depends_on('zlib-api')
    depends_on('libpng')
    depends_on('libtiff')
    depends_on('libjpeg-turbo')
    depends_on('libe57')
    depends_on('pcl^hdf5+hl+cxx', when='+pcl')

    depends_on('opencrg')
    depends_on('osgcal')
    depends_on('opennurbs', when='+opennurbs')
    depends_on('draco3d+pic')
    depends_on('tinygltf')
    depends_on('open62541')

    depends_on('hidapi')
    depends_on('vrpn')

    depends_on('fftw')
    depends_on('speex')

    depends_on('proj@:7')


    def cmake_opencover_args(self):
        """Populate cmake arguments for OpenCOVER."""

        spec = self.spec

        args = HlrsCovisePackage.cmake_covise_args(self)

        args.append(self.define_from_variant('COVISE_USE_VIRVO', 'virvo')),
        args.append(self.define_from_variant('COVISE_USE_VISIONARAY', 'visionaray')),
        args.append(self.define_from_variant('COVISE_USE_X11', 'x11')),
        args.append(self.define_from_variant('COVISE_BUILD_DRIVINGSIM', 'drivingsim')),
        args.append(self.define_from_variant('COVISE_USE_QT5', 'qt5')),
        args.append(self.define_from_variant('COVISE_USE_CUDA', 'cuda')),

        return args


    def cmake_args(self):
        """Populate cmake arguments for COVER."""

        spec = self.spec

        args = self.cmake_opencover_args()

        args.append('-DCOVISE_BUILD_ONLY_COVER=ON')

        return self.cmake_disable_implicit_deps(args)
