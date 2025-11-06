cmake_minimum_required(VERSION 3.18.1)
project("whitelist-tunnel")

add_library(whitelist-tunnel SHARED
            native-tunnel.cpp)

find_library(log-lib log)

target_link_libraries(whitelist-tunnel ${log-lib})
