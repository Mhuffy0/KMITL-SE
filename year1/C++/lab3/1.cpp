#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<vector<char>> keypad = {
    {'-'},
    {'-'},
    {'a', 'b', 'c'},
    {'d', 'e', 'f'},
    {'g', 'h', 'i'},
    {'j', 'k', 'l'},
    {'m', 'n', 'o'},
    {'p', 'q', 'r', 's'},
    {'t', 'u', 'v'},
    {'w', 'x', 'y', 'z'}
};

int main() {
    string digits ;
    cout << "Enter Digits" << endl;
    cin >> digits;

    vector<string> comb = {""};

    //loop
    for(char c : digits){
        vector<string> Temp;

        for (string current : comb) {
            int index = c - '0';

            for (char letter : keypad[index]) {
                Temp.push_back(current + letter);
            }
        }
        comb = Temp;
    };
    
    int counter = 0;
    for (const string combo : comb) {
        cout << ++counter << ") " << combo << endl;
    }
}