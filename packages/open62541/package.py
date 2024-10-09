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
    version("1.4.6", sha256="bc4ad185fec5c257e15fcb813b7fef9607b7aaa5d355de7b665e1f210556d38e")
    version("1.4.4", sha256="8d92d4d7b293612efcd87bfe3b833fc2a953d83e4d58045a9186b6cacaad4c58")
    version("1.4.3", sha256="7e7091285221a0b686a08780efb84026cf5728e5b4c59febe230fe77b6d03475")
    version("1.4.2", sha256="0ea31fbe836db685946439db3f06ccb04be86d5914d88327e9f3d641ebe10739")
    version("1.4.1", sha256="4f45f33e4ebd5241142817c4c61a94f2b1353304c8adf9091562bafab6ddb3da")
    version("1.4.0", sha256="22a7a1f821b26f541feb96cc5879e0c76cb3b968e508209b5bf98f2869b11a89")
    version("1.3.14", sha256="826e74e02670b53e04114050e1179d0bd84a0fb8833c7c490a83c8ba12d1a320")
    version("1.3.12", sha256="d31e2aa45de6b7c410b09455ffbd0b361a2205e56e61d2f6a751ded85d9d7871")
    version("1.3.10", sha256="6bb51f55eeaf98fd5d9b61716bbae2ab9ac361fce0e62dfe23f8f2ecfb1de66f")
    version("1.3.8", sha256="b6943b564787c4953b77ca8d7f987c4b896b3f3e91f45d9f13e9056b6148bc1d")
    version("1.3.7", sha256="d3f84f1e2632c15a3892dc6c89f0cd6b4137e990b8aef8fe245cd8e75fbb5388")
    version("1.2.10", sha256="5871633facfd121b301fdcbd106493ba81ad6204aed9872d83af97a635d7422c")
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
