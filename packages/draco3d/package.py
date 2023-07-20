# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Draco3d(CMakePackage):
    """3D geometric mesh and point cloud compression library"""
    homepage = "https://google.github.io/draco/"
    url = "https://github.com/google/draco/archive/1.5.6.tar.gz"
    git = "https://github.com/google/draco/"

    maintainers("aumuell")

    variant("pic", default=False, description="Produce position-independent code")

    version("master", branch="master")
    version("1.5.6", sha256="0280888e5b8e4c4fb93bf40e65e4e8a1ba316a0456f308164fb5c2b2b0c282d6")
    version("1.4.3", sha256="02a620a7ff8388c57d6f6e0941eecc10d0c23ab47c45942fb52f64a6245c44f5")

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant

        args = [
                from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
        ]
        return args
