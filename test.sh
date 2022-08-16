#!/usr/bin/env sh

conan install --build=missing conan/
conan install --build=missing conan/ -s build_type=Debug

conan build conan/
# This next one fails, because the debug lib of spdlog is found first.
cd build && cmake --build . --config Release
