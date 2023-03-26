# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

import os


class Opencrg(MakefilePackage):
    """Creation and evaluation of road surfaces"""

    homepage = "https://www.asam.net/standards/detail/opencrg/"
    git      = "https://github.com/hlrs-vis/opencrg.git"

    maintainers = ['aumuell']

    version('master',
            git = 'https://code.asam.net/simulation/standard/asam-opencrg.git',
            branch='master')
    version('1.2.0',
            git = 'https://code.asam.net/simulation/standard/asam-opencrg.git',
            commit='21a9d1d6edfb87ad9b8ab51005c9063e7d44ae31')
    version('1.1.2', tag='v1.1.2', preferred=True)
    version('1.1.1', tag='v1.1.1')
    version('1.1.0-rc1', tag='v1.1.0-rc1')
    version('1.0.6', tag='v1.0.6')
    version('1.0.5-rc1', tag='v1.0.5-rc1')
    version('1.0.4', tag='v1.0.4')
    version('1.0.3', tag='v1.0.3')
    version('1.0.2', tag='v1.0.2')

    parallel = False

    @property
    def build_targets(self):
        spec = self.spec

        basedir = ''
        if spec.version >= Version('1.2.0'):
            basedir = 'c-api/baselib/'

        # these directories exist in .zip archives, but not in the source repository
        mkdirp('{0}obj'.format(basedir))
        mkdirp('{0}lib'.format(basedir))

        args = []
        if spec.version >= Version('1.2.0'):
            args.append('-C')
            args.append(basedir)

        args.append('REVISION={0}'.format(self.version))
        args.append('COMP={0}'.format(self.compiler.cc))
        args.append('CFLGS={0} {1} {2} -Iinc'.format(self.compiler.cc_pic_flag, self.compiler.debug_flags[0], self.compiler.opt_flags[3]))

        return args


    def install(self, spec, prefix):
        basedir = ''
        if spec.version >= Version('1.2.0'):
            basedir = 'c-api/baselib/'

        mkdir(prefix.include)
        install('{0}inc/crgBaseLibPrivate.h'.format(basedir), prefix.include)
        install('{0}inc/crgBaseLib.h'.format(basedir), prefix.include)

        mkdir(prefix.lib)
        install('{0}lib/libOpenCRG.{1}.a'.format(basedir, self.version), '{0}/libOpenCRG.a'.format(prefix.lib))
