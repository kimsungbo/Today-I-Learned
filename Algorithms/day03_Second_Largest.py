'''

Intro: 정수 배열에서 두 번째로 큰 값 찾기
파이썬에서 정수 배열의 최대값을 찾는 것은 매우 쉽습니다. max 함수를 사용하면 됩니다.
하지만 가령 두 번째 값이라면 어떨까요? 우리 2등도 기억해주자구요.


문제: 정수 배열에서 두 번째로 큰 값을 반환하라

:입력: list of int | 정수 배열. 크기는 2 이상. (ex: [6, 5, 2, 1, 100, 3, 1, 59])
:출력: int | 정수 배열의 2번째로 큰 정수. (ex: 59)
:조건:

list.sort() 함수를 쓰지 않는다. 이걸 쓰면 너무 쉽죠 사실...
만약 최대값이 두 개 이상이면, 정답은 그것보다 작아야 한다.(ex: function([2, 2, 2, 1]) --> 1)
만약 배열 내 모든 값이 똑같다면 두 번째 큰 값은 없기 때문에 'equality'라는 문자열을 출력한다.

'''
# Initial Code
def second_largest(numbers):
    list_max = max(numbers)
    list_min = min(numbers)
    second_largest = list_min

    for n in numbers:
        if n != list_max and n > second_largest:
            second_largest = n
    return second_largest


print(second_largest([1, 2, 3, 4, 5]))
print(second_largest([2, 2, 2, 1]))

# REVIEW
# 1. Redundant steps can be removed
# 2. 만약 입력의 배열이 모두 같은 값을 같고 있다면, 두 번째 값은 없기 때문에 'equality'라는 문자열을 반환하라고 했거든요. 기억해주세요. 문제를 제대로 이해하지 못하면 문제를 해결할 수 없어요. 

from numpy import unique

def second_largest_modified(numbers):

    list_max = max(numbers)
    list_min = min(numbers)
    second_largest = list_min

    if len(unique(numbers)) == 1:
    	return 'equality'

    for n in numbers:
        if n != list_max and n > second_largest:
            second_largest = n
            
    return second_largest


print(second_largest_modified([1, 2, 3, 4, 5]))
print(second_largest_modified([2, 2, 2, 1]))
print(second_largest_modified([2, 2, 2, 2]))