# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VulkanHeaders(CMakePackage):
    """Vulkan header files and API registry"""

    homepage = "https://www.vulkan.org/"
    url = "https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.3.263.tar.gz"
    git = "https://github.com/KhronosGroup/Vulkan-Headers.git"

    maintainers("aumuell")

    version("main", branch="main")
    version("1.3.265", sha256="24076540521da1eceecfb56235cb0361a01fb24a306cbefe874c949bf2d2e9a4")

    depends_on("libxrandr", when="platform=linux")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
