#Hash Table
---
### 해시테이블이란?
- 효율적인 탐색을 위한 자료구조를 말한다.
- key를 value에 대응시켜 표현한다.

### hash function 

- 키와 값을 해시 테이블에 넣게 되면 해시 함수가 키를 정수값으로 대응시킨다. (이 정수값이 인덱스로 쓰임) 데이터는 해당 인덱스에 저장된다.
- 모든 가능한 키에 대해서 해시 함수가 계산해 내는 정수값이 유일해야한다.
- 중복방지(chain hashing) : hash[key]에 저장하는 대신 hash[key]%arr_length 위치에 연결리스트 형태로 저장할 수도 있다.

### 기능
Insert - 해시 인덱스를 계산하고 그 위치로 가서 삽입
Delete - 해시 인덱스를 계산하고 그 위치의 연결 리스트를 탐색해서 값을 찾으면 제거

### C++ 구현


---
### 참고링크
https://www.geeksforgeeks.org/c-program-hashing-chaining/
