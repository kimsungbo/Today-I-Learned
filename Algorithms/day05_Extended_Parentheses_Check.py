'''

Extended Parenthesis Check

지난번 3번 문제가 ()를 활용한 괄호식이 옳은 형태의 괄호식인지 검증하는 문제였습니다. 하지만 수학에서 범위를 한정하는 수식 기호는 ()가 다가 아니죠. {}와 []도 존재합니다.

가령 (}는 틀린 괄호식입니다. 말씀 안 드려도 당연히 아실 거라고 생각해요. 이번엔 이들까지 사용한 확장된 괄호식을 검증해봅시다.

이 문제를 조금만 더 확장하고 노력하면 간단한 사칙연산을 지원하는 계산기를 만들 수 있어요. 정말 많이 온 겁니다. 같이 화이팅!!


문제: 괄호식을 입력받아 이 괄호식이 옳은 형태의 괄호식인지 검증하라

:입력: str | (){}[]을 사용한 문자열. 길이는 0 이상. (ex: (}(])
:출력: bool | 입력 문자열이 올바른 괄호인지 아닌지의 여부. (ex: False)
:조건:

입력에는 (){}[] 이외의 그 어떤 글자도 들어오지 않는다.

'''
open_brackets = ['{', '[', '(']
close_brackets = ['}', ']', ')']

def is_right_parentheses(brackets):


	if len(brackets) % 2 != 0:
		return False
	elif len(brackets) == 0:
		return True
	elif brackets[0] == ')':
		return False

	stack = []

	for bracket in brackets:
		if bracket in open_brackets:
			stack.append(bracket)
		elif bracket in close_brackets:
			if not stack:
				return False
			elif stack[-1] == open_brackets[close_brackets.index(bracket)]:
				stack.pop()
			else:
				return False

	return not stack

print(is_right_parentheses('(}(]'))
print(is_right_parentheses(''))
print(is_right_parentheses('(){}[]'))


