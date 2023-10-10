#include <gtest/gtest.h>

// Include any header files for your code here
// #include "hello_world.h"

int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}