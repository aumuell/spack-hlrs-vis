# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
from spack.pkg.builtin.qt_base import QtBase, QtPackage


class QtTools(QtPackage):
    """Classes for loading QWidget based forms created in Qt Designer dynamically, at runtime."""

    url = QtPackage.get_url(__qualname__)
    list_url = QtPackage.get_list_url(__qualname__)

    version("6.6.1", sha256="6e5816628a2cdcf4147483f7d088870695af7d9770d4e2b68a0765fda5b3e12a")
    version("6.6.0", sha256="b7e3f49543176cea0b48641d115e00f4779b7c366b9fcf70235abe1b50b89112")
    version("6.5.3", sha256="e0f7407ef889688aaddaba3b6984da10e009189659d403e141e3b81580da2294")
    version("6.5.2", sha256="962a343f090adcf73340f72cb81655b6243f7b4d91a980e0f538c2a111e1aa3a")
    version("6.5.1", sha256="d86516cb8083ce6088fae9f900490c41cf4e472c51e4334e06e5dbb2e24fe688")
    version("6.5.0", sha256="e775a323eab8acb4367f910b572ffacb71dc91d78d79f31eee472ae4214ba5e9")
    version("6.4.3", sha256="d0bce31c0780630f6f15a531a07f727a4bf409f9b6af3348c462b5c044b12920")
    version("6.4.2", sha256="ee77e3e48cffe068edaf5fe119eb64dab6f65c26d79936a2e35abf7f3e0deeff")
    version("6.4.1", sha256="81b705e6fd4bee56f40fe9f4bc1621bbe0dc590cfdc07380e29064a146cdeb34")
    version("6.4.0", sha256="b408ed50b0523ee9cc8fab94db2cd73e7ac693605764b12ec251c99563877ff2")
    version("6.3.2", sha256="a1b1cae6112f693d422686c786a25e9180f346250ba95ac4c519b58f41f3d2ed")

    variant("dbus", default=False, description="Build dbus support.")
    variant("llvm", default=False, description="Build with lupdate support.")

    depends_on("qt-base +gui +network")
    depends_on("qt-base +dbus", when="+dbus")
    depends_on("llvm +clang", when="+llvm")

    for _v in QtBase.versions:
        v = str(_v)
        depends_on("qt-base@" + v, when="@" + v)

    def cmake_args(self):
        args = super().cmake_args() + [
                self.define("FEATURE_assistant", False),
                self.define("FEATURE_clang", "+llvm" in self.spec),
                self.define("FEATURE_clangcpp", "+llvm" in self.spec),
                ]
        return args
