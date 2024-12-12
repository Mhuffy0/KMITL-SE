#include <iostream>
#include <string>

int main()
{
    std::string name1, name2, p_name1, p_name2;

    std::cout << "Enter name 1 : " << std::endl;
    std::cin >> name1;
    std::cout << "Enter name 2 : " << std::endl;
    std::cin >> name2;


    for (int i = 0; i < name1.size() + name2.size(); i++) {
        std::cout << "*";
    }
    std::cout << "*****************************" << std::endl;

    std::cout << "*";
    for (int i = 0; i < 13 + name1.size(); i++)
    {
        std::cout << " ";
    }
    std::cout << "*";
    for (int i = 0; i < 13 + name2.size(); i++)
    {
        std::cout << " ";
    }
    std::cout << "*\n";

    std::cout << "* Player 1 : " << name1 << " * " << "Player 2 : " << name2 << " *" << std::endl;
    // std::cout << "* Player 2 : " << name2 << " *" << std::endl;

    std::cout << "*";
    for (int i = 0; i < 13 + name1.size(); i++)
    {
        std::cout << " ";
    }
    std::cout << "*";
    for (int i = 0; i < 13 + name2.size(); i++)
    {
        std::cout << " ";
    }
    std::cout << "*\n";


    for (int i = 0; i < name1.size() + name2.size(); i++) {
        std::cout << "*";
    }
    std::cout << "*****************************" << std::endl;

    //vertical
    std::cout << "Enter name 1 : " << std::endl;
    std::cin >> p_name1;
    std::cout << "Enter name 2 : " << std::endl;
    std::cin >> p_name2;
    int size_ver = 0;

    if (p_name1.size() > p_name2.size()) {
        size_ver = p_name1.size();
        for (int i = 0; i < size_ver; i++) 
        {
            std::cout << "*";
        }
        std::cout << "***************" << std::endl;

        //empty line
        std::cout << "*";
        for (int i = 0; i < 13 + p_name1.size(); i++)
        {
            std::cout << " ";
        }
        std::cout << "*\n";

        std::cout << "* Player 1 : " << p_name1 << " *" << std::endl;

        std::cout << "*";
        for (int i = 0; i < 13 + p_name1.size(); i++)
        {
            std::cout << " ";
        }
        std::cout << "*\n";

        for (int i = 0; i < size_ver; i++) 
        {
            std::cout << "*";
        }
        std::cout << "***************" << std::endl;

        std::cout << "*";
        for (int i = 0; i < 13 + p_name1.size(); i++)
        {
            std::cout << " ";
        }
        std::cout << "*\n";

        std::cout << "* Player 2 : " << p_name2;
        for (int i = 0; i < p_name1.size(); i++) 
        {
            std::cout << " ";
        }
        std::cout << "*" << std::endl;

        std::cout << "*";
        for (int i = 0; i < 13 + p_name1.size(); i++)
        {
            std::cout << " ";
        }
        std::cout << "*\n";

        for (int i = 0; i < size_ver; i++) 
        {
            std::cout << "*";
        }
        std::cout << "***************" << std::endl;
    }
    else {
        size_ver = p_name2.size();
        for (int i = 0; i < size_ver; i++) 
        {
            std::cout << "*";
        }
        std::cout << "***************" << std::endl;

        //empty line
        std::cout << "*";
        for (int i = 0; i < 13 + p_name2.size(); i++)
        {
            std::cout << " ";
        }
        std::cout << "*\n";

        std::cout << "* Player 2 : " << p_name2 << " *" << std::endl;

        std::cout << "*";
        for (int i = 0; i < 13 + p_name2.size(); i++)
        {
            std::cout << " ";
        }
        std::cout << "*\n";

        for (int i = 0; i < size_ver; i++) 
        {
            std::cout << "*";
        }
        std::cout << "***************" << std::endl;

        std::cout << "*";
        for (int i = 0; i < 13 + p_name2.size(); i++)
        {
            std::cout << " ";
        }
        std::cout << "*\n";

        std::cout << "* Player 1 : " << p_name1;
        for (int i = 0; i < p_name2.size() - p_name1.size(); i++) 
        {
            std::cout << " ";
        }
        std::cout << " *" << std::endl;


        std::cout << "*";
        for (int i = 0; i < 13 + p_name2.size(); i++)
        {
            std::cout << " ";
        }
        std::cout << "*\n";

        for (int i = 0; i < size_ver; i++) 
        {
            std::cout << "*";
        }
        std::cout << "***************" << std::endl;
    }
    return 0;
}