from conans import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout


class MulticonfigConan(ConanFile):
    name = "multiconfig"
    license = "MIT"
    author = "adnn"
    description = "Illustrate an issue with multiconfig generation."
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
    }
    default_options = {
        "shared": False,
    }

    requires = (
        ("spdlog/1.9.2"),
    )

    build_policy = "missing"
    generators = "CMakeDeps", "CMakeToolchain"

    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto",
        "submodule": "recursive",
    }


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake


    def layout(self):
        # Otherwise, root is the folder containing conanfile.py
        self.folders.root = ".."
        # Handles single-config (with subfolders) and multi-config (in a common folder)
        cmake_layout(self)


    def build(self):
        cmake = self._configure_cmake()
        cmake.build()


    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
