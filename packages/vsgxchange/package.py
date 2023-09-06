# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Vsgxchange(CMakePackage):
    """Utility library for converting data+materials to/from VulkanSceneGraph"""

    homepage = "https://github.com/vsg-dev/vsgXchange"
    url = "https://github.com/vsg-dev/vsgXchange/archive/refs/tags/v1.0.5.tar.gz"
    git = "https://github.com/vsg-dev/vsgXchange.git"

    maintainers("aumuell")

    version("master", branch="master")
    version("1.0.5", sha256="b43aeb4619f86bd2b17db67560b4c92e2e0805477a6adc2a55e47ae995ca33d7")

    variant("osg", default=False, description="I/O for OpenSceneGraph formats")
    variant("openexr", default=False, description="OpenEXR image support")
    variant("shared", default=True, description="Build shared libraries")

    depends_on("cmake@3.7:")
    depends_on("vulkanscenegraph@1.0.8:")
    depends_on("assimp@5")
    depends_on("gdal")
    depends_on("openexr@3", when="+openexr")
    depends_on("curl")
    depends_on("freetype")
    depends_on("osg2vsg", when="+osg")

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))
        return args
