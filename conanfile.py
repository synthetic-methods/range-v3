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
from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain
from conan.tools.build import check_min_cppstd

class RangeV3__Conan(ConanFile):
    required_conan_version = ">=2.0.0"

    # Info:
    url = "https://github.com/ericniebler/range-v3"
    name = "range-v3"
    version = "0.12.0"
    license = "Boost Software License - Version 1.0 - August 17th, 2003"
    description = """Experimental range library for C++14/17/20"""

    # Build:
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "CMakeToolchain"
    
    def layout(self):
        cmake_layout(self)

    def validate(self):
        check_min_cppstd(self, 14)

    # Package:
    no_copy_source = True
    exports_sources = "include*", "LICENSE.txt", "CMakeLists.txt", "cmake/*", "Version.cmake", "version.hpp.in"

    def package(self):
        for glob in self.exports_sources:
            copy(self, glob, self.source_folder, self.package_folder)
        cmake = CMake(self)
        cmake.configure({
            "RANGE_V3_DOCS": "OFF",
            "RANGE_V3_PERF": "OFF",
            "RANGE_V3_TESTS": "OFF",
            "RANGE_V3_EXAMPLES": "OFF",
            "RANGE_V3_HEADER_CHECKS": "OFF"
        })
        cmake.install()

    def package_id(self):
        self.info.clear()

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
