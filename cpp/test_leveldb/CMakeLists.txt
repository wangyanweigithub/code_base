cmake_minimum_required(VERSION 3.9)

project(one)

include_directories(/home/wang/F/git_open/leveldb/include)

link_directories(/home/wang/F/git_open/leveldb/build)

add_executable(mai a.cpp)

target_link_libraries(mai leveldb pthread )
