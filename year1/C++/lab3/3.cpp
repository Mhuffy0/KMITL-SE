#include <iostream> 
#include <list> 

using namespace std;

void merge(list<int> a, list<int> b){
    list<int> output;
    while (a.size() != 0 && b.size() != 0) {
        if (a.front() < b.front()) {
            output.push_back(a.front());
            a.pop_front();
        }
        else {
            output.push_back(b.front());
            b.pop_front();
        }
    }
    if (!a.empty()) {
        output.push_back(a.front());
    }
    else {
        output.push_back(b.front());
    }

    for (int i : output) {
        cout << i ;
    }
}


int main() {
    list<int> list1 = {1,3,5,7}; 
    list<int> list2 = {2,4,6,8}; 

    merge(list1, list2);
}