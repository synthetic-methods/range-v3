# Range v3 library
#
#  Copyright Luis Martinez de Bartolome Izquierdo 2016
#
#  Use, modification and distribution is subject to the
#  Boost Software License, Version 1.0. (See accompanying
#  file LICENSE_1_0.txt or copy at
#  http://www.boost.org/LICENSE_1_0.txt)
#
# Project home: https://github.com/ericniebler/range-v3
#
import os
from conan             import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class RangeV3_TestPackage__Conan(ConanFile):
    required_conan_version = ">=2.0.0"

    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def imports(self):
        for glob in ["*.dll", "*.dylib"]:
            self.copy(glob, "bin", "bin")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        os.chdir(self.cpp.build.bindir)
        self.run(".%srange-v3-example" % os.sep)
