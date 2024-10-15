# 일반 배열
arr = [10, 20, 30, 40, 50]

print("배열[2]의 값 : ", arr[2])

print("")

# 연결리스트 빠짐

print("")

# 스택
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("마지막을 꺼냄", stack.pop())
print("남은 배열 값", stack)

print("")

# 큐
from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print("맨 앞을 꺼낸다", queue.popleft())
print("남은 큐", queue)


# 해시맵
hash_map = {}
hash_map['name'] = 'alice'
hash_map['age'] = 25
hash_map['job'] = 'Engineer'

print("해시맵 네임은 ", hash_map['name'])
print("해시맵 잡은 ", hash_map.get('job'))