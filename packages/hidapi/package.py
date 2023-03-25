# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Hidapi(CMakePackage):
    """Library for communicating with USB and Bluetooth HID devices"""

    homepage = "https://github.com/libusb/hidapi"
    url = "https://github.com/libusb/hidapi/archive/hidapi-0.13.1.tar.gz"
    git = "https://github.com/libusb/hidapi.git"

    maintainers("aumuell")

    version('master', branch='master', submodules=True)
    version("0.13.1", sha256="476a2c9a4dc7d1fc97dd223b84338dbea3809a84caea2dcd887d9778725490e3")
    version("0.13.0", sha256="e35eabe4ad59bd6e24dce6136f084997cdecd9bb7f6e83b40f3cc15b0ea8d56f")
    version("0.12.0", sha256="28ec1451f0527ad40c1a4c92547966ffef96813528c8b184a665f03ecbb508bc")
    version("0.11.2", sha256="bc4ac0f32a6b21ef96258a7554c116152e2272dacdec1e4620fc44abeea50c27")
    version("0.11.0", sha256="391d8e52f2d6a5cf76e2b0c079cfefe25497ba1d4659131297081fc0cd744632")
    version("0.10.1", sha256="f71dd8a1f46979c17ee521bc2117573872bbf040f8a4750e492271fc141f2644")
    version("0.10.0", sha256="68febd416cb6e6e6e205c9dd46a6f86f0d5a9808b7cd8c112906cd229889b8e1")

    #depends_on('fox')
    depends_on('libusb')

    def cmake_args(self):
        """Populate cmake arguments for Hidapi."""
        spec = self.spec
        args = []
        args.append('-DHIDAPI_BUILD_HIDTEST=ON')
        return args

#  depends_on "pkg-config" => :build
#
#  on_linux do
#    depends_on "libusb"
#    depends_on "systemd" # for libudev
#  end
#
#  def install
#    mkdir "build" do
#      system "make", "install"
#
#      # hidtest/.libs/hidtest does not exist for Linux, install it for macOS only
#      bin.install "hidtest/hidtest" if OS.mac?
#    end
#  end
#
#  test do
#    (testpath/"test.c").write <<~EOS
#      #include "hidapi.h"
#      int main(void)
#      {
#        return hid_exit();
#      }
#    EOS
#
#    flags = ["-I#{include}/hidapi", "-L#{lib}"]
#    flags << if OS.mac?
#      "-lhidapi"
#    else
#      "-lhidapi-hidraw"
#    end
#    flags += ENV.cflags.to_s.split
#    system ENV.cc, "-o", "test", "test.c", *flags
#    system "./test"
#  end
#end
