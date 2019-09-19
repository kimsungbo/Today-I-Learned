'''
Caesar Cipher

평문(plain text)을 적이 알아볼 수 없는 암호(cipher)로 만드는 암호학은 현재 우리 삶에 지대한 영향을 미치고 있어요.
그중 오랜 역사를 가지고 있는 카이사르 암호가 있습니다. 이 암호는 평문을 다음과 같이 바꿔요:

caesar example


이번 문제에서는 영어 소문자만 염두에 둡니다. 카이사르 암호는 만들기 매우 간단한데요.
'a' -> 'd', 'b' -> 'e'와 같이 소문자에서 위치를 3씩 오른쪽으로 옮기면 됩니다.
이때 오른쪽 끝에 있는 'xyz'에 대해서는 'x' -> 'a', 'y' -> 'b', 'z' -> 'c'와 같이 회전하면 됩니다.


문제: 문자열을 입력받아 카이사르 암호를 만들어라.

:입력: str | 영어 소문자 문자열. 크기는 0 이상. (ex: word)
:출력: str | 각 글자를 오른쪽으로 3씩 옮긴 암호. (ex: zrug)
:조건:

입력에는 영어 소문자 이외의 글자는 들어오지 않는다. 예를 들어 대문자, 한글, 공백문자 등.
'''

# First Commit
def caesar_cipher(str):
    cipher = ''
    for c in str:
        if c == 'x' or c == 'y' or c == 'z':
            cipher += chr(ord(c) - 23)
        else:
            cipher += chr(ord(c) + 3)
    return cipher


print(caesar_cipher('word'))
print(caesar_cipher('xyz'))

# REVIEW
# 1. 4번째 줄은 파이썬으로 이렇게 할 수 있어요: c in 'xyz'
# 2. 일단 답은 나오는데 직접 23을 빼는 방식은 좋지 않아요 사실. 23을 하드코딩했는데 제 3자는 결코 이해할 수 없을 거에요. 저게 무슨 뜻인지. 23가지의 인격 뭐 그런걸까요? 저 방식의 단점은 일단 옮기는 횟수가 3번이 아니라 계속 변한다고 문제 상황이 바뀌면 전혀 대응이 안 된다는 거에요. 이런 상황에서 대표적인 방법은 나머지 연산을 활용하는 거에요. 그러면 범위를 넘기는지 따로 검증을 안 해도 돼요.

# Modified Code
def caesar_cipher_modified(str):
	cipher = ''
	alphabets = 'abcdefghijklmnopqrstuvwxyz'

	for c in str:
		cipher = cipher + alphabets[(alphabets.find(c) + 3) % 26]

	return cipher 


print(caesar_cipher_modified('word'))
print(caesar_cipher_modified('xyz'))
