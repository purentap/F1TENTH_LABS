# Install script for directory: /home/puren/ros_workspaces/f1tenth_labs/lab1/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/puren/ros_workspaces/f1tenth_labs/lab1/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/puren/ros_workspaces/f1tenth_labs/lab1/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/puren/ros_workspaces/f1tenth_labs/lab1/install" TYPE PROGRAM FILES "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/puren/ros_workspaces/f1tenth_labs/lab1/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/puren/ros_workspaces/f1tenth_labs/lab1/install" TYPE PROGRAM FILES "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/puren/ros_workspaces/f1tenth_labs/lab1/install/setup.bash;/home/puren/ros_workspaces/f1tenth_labs/lab1/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/puren/ros_workspaces/f1tenth_labs/lab1/install" TYPE FILE FILES
    "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/catkin_generated/installspace/setup.bash"
    "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/puren/ros_workspaces/f1tenth_labs/lab1/install/setup.sh;/home/puren/ros_workspaces/f1tenth_labs/lab1/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/puren/ros_workspaces/f1tenth_labs/lab1/install" TYPE FILE FILES
    "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/catkin_generated/installspace/setup.sh"
    "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/puren/ros_workspaces/f1tenth_labs/lab1/install/setup.zsh;/home/puren/ros_workspaces/f1tenth_labs/lab1/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/puren/ros_workspaces/f1tenth_labs/lab1/install" TYPE FILE FILES
    "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/catkin_generated/installspace/setup.zsh"
    "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/puren/ros_workspaces/f1tenth_labs/lab1/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/puren/ros_workspaces/f1tenth_labs/lab1/install" TYPE FILE FILES "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/gtest/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/visualization_tutorials/visualization_tutorials/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/lab1_pkg/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/reactive_gap_following/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/safety_node/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/particle_filter/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/pure_pursuit/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/f1tenth_simulator/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/visualization_tutorials/interactive_marker_tutorials/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/visualization_tutorials/librviz_tutorial/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/visualization_tutorials/rviz_plugin_tutorials/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/visualization_tutorials/rviz_python_tutorial/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/visualization_tutorials/visualization_marker_tutorials/cmake_install.cmake")
  include("/home/puren/ros_workspaces/f1tenth_labs/lab1/build/wall_following/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/puren/ros_workspaces/f1tenth_labs/lab1/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
