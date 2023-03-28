# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Osgcal(CMakePackage):
    """Cal3D adapter for OpenSceneGraph, imported from https://sourceforge.net/p/osgcal/code"""

    homepage = "http://osgcal.sourceforge.net"
    git      = "https://github.com/hlrs-vis/osgcal.git"

    maintainers = ['aumuell']

    version('master', tag='master')
    version('2022.5', commit='66f92936b4783627b71ca640e38cc3789d6dc479')
    version('2021.10', commit='ab2bbb1579479923acd6b96a07101bf07cec3038')
    version('2018.5.1', commit='fbefbd54bb4ec822bb192073f93e904b2645a162')

    depends_on('openscenegraph')
    depends_on('cal3d')

    root_cmakelists_dir = 'osgCal'

    def test(self):
        """Perform smoke tests on the installed package."""
        self.run_test('osgCalViewer', ['-h'], [], installed=True,
                      purpose=reason, skip_missing=True, work_dir='.')
