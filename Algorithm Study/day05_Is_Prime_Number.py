'''
양의 정수의 소수 여부 판별하기
아시다시피 소수(prime number)는 1과 자기 자신 이외에 약수를 갖지 않는 양의 정수를 말합니다. 소수와 관련한 문제는 알고리즘을 풀게 되면 반드시 마주치게 되어 있습니다. 특히 가장 간단한 판별방법은 알고리즘을 공부하는 초반에 반드시 한 번 다루고 넘어갑니다. 우리도 예외일 수는 없을 것 같아요.


문제: 입력 받은 숫자가 소수인지 판단하라

:입력: int | 판단할 정수. 크기는 1 이상, 10000 이하
:출력: bool | 입력 받은 정수가 소수인지의 여부
:조건:

1은 원칙상 소수가 아닙니다. 참고하세요!
'''
import math 

def is_prime(n):
	if n == 1:
		return False

	for i in range(2, int(math.sqrt(n))):
		if n % i == 0:
			return False
	return True 

print(is_prime(1))
print(is_prime(2))
print(is_prime(127))
print(is_prime(131))
print(is_prime(222))
print(is_prime(10000))
