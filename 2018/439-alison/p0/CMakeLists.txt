cmake_minimum_required(VERSION 3.9)
project(p0)

set(CMAKE_CXX_STANDARD 11)
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")

add_executable(fib fib.c)
add_executable(psh psh.c util.c)
add_executable(handle util.c handle.c)
add_executable(mykill mykill.c)
add_executable(msh msh.c util.c jobs.c)