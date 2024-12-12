#include <iostream>

int main() {
    std::cout << "Face Length of cube\t" << "Surface area of cube\t" << "Volume of cube\t\n";
    std::cout << "(cm)\t\t\t" << "(cm 2)\t\t\t" << "(cm 3)\t\t\t\n";

    for (int i = 0; i <= 4; i++)
    {
        std::cout << i << "\t\t\t" << i*i*6 << "\t\t\t" << i*i*i << "\t\t\t";
        std::cout << std::endl;
    }
}