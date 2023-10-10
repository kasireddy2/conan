from conans import ConanFile, CMake

class HelloWorldConan(ConanFile):
    name = "hello_world"
    version = "1.0"
    license = "MIT"  # Specify your license
    url = "https://github.com/your_username/hello_world"  # URL of your project
    description = "A simple Hello World program"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello_world"]