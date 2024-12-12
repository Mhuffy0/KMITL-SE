#include <iostream>

void printTri(int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j <= i; j++)
        {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
}

void printRevTri(int size) {
    for (int i = size - 1; i > 0; i--) {
        for (int j = 0; j < i; j++)
        {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
}

int main() {
    int size;
    std::cout << "Enter size\n";
    std::cin >> size;

    printTri(size);
    std::cout << "REV\n";

    printTri(size);
    printRevTri(size);
}