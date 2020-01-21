cmake_minimum_required(VERSION 3.9)

SET(CMAKE_C_COMPILER gcc)
SET(CMAKE_CXX_COMPILER g++)

SET(CMAKE_C_FLAGS "-lpthread -O3")
SET(CMAKE_CXX_FLAGS "-fpermissive -lpthread -O3 -std=gnu++17")

project(timeswipe_py DESCRIPTION "timeswipe driver python binding")

SET(SRC src/timeswipe_py.cpp)

add_library(timeswipe_py SHARED ${SRC})
set_target_properties(timeswipe_py PROPERTIES PREFIX "")
set_target_properties(timeswipe_py PROPERTIES OUTPUT_NAME "timeswipe")
set_target_properties(timeswipe_py PROPERTIES SOVERSION 1)

# rasbian has python3 while arch has python
find_package(Boost COMPONENTS python3)
If (Boost_FOUND)
else ()
find_package(Boost COMPONENTS python REQUIRED)
endif ()

find_package(PkgConfig REQUIRED)
pkg_search_module(PYTHON3 REQUIRED python3)
target_include_directories(timeswipe_py PRIVATE ${PYTHON3_INCLUDE_DIRS} src)

#target_link_libraries(timeswipe_py timeswipe ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
target_link_libraries(timeswipe_py timeswipe ${Boost_LIBRARIES})

add_custom_target(
  dep_libs
  COMMAND
  	mkdir -p ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/timeswipe &&
	rm -f ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/timeswipe/* &&
	mv ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/timeswipe.so* ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/timeswipe &&
	python3 ${CMAKE_SOURCE_DIR}/_bundle.py ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/timeswipe/timeswipe.so ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/timeswipe libtimeswipe libboost_python
)
add_dependencies(dep_libs timeswipe_py)

add_custom_target(run ALL
    DEPENDS dep_libs)

