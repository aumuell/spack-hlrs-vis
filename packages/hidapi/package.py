# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Hidapi(CMakePackage):
    """Library for communicating with USB and Bluetooth HID devices"""

    homepage = "https://github.com/libusb/hidapi"
    url = "https://github.com/libusb/hidapi/archive/hidapi-0.13.1.tar.gz"
    git = "https://github.com/libusb/hidapi.git"

    maintainers("aumuell")

    version('master', branch='master', submodules=True)
    version("0.14.0", sha256="a5714234abe6e1f53647dd8cba7d69f65f71c558b7896ed218864ffcf405bcbd")
    version("0.13.1", sha256="476a2c9a4dc7d1fc97dd223b84338dbea3809a84caea2dcd887d9778725490e3")
    version("0.12.0", sha256="28ec1451f0527ad40c1a4c92547966ffef96813528c8b184a665f03ecbb508bc")
    version("0.11.2", sha256="bc4ac0f32a6b21ef96258a7554c116152e2272dacdec1e4620fc44abeea50c27")
    version("0.10.1", sha256="f71dd8a1f46979c17ee521bc2117573872bbf040f8a4750e492271fc141f2644")

    # depends on systemd/systemd-devel provided by system
    variant("libudev", default=False, description="Build with libudev")

    depends_on('pkgconfig', type='build')
    depends_on('libusb')
    depends_on('libiconv')

    def cmake_args(self):
        """Populate cmake arguments for Hidapi."""
        spec = self.spec
        args = []
        args.append("-DHIDAPI_BUILD_HIDTEST=ON"),
        args.append(self.define_from_variant("HIDAPI_WITH_HIDRAW", "libudev")),
        return args
