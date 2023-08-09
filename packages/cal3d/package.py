# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Cal3d(AutotoolsPackage):
    """Skeletal 3D character animation library written in C++"""

    homepage = 'http://cal3d.sourceforge.net/docs/api/html/cal3dfaq.html'
    git      = "https://github.com/hlrs-vis/cal3d.git"

    maintainers = ['aumuell']

    version('master', preferred=False, branch='master')
    version('2021.10', commit='8c45a264acb881c026c3e3c2e7a07826aa2eaa01')
    version('2018.5.2', commit='8cbf44f8c20a191b67063cb943420ec55e7125b8')

    #url "https://github.com/hlrs-vis/libe57.git", branch: "main", revision: "6c6b0c8355d870342f1736bfcc3b5299fe012d4c"
    #license "http://libe57.org/license.html"
    #head "https://github.com/hlrs-vis/libe57.git", branch: "main"

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

    def cmake_args(self):
        """Populate cmake arguments for Cal3D."""
        spec = self.spec

        args = []

        return args

    def test(self):
        """Perform smoke tests on the installed package."""
        self.run_test('cal3d_converter', ['--help'], [], installed=True,
                      purpose=reason, skip_missing=True, work_dir='.')
