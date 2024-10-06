# IndexError: list index out of range
리스트나 문자열에서 인덱스를 벗어난 접근을 시도할 때 발생하는 IndexError를 방지하기 위한 방법은 매우 중요합니다. 특히, 특정 인덱스 이후의 요소를 비교하거나 접근할 때 미리 범위를 확인하는 습관이 필요합니다. 이 방법에서는 조건문으로 범위 확인하는 방식을 사용하여 IndexError를 방지하는 방법을 쉽게 설명합니다.


**문자열 리스트 예시**
```python
my_list = ["apple", "banana", "cherry", "date"]
```

## 방법 1: 조건문으로 범위 확인
if문을 사용해서 인덱스가 범위를 넘지 않는지 먼저 확인한 후, 그 다음에 비교를 수행할 수 있습니다.

```python
# 문자열 리스트 예시
my_list = ["apple", "banana", "cherry", "date"]

# 각 단어의 마지막 문자와 그 다음 문자의 아스키 코드를 비교
for word in my_list:
    word_len = len(word) - 1  # 마지막 문자의 인덱스
    
    # 마지막 인덱스가 리스트 길이 내에 있는지 확인
    if word_len + 1 < len(word):
        # 아스키 코드 비교
        if ord(word[word_len]) < ord(word[word_len + 1]):
            print(f"{word}: 마지막 문자 {word[word_len]}가 {word[word_len + 1]}보다 작습니다.")
        else:
            print(f"{word}: 마지막 문자 {word[word_len]}가 {word[word_len + 1]}보다 크거나 같습니다.")
    else:
        print(f"{word}: 마지막 문자 {word[word_len]} 이후에 비교할 문자가 없습니다.")
```

<br>

## 방법 2: 리스트 슬라이싱을 활용한 접근
파이썬에서는 인덱스를 벗어난 슬라이싱을 사용하면 에러가 발생하지 않고 빈 값을 반환하는 특성이 있습니다. 이를 이용하면 인덱스 범위 오류를 피할 수 있습니다.

```python
# 문자열 리스트 예시
my_list = ["apple", "banana", "cherry", "date"]

# 각 단어의 마지막 문자와 그 다음 문자의 아스키 코드를 비교
for word in my_list:
    word_len = len(word) - 1  # 마지막 문자의 인덱스

    # 슬라이싱으로 마지막 문자 다음 문자 가져오기 (범위 벗어나면 빈 문자열 반환)
    next_char = word[word_len + 1:word_len + 2]

    # 다음 문자가 있는 경우에만 비교
    if next_char:
        # 아스키 코드 비교
        if ord(word[word_len]) < ord(next_char):
            print(f"{word}: 마지막 문자 {word[word_len]}가 {next_char}보다 작습니다.")
        else:
            print(f"{word}: 마지막 문자 {word[word_len]}가 {next_char}보다 크거나 같습니다.")
    else:
        print(f"{word}: 마지막 문자 {word[word_len]} 이후에 비교할 문자가 없습니다.")
```