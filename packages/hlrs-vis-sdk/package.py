# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class HlrsVisSdk(BundlePackage):
    """Dependencies and tools for COVISE and Vistle development"""

    homepage = "https://github.com/hlrs-vis"
    maintainers("aumuell")

    version("2023.10")

    variant("vistle", default=True, description="install dependencies for Vistle")
    variant("covise", default=False, description="install dependencies for COVISE")
    variant("cover", default=True, description="install dependencies for OpenCOVER")
    variant("qt5", default=False, description="use Qt5 instead of Qt6")
    variant("mpi", default=True, description="use MPI")

    depends_on("boost +atomic+chrono+container+date_time+exception+filesystem+graph+icu+iostreams+locale+log+math+multithreaded+program_options+random+regex+serialization+system+thread+timer+wave cxxstd=17")
    depends_on("boost +mpi", when="+mpi")
    depends_on("boost ~mpi", when="~mpi")

    depends_on("ninja")
    depends_on("cmake")
    depends_on("pkg-config") # Zstd for SZ3 in Vistle

    depends_on("python@3")
    depends_on("zlib-api")

    with when("+qt5"):
        depends_on("qt@5.15: +gui+opengl+tools")
    with when("~qt5"):
        depends_on("qt-base +gui+opengl+network")
        depends_on("qt-svg")

    with when("+vistle"):
        depends_on("mpi", when="+mpi")
        depends_on("tbb")
        depends_on("hwloc")
        depends_on("llvm-openmp", when="platform=darwin")

        depends_on("ispc@1.20:")
        depends_on("embree+ispc@4.3:")
        #depends_on("anari-sdk +examples +helide")

        depends_on("botan")
        depends_on("proj@7:")
        depends_on("cgal")

        depends_on("lz4")
        depends_on("zstd")
        depends_on("libjpeg-turbo")

        depends_on("netcdf-c +hdf4") # for MPAS data
        depends_on("netcdf-c ~mpi", when="~mpi")
        depends_on("netcdf-c +mpi", when="+mpi")
        depends_on("netcdf-cxx4")
        depends_on("parallel-netcdf", when="+mpi")

        depends_on("tinyxml2")
        # repeat those for COVISE
        depends_on("vtk@9: ~mpi", when="~mpi")
        depends_on("vtk@9: +mpi", when="+mpi")
        depends_on("libzip")
        depends_on("libarchive")
        depends_on("assimp")
        depends_on("cfitsio")

    def cover_deps():
        depends_on("flex")
        depends_on("bison")
        depends_on("xerces-c")

        depends_on("glew")
        depends_on("openscenegraph +apps +dcmtk +gdal +gta +inventor +opencascade +openexr +pdf +svg")
        depends_on("osgcal")
        depends_on("vrpn")
        depends_on("hidapi")
        depends_on("opencv")
        depends_on("opencv@4.7: +aruco +objdetect +highgui +videoio")
        depends_on("ffmpeg")
        depends_on("libtiff")
        depends_on("tinygltf")
        depends_on("draco3d+pic")
        depends_on("libe57")
        depends_on("speex")

        with when("~qt5"):
            depends_on("qt-tools")
            depends_on("qt-declarative")
            #depends_on("qt-webengine")

    with when("+cover"):
        cover_deps()

    with when("+covise"):
        cover_deps()

        depends_on("swig")

        depends_on("proj@:7")

        depends_on("vtk@9: ~mpi", when="~mpi")
        depends_on("vtk@9: +mpi", when="+mpi")
        depends_on("libzip")
        depends_on("libarchive")
        depends_on("assimp")
        depends_on("cfitsio")
