# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Osgcal(CMakePackage):
    """Cal3D adapter for OpenSceneGraph, imported from https://sourceforge.net/p/osgcal/code"""

    homepage = "http://osgcal.sourceforge.net"
    url = "https://github.com/hlrs-vis/osgcal/archive/refs/tags/2022.5.tar.gz"
    git = "https://github.com/hlrs-vis/osgcal.git"

    maintainers = ['aumuell']

    version('master', tag='master')
    version("2022.5", sha256="ae35a1b84ed89f5a57e3dc294f8f737056df7cff95fc3cf0cc935765c7f059b5")
    version("2021.10", sha256="0a4818e58e5e9cb4e44bad2f21c93e8a406e3d185b431cba3d912fb1a5d01471")
    version("2018.5.1", sha256="a819efdbcee6a46c1d831e33b928abf1cb734c9c82b473359d43ea8c7241ded8")

    depends_on('openscenegraph')
    depends_on('cal3d')

    root_cmakelists_dir = 'osgCal'

    def test(self):
        """Perform smoke tests on the installed package."""
        self.run_test('osgCalViewer', ['-h'], [], installed=True,
                      purpose=reason, skip_missing=True, work_dir='.')
