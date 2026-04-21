## 공부하다가 헷갈렸던 개념 및 기억할 내용들
---
switch(객체){
    case 값:
      실행문;
      break;
}
if문보다 빠르고 비슷한 역할을 한다.
단 각각의 케이스가 확실해야한다.
만약 실행문이 return이라면 break는 생략 가능하다.
또한 예외처리를 위해 마지막에 default를 사용해주면 좋다.

### 예시
```
switch(weight){
    case 100:
      cout << "Try cutting";
      break;
    case 80:
      cout << "Good!";
      break;
    default:
      cout << "Input value is number";
}
switch(op){
    case '+': return val1 + val2;
    case '-': return val1 - val2;
    case '*': return val1 * val2;
    case '/': return val1 / val2;
    default: cout << "invalid operator";
}
```

---

uint32_t는 32bit의 부호 없는 정수를 뜻함.
크기가 고정돼 있다는 점이 장점으로 데이터 크기가 정확해야 하는 상황에서 쓰기 좋다.
임베디드 시스템이나 네트워크 등 정교한 작업에 사용하기 용이하다.

---

find(start, end, target)

include <algorithm>이 필요하다.
변수 타입은 auto로 받아오는게 좋다.(타입 자체가 일반적으로 사용하는 타입이 아님)
`ex) auto point = find(haystack.begin(), haystack.end(), "needle");`
이 경우 자동으로 타입을 지정해준다. 
인덱스 위치를 구하고 싶을 땐 연산을 하면 된다.
`ex) to_string(point - haystack.begin()); // 정수형으로 바꾼 후 문자열로 변환한다.
찾지 못했을 경우 end() 즉 범위 밖을 반환한다. 따라서 if(point == haystack.end()){cout <<"not found"}처럼 미리 처리하면 좋다.

---

벡터의 합 구하기

accumulate(start, end, init);
vector속 원소의 값을 처음부터 끝까지 더한다.
이 때 init은 초기값이다.
쉽게 생각하면 start_num += vector[i] 같은 느낌이다.

include <numeric>이 필요하다.
ex) accumulate(numbers.begin(), numbers.end(), 0);

---

최대 최소 구하기

max_element(start, end);
min_element(start, end);
vector속 원소중 최대, 최소값의 iterator를 반환한다.
이 때 기본적으로 반환하는 값은 iterator이기에.
*max_element(start, end);, *min_element(start, end); 처럼 바로 참조해 값을 받아올 수 있다.
참조 없이 사용할 경우 위와 마찬가지로 타입을 auto로 받아오는 게 좋다.

ex1)
  int volume = numbers.size();
  int sigma = accumulate(numbers.begin(), numbers.end(), 0);
  
  auto max_val = max_element(numbers.begin(), numbers.end());
  auto min_val = min_element(numbers.begin(), numbers.end());

  return sigma - *max_val - *min_val;

ex2)
  int volume = numbers.size();
  int sigma = accumulate(numbers.begin(), numbers.end(), 0);
  
  int max_val = *max_element(numbers.begin(), numbers.end());
  int min_val = *min_element(numbers.begin(), numbers.end());

  return sigma - max_val - min_val;