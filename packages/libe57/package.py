# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Libe57(CMakePackage):
    """Software Tools for Managing E57 Point Cloud Files"""

    homepage = 'http://libe57.org'
    git      = "https://github.com/hlrs-vis/libe57.git"

    maintainers = ['aumuell']

    version('master', preferred=False, branch='master')
    version('1.1.334', tag='v1.1.334')
    version('1.1.333', tag='v1.1.333')

    #url "https://github.com/hlrs-vis/libe57.git", branch: "main", revision: "6c6b0c8355d870342f1736bfcc3b5299fe012d4c"
    #license "http://libe57.org/license.html"
    #head "https://github.com/hlrs-vis/libe57.git", branch: "main"

    depends_on('cmake@3.3:', type='build')
    depends_on('boost+multithreaded')
    depends_on('xerces-c')

    def cmake_args(self):
        """Populate cmake arguments for LibE57."""
        spec = self.spec

        args = []

        return args

    def test(self):
        """Perform smoke tests on the installed package."""
        self.run_test('e57validate', [], [], installed=True,
                      purpose=reason, skip_missing=True, work_dir='.')
