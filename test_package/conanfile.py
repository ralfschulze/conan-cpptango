import os

from conans import ConanFile, CMake, tools


class TangoTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%stango_package_test" % os.sep)