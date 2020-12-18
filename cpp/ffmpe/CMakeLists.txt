cmake_minimum_required (VERSION 3.8)

project(one)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-fpermissive")
# 设置头文件的查找位置
include_directories("/usr/local/ffmpeg/include")

link_directories("/usr/local/ffmpeg/lib")

add_executable (two FFMPEG-study-master/FFmpeg-playAudio.cpp)

#设置编译链接的库 ffmpeg
target_link_libraries( two avutil avcodec avformat swscale swresample SDL2)
#target_link_libraries( two avutil avcodec avfilter  avdevice avformat SDL2)
