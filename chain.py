from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    # 해시를 구성하는 노드
    def __init__(self, key : Any, value: Any, next: Node) -> None:
        # 초기화
        self.key = key
        self.value = value
        self.next = next # 뒤쪽 노드를 참조

class ChainedHash :
    # 체인법으로 해시 클래스 구현
    def __init__(self, capacity : int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def hash_value(self, key : Any) -> int:
        # 해시값을 구하는 함수.
        if isinstance(key, int) :
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity) # int가 아닐 시

    def search(self, key : Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash] # head node p는 node이다.

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        # 검색 실패 
        return None

    def add(self, key: Any, value : Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash] # head node p는 node이다.
        
        while p is not None:
            if p.key == key:
                return False # 추가 실패 동일 원소가 존재하기 때문
            p = p.next
        
        temp = Node(key, value, self.table[hash]) # 새롭게 들어오는 원소가 head node
        self.table[hash] = temp # 동문 3번째 자리는 next node이다.
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key) # 삭제할 key의 해시값
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None: # 처음에 바로 발견
                    self.table[hash] = p.next
                else : # ~first
                    pp.next = p.next
                return True
            pp = p # 다음 노드 주목
            p = p.next # 뒤 쪽 노드 조지기
        
        return False
    
    def dump(self) -> None :
        # 원소 출력 함수
        for i in range(self.capacity) :
            p = self.table[i]
            print(i, end='')
            while p is not None :
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()
