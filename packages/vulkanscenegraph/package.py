# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Vulkanscenegraph(CMakePackage):
    """Vulkan & C++17 based Scene Graph Project"""

    homepage = "http://www.vulkanscenegraph.org/"
    url = "https://github.com/vsg-dev/VulkanSceneGraph/archive/refs/tags/v1.0.9.tar.gz"
    git = "https://github.com/vsg-dev/VulkanSceneGraph.git"

    maintainers("aumuell")

    version("master", branch="master")
    version("1.0.9", sha256="9a62be7facc13c391c33dc8356b147a3b86f531ea72a28f6b2c364777e761412")

    variant("shared", default=True, description="Build shared libraries")

    depends_on("cmake@3.7:")
    depends_on("vulkan-headers@1.1.70:")
    depends_on("vulkan-loader")
    with when("platform=linux"):
        depends_on("pkg-config")
        depends_on("libxcb")

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))
        return args
