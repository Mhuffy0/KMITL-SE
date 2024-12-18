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

vector<string> rec(string num, vector<string> data = {""}){
    int letter = num[0] - '0';
    vector<char> k = keypad[letter];
    vector<string> result;
    for (char x: k){
        for (string d: data){
            result.push_back(d+x);
        }
    }
    if (num.size() == 1){
        return result;
    }
    num.erase(0,1);
    return rec(num, result);
}

int main() {
    string digits ;
    cout << "Enter Digits" << endl;
    cin >> digits;
    vector<string> comb = rec(digits);

    int counter = 0;
    for (const string combo : comb) {
        cout << ++counter << ") " << combo << endl;
    }
}