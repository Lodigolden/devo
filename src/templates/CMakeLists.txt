#---------------------------------------------------------------------------------------------------
# Basic Configuration
#---------------------------------------------------------------------------------------------------
cmake_minimum_required(VERSION 3.14)
project(template_project)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(SRC_DIR ${PROJECT_SOURCE_DIR}/src)
set(INC_DIR ${PROJECT_SOURCE_DIR}/inc)
set(TEST_DIR ${PROJECT_SOURCE_DIR}/tests)

#---------------------------------------------------------------------------------------------------
# Included Libraries
#---------------------------------------------------------------------------------------------------
include (FetchContent)

#---------------------------------------------------------------------------------------------------
FetchContent_Declare(
    googletest
    URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

#---------------------------------------------------------------------------------------------------
# Source(s)
#---------------------------------------------------------------------------------------------------
set(LIB_SOURCES
    # ${SRC_DIR}/ex/ex.cpp
)

add_library(${PROJECT_NAME}_lib ${LIB_SOURCES})
target_include_directories(${PROJECT_NAME}_lib PUBLIC
    ${INC_DIR}
    ${SRC_DIR}
)

add_executable(${PROJECT_NAME} 
    ${SRC_DIR}/main.cpp
)
target_link_libraries(${PROJECT_NAME}
    PRIVATE ${PROJECT_NAME}_lib
)

#---------------------------------------------------------------------------------------------------
# Test(s)
#---------------------------------------------------------------------------------------------------
enable_testing()

set(TESTS
    # ${TEST_DIR}/ex_test.cpp
)

add_executable(${PROJECT_NAME}_tests ${TESTS})

target_link_libraries(${PROJECT_NAME}_tests
    GTest::gtest_main
    ${PROJECT_NAME}_lib
)

include(GoogleTest)
gtest_discover_tests(${PROJECT_NAME}_tests)
