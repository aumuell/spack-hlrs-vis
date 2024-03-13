# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys
from spack.package import *


class Vrpn(CMakePackage):
    """VRPN the Virtual Reality Peripheral Network
       The device-independent, network-transparent system for accessing virtual reality peripherals from VR applications."""

    homepage = "https://vrpn.github.io/"
    url = "https://github.com/vrpn/vrpn/releases/download/version_07.35/vrpn_07.35.zip"
    git = "https://github.com/vrpn/vrpn.git"

    maintainers("aumuell")

    version("master", branch="master", submodules=True)
    version("07.35", sha256="06b74a40b0fb215d4238148517705d0075235823c0941154d14dd660ba25af19")
    version("07.34", sha256="1ecb68f25dcd741c4bfe161ce15424f1319a387a487efa3fbf49b8aa249c9910")
    version("07.33", sha256="3cb9e71f17eb756fbcf738e6d5084d47b3b122b68b66d42d6769105cb18a79be",
            url="https://github.com/vrpn/vrpn/releases/download/v07.33/vrpn_07_33.zip")


    variant("python", default=False, description="Python bindings")
    variant("server", default=False, description="VRPN device server")
    variant("client", default=True, description="VRPN client")

    depends_on("swig")
    depends_on("python@3")
    depends_on("perl")
    depends_on("libusb")
    depends_on("jsoncpp")
    depends_on("hidapi", when=(sys.platform != "darwin"))

    def cmake_args(self):
        """Populate cmake arguments for VRPN."""
        spec = self.spec
        args = []
        args.append(self.define("VRPN_GPL_SERVER", True))
        args.append(self.define("VRPN_BUILD_JAVA", False))
        args.append(self.define("VRPN_USE_MPI", False))
        args.append(self.define("VRPN_BUILD_PYTHON_HANDCODED_2X", False))
        args.append(self.define_from_variant("VRPN_BUILD_PYTHON", "python"))
        args.append(self.define_from_variant("VRPN_BUILD_PYTHON_HANDCODED_3X", "python"))
        args.append(self.define_from_variant("VRPN_BUILD_CLIENTS", "client"))
        args.append(self.define_from_variant("VRPN_BUILD_CLIENT_LIBRARY", "client"))
        args.append(self.define_from_variant("VRPN_BUILD_SERVERS", "server"))
        args.append(self.define_from_variant("VRPN_BUILD_SERVER_LIBRARY", "server"))
        return args
