# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VulkanLoader(CMakePackage):
    """Vulkan loader"""

    homepage = "https://vulkan.lunarg.com/doc/sdk/latest/linux/LoaderInterfaceArchitecture.html"
    url = "https://github.com/KhronosGroup/Vulkan-Loader/archive/refs/tags/v1.3.263.tar.gz"
    git = "https://github.com/KhronosGroup/Vulkan-Loader.git"

    maintainers("aumuell")

    version("main", branch="main")
    version("1.3.265", sha256="fffca4a5e6daf3bbe18585f96bf7cad8cf173ebf3fa4d00b755108bd0b129bd8")

    depends_on("vulkan-headers")
    depends_on("pkg-config", type="build")
    depends_on("python@3", type="build")

    with when("platform=linux"):
        depends_on("libxrandr", type="build")
        depends_on("libx11")
        depends_on("libxcb")
        depends_on("wayland")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args

#  def install
#    system "cmake", "-S", ".", "-B", "build",
#                    "-DVULKAN_HEADERS_INSTALL_DIR=#{Formula["vulkan-headers"].opt_prefix}",
#                    "-DFALLBACK_DATA_DIRS=#{HOMEBREW_PREFIX}/share:/usr/local/share:/usr/share",
#                    "-DCMAKE_INSTALL_SYSCONFDIR=#{etc}",
#                    "-DFALLBACK_CONFIG_DIRS=#{etc}/xdg:/etc/xdg",
#                    *std_cmake_args
#    system "cmake", "--build", "build"
#    system "cmake", "--install", "build"
#
#    inreplace lib/"pkgconfig/vulkan.pc", /^Cflags: .*/, "Cflags: -I#{Formula["vulkan-headers"].opt_include}"
#  end

