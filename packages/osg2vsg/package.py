# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Osg2vsg(CMakePackage):
    """Adapter library for converting OpenSceneGraph Images and 3D models to VulkanSceneGraph"""

    homepage = "https://github.com/vsg-dev/osg2vsg"
    url = "https://github.com/vsg-dev/osg2vsg/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/vsg-dev/osg2vsg.git"

    maintainers("aumuell")

    version("master", branch="master")
    version("0.1.0", sha256="3af6cc7ef98ffb9a03315aee66400160d3339b336351eca67b10f745f435cadc")

    variant("shared", default=True, description="Build shared libraries")

    depends_on("cmake@3.7:")
    depends_on("vulkanscenegraph@1.0.3:")
    depends_on("openscenegraph@3.6:")

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))
        return args
