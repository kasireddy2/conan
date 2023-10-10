cpp
Copy code
#include <gtest/gtest.h>

// Include the header file(s) for your code here
#include "hello_world.h"

TEST(HelloWorldTest, TestHelloWorld) {
    ASSERT_EQ(hello_world_function(), "Hello, World!");
}