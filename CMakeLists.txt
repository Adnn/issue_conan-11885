cmake_minimum_required(VERSION 3.20)

project(Multiconfig)

add_executable(${PROJECT_NAME}
    main.cpp
)

find_package(spdlog CONFIG REQUIRED)

target_link_libraries(${PROJECT_NAME}
    PRIVATE
        spdlog::spdlog
)
