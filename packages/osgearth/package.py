# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Osgearth(CMakePackage):
    """3D Mapping Engine & C++ SDK for OpenSceneGraph"""

    homepage = "http://osgearth.org/"
    url = "https://github.com/gwaldron/osgearth/archive/refs/tags/osgearth-3.4.tar.gz"
    git = "https://github.com/gwaldron/osgearth"

    maintainers("aumuell")

    version("master", branch="master", submodules=True)
    version("3.4", sha256="2a5aabd6950c598b2310842dfa1e9cf085d54692a0c787cef5627530fcbe682e")
    version("3.3", sha256="4b4a8ba70e707c6aae7d2fe2904b8761e9827398ddeb60633938fe486f5fa622")
    version("3.2", sha256="7e1dd643b1f3b8d1ba9561b899c18176af988342b86c42d89a70be924cb747f6")
    version("3.1", sha256="ad1557583a1f062c67836ce1dafbad9c9d079d0cafe5637158f3e8659a5e82b7")
    version("3.0", sha256="9ea14b63d75e244c02f0ad0227d299cbb804e6bd8767092679adeab2361b7dd2")
    version("2.10.1", sha256="aec8e2d86e700c45aac5e12d352ab7e4011b40c34533c998da7abe18d297af4f")
    version("2.10", sha256="986ad26b8e340a40ac6404137aa61f80a030030fa3e8cf5fbdf183c697f2556e")
    version("2.9", sha256="22aeef42bb700c1e669d9ba57ce4155c0668caf86cc738750a6b9d34c1eaf2a4")
    version("2.8", sha256="5570dc5b62f6f9e28954f5cbd7946a9b35767c06b375eff1c4cc40561e7f1655")
    version("2.7", sha256="945bd4d0bc65143a14caeb434b07384eccef1ba89ae11282fc499903a251ec18")

    depends_on("openscenegraph")
    depends_on("libzip")
    depends_on("libwebp")
    depends_on("sqlite")
    depends_on("gdal")
    depends_on("geos")
    depends_on("glew")
    depends_on("draco3d")
    depends_on("rapidjson")
    depends_on("protobuf@:3.21")
    depends_on("c-blosc")

    def patch(self):
        # handle AppleClang as Clang
        filter_file("STREQUAL \"Clang\"", "MATCHES \"Clang\"", "CMakeModules/CXX11.cmake")
        # rapidjson is not included in distribution, but CMakeLists.txt assumes so
        filter_file("\\${OSGEARTH_EMBEDDED_THIRD_PARTY_DIR}/rapidjson/include/rapidjson", "{0}/include/rapidjson".format(self.spec["rapidjson"].prefix), "src/osgEarthDrivers/gltf/CMakeLists.txt")
        # disable lerc - not included in distribution
        filter_file("add_subdirectory\\(lerc\\)", "", "src/osgEarthDrivers/CMakeLists.txt")
        #if self.spec.satisfies("@:3.3"):
            #filter_file("../../third_party/lerc/include", "{0}/include".format(self.spec["lerc"].prefix), "src/osgEarthDrivers/lerc/CMakeLists.txt")

        args = []
        args.append("-DOSGEARTH_BUILD_TESTS:BOOL=OFF")
        return args
