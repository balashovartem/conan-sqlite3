from conans.model.conan_file import ConanFile
from conans import CMake
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "balashovartem")

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "sqlite3/3.14.1@%s/%s" % (username, channel)

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line ) )
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.run(".%sbin%stest " % (os.sep, os.sep))
