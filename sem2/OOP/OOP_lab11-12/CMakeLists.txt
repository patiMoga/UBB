cmake_minimum_required(VERSION 3.24)
project(OOP_lab11_12)

set(CMAKE_CXX_STANDARD 17)

add_executable(OOP_lab11_12 main.cpp Produse.h Produse.cpp Repo_tonomat.h Repo_tonomat.cpp Service.h Service.cpp teste.h teste.cpp UI.h UI.cpp FileRepository.h FileRepository.cpp utils/MyException.h utils/MyValidator.h utils/FileException.h utils/ValidatorError.h utils/PurchesException.h)
