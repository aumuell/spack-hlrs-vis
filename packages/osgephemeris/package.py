# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install osgephemeris
#
# You can edit this file again by typing:
#
#     spack edit osgephemeris
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Osgephemeris(CMakePackage):
    """OpenSceneGraph Ephemeris Model"""

    homepage = "http://www.andesengineering.com/Projects/OsgEphemeris/"
    git = "https://github.com/hlrs-vis/osgephemeris"

    maintainers("aumuell")

    version("1.0.1", commit="ef923a437831e0f3b574b5e802e3aa0e74b4df58")

    depends_on("openscenegraph")

    root_cmakelists_dir = "osgEphemeris"
