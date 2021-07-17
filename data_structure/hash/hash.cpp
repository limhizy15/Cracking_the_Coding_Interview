#include <iostream>
#include <list>
#include <functional>

using namespace std;

class Hash {
    int BUCKET; // 해시 테이블의 크기

    list<int> *table; // 연결리스트로 이루어진 해시 테이블 선언

    public:
    Hash(int V); //생성자. V = 크기

    void insertItem(int key);

    void deleteItem(int key);

    int hashFunction(int key) {
        return (key % BUCKET);
    }

    void displayHash();
};

// "::"은 범위 지정 연산자를 뜻한다.
// 예로 Hash::displayHash() -> Hash클래스 안 함수 접근

// 해시 테이블 생성부분 v는 크기
Hash::Hash(int v){
    this->BUCKET = v;
    table = new list<int>[BUCKET];
}

void Hash::insertItem(int key){
    int idx = hashFunction(key);
    table[idx].push_back(key);
}

void Hash::deleteItem(int key){
    // 해당 key에 대응하는 해시 인덱스를 받아옴 
    int idx = hashFunction(key);

    list <int> :: iterator it; //반복자 선언
    for (it = table[idx].begin(); it != table[idx].end(); it++) {
        if (*it == key) break;
    }

    // 원하는 키를 찾음
    if (it != table[idx].end())
        table[idx].erase(it);
}

void Hash::displayHash() {
    for (int i = 0; i < BUCKET; i++) {
        cout << i;
        for (auto x : table[i])
            cout << " --> " << x;
        cout << endl;
    }
}

int main() {
    int a[] = {12, 14, 8, 13, 8};
    int n = sizeof(a) / sizeof(a[0]);

    Hash h(7);

    for (int i = 0; i < n; i++){
        h.insertItem(a[i]);
    }

    h.deleteItem(8);

    h.displayHash();

    return 0;
}