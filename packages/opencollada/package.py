# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Opencollada(CMakePackage):
    """A stream based reader and writer library for COLLADA files"""

    homepage = "http://www.opencollada.org/"
    url = "https://github.com/KhronosGroup/OpenCOLLADA/archive/refs/tags/v1.6.68.tar.gz"
    git = "https://github.com/KhronosGroup/OpenCOLLADA.git"

    maintainers("aumuell")


    version("1.6.70", sha256="3ee267857234d928facc8407fffc0a365d3a1956bc67f90ab6f94400c91b56fe")
    version("1.6.68", sha256="d9db0c0a518aa6ac0359626f222707c6ca1b63a83cbf229d97a5999c9cde347b")
    version("1.6.67", sha256="1c83f48371f9ab355268a1805dda33bdf46a4b0e6c495773a657f48b6e6a73ae")
    version("1.6.66", sha256="3b70781168f83482e69982f3904806242238b350162fea874e49343ea04da583")
    version("1.6.65", sha256="c8b4744be671ddf09a112e94503af276cf5fe8d2e52cdf8bbbd3b7b93ac9d5b9")
    version("1.6.64", sha256="82eec237890f1949f53a093eaf38e876c6f95fa55bc3119e6b63db6ea21db055")
    version("1.6.63", sha256="3a0e25f38262d872c393bbf14ff0ce2ef6a7d66bb0d57e080cfd9e37be7ee076")
    version("1.6.62", sha256="a2facf26d58817119f6166eff5de37866d5b869f8642f469914b1debd9cbe56d")
    version("1.6.61", sha256="c0b19d315bf7eaed5f29636ddd962ee7d3c2f7067039dba124bf9f0c94aa9e1e")
    version("1.6.60", sha256="5bd50a9eecc812d26de22c7e195385ab29061c3c9b3c68040efff8ac8cbd7593")
    version("1.6.59", sha256="638ce67a3f8fe0ce99b69ba143f1ecf80813b41ed09438cfbb07aa913f1b89d7")

    depends_on("pcre")
    depends_on("libxml2")
    depends_on("zlib")

    def url_for_version(self, version):
        if version < Version("1.6.70"):
            return super().url_for_version(version)
        url_fmt = "https://github.com/RemiArnaud/OpenCOLLADA/archive/refs/tags/v{0}-max.tar.gz"
        url_fmt = "https://github.com/RemiArnaud/OpenCOLLADA/archive/refs/tags/v{0}-maya.tar.gz"
        return url_fmt.format(version)

    # fix mismatch between <pcre.h> and struct pre-declaration
    patch(
            "https://github.com/Geopipe/OpenCOLLADA/commit/a5e07f588bd5b767eb5278ccdb0252d10a323bee.patch?full_index=1",
            sha256="c22a41ffe2d2dc2acd7feb320cb5d2651696f44bba5fa71066be7c403acfb316"
    )

    # fix build with GCC 13
    patch(
            "https://github.com/KhronosGroup/OpenCOLLADA/pull/656/commits/84c8c9a02b4e5fe40465034563cb36527e865dac.patch?full_index=1",
            sha256="9741a73c9759d12ebb52258b83905ffc06f801e710beaeb224443b58da13f8b4"
    )

    # do not use private copy of zlib
    patch(
            "no-internal-zlib.patch",
    )

    def patch(self):
        filter_file("/lib/opencollada", "/lib", "CMakeLists.txt")

    def cmake_args(self):
        args = []
        args.append("-DUSE_STATIC:BOOL=OFF")
        args.append("-DUSE_SHARED:BOOL=ON")
        #args.append("-DOPENCOLLADA_INST_LIBRARY:STRING={0}/lib".format(self.spec.prefix))
        return args
