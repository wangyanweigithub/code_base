#!/usr/bin/python3
import os
import sys
import shutil
import subprocess


def build_opencv(omk_file):
    cons = ["project(one)","cmake_minimum_required(VERSION 3.5)", 
            "find_package(OpenCV REQUIRED)", "add_executable(main %s)" % omk_file,
            "target_link_libraries(main ${OpenCV_LIBS})"]

    with open("CMakeLists.txt", "w") as f:
        f.write("\n".join(cons))

    cmake = ["cmake",".", "-B", "build"]
    subprocess.run(cmake)

    os.chdir("./build")
    subprocess.run("make")

    shutil.move("main", "../")
    os.chdir("../")
    subprocess.run("./main")


if __name__ == "__main__":
    omk_file = sys.argv[1] if len(sys.argv)>1 else "main.cpp"
    files = os.listdir(os.getcwd())
    
    if omk_file not in files:
        raise Exception("not have source cpp")

    build_opencv(omk_file)
