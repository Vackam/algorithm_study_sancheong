# For stack class
from typing import Any

class FixedStack:
    # 고정된 길이인 스택 클래스

    class Empty(Exception) :
        pass
    # 비어있는 순간
    class Full(Exception) :
        pass
    # 가득 찬 순간

    def __init__(self, capacity: int  = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0 # 검색할 때 쓰이는 포인터입니다.

    def __len__(self) -> int :
        return self.ptr # 지금 현재 스택의 데이터 개수 반환

    def is_empty(self) -> bool :
        return self.ptr <= 0 # bool형 자료이니 음양으로 판단. 비어있는지 확인

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        # 스택에 값을 넣는 작업
        if self.is_full() :
            raise FixedStack.Full # 스택이 가득 차 있을 때
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self) -> Any :
        # 꼭대기에서 끄내는 작업
        if self.is_empty() :
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any :
        # 꼭대기 밸류를 확인하는 작업
        if self.is_empty() :
            raise FixedStack.Full
        return self.stk[self.ptr -1]

    def clear(self) -> None:
        # 스택을 비운다.
        self.ptr = 0 # 스택을 의미적으로만 비운 것. 초기화랑 같다.

    def find(self, value: Any) -> Any :
        # 스택에서 밸류찾기 
        for i in range(self.ptr -1, -1, -1) :
            if self.stk[i] == value:
                return i
        return -1 # 없는 경우
         
    def count(self, value: Any) -> int:
        # 스택에 있는 값의 개수 반환
        c = 0
        for i in range(c, self.ptr, 1) :
            if self.stk[i] == value: # 검색에 성공했습니다.
                return i+1
        print('--존재하지 않음--')
        return 0
    
    def __contains__(self, value: Any) -> bool :
        return self.count(value) > 0 # 값이 존재하는지 찾아줍니다.
    
    def dump(self) -> None :
        # 꼭대기부터 스택 출력
        if self.is_empty() :
            print('스택이 비어있습니다')
        else: 
            print(self.stk[:self.ptr])