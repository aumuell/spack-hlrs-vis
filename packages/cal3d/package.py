# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Cal3d(AutotoolsPackage):
    """Skeletal 3D character animation library written in C++"""

    homepage = 'http://cal3d.sourceforge.net/docs/api/html/cal3dfaq.html'
    url = "https://github.com/hlrs-vis/cal3d/archive/refs/tags/v2021.10.tar.gz"
    git  = "https://github.com/hlrs-vis/cal3d.git"

    maintainers = ['aumuell']

    version("master", preferred=False, branch="master")
    version("2024.1", sha256="ea92fa0e7ec4f831d17ab04de5413f88d6a861f2260f64593ceee3c9f6b618ac")
    version("2021.10", sha256="f35bb2dd034f254cecf47f66b67bb76aa421180bd662f0258760b9a2875f5a07")
    version("2018.5.2", sha256="55e61e04d85e4fd8bb608f477558ffcb616a48988f9e45ec244aa2ef59e21732")

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('pkg-config', type='build')

    configure_directory = 'cal3d'
    autoreconf_extra_args = ["-i"]

    def configure_args(self):
        args = []

        args.append('--disable-debug')
        args.append('--disable-unittest')
        args.append('--disable-dependency-tracking')
        args.append('--disable-silent-rules')
        args.append('--prefix={0}'.format(self.prefix))

        return args

    def test(self):
        """Perform smoke tests on the installed package."""
        self.run_test('cal3d_converter', ['--help'], [], installed=True,
                      purpose=reason, skip_missing=True, work_dir='.')
