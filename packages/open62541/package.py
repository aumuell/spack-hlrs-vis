# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Open62541(CMakePackage):
    """Open source implementation of OPC UA (OPC Unified Architecture) aka IEC 62541"""

    homepage = "https://www.open62541.org/"
    url = "https://github.com/open62541/open62541/archive/refs/tags/v1.3.6.tar.gz"
    git = "https://github.com/open62541/open62541.git"

    maintainers("aumuell")

    variant("shared", default=True, description="Build shared libraries")

    version("master", branch="master", submodules=True)
    version("1.3.6", sha256="0751ce6273908b1e571f36591665f3d5b9451514c2478ea5f6b4b466d7da6b02")
    version("1.2.7", sha256="6bf64ce86f2e5e1d5c7213e13577ebf6d6c8a3a41fc3e33d1fbdb29117e9ef5b")

    depends_on("python@3")
    depends_on("openssl")

    def cmake_args(self):
        args = [
                self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
                self.define("UA_ENABLE_DISCOVERY", True),
                self.define("UA_ENABLE_HISTORIZING", True),
                self.define("UA_ENABLE_JSON_ENCODING", True),
                self.define("UA_ENABLE_ENCRYPTION", "OPENSSL"),
                self.define("PYTHON_EXECUTABLE", self.spec["python"].command.path),
                ]
        self.spec["python"].command.path
        return args
