'''
() 괄호식 맞는지 판단하기

우리는 수학을 모두 공부했습니다. 이때 () 괄호를 모두 기억하실 거에요. 이 괄호는 어떤 계산을 다른 계산보다 앞서게 할 때 썼던 것으로 기억합니다. 이때 괄호는 여는 괄호(()와 닫는 괄호())가 순서가 맞아야 해요.

예를 들어서 ()()(), ((())), (())() 등은 맞는 괄호에요.
반대로 ((, ), ))((, )(, ())( 등은 틀린 괄호에요. 그렇죠?

이것을 가지고 문제를 풀어봅니다.


문제: 괄호식을 입력받아 이 괄호식이 옳은 형태의 괄호식인지 검증하라

:입력: str | (와 )로 구성된 문자열. 길이는 0 이상. (ex: (())()())
:출력: bool | 입력 문자열이 올바른 괄호인지 아닌지의 여부. (ex: True)
:조건:

입력에는 () 이외의 그 어떤 글자도 들어오지 않는다.
'''

# Initial Code
def is_right_parenthesis(brackets):
    if len(brackets) % 2 != 0:
        return False
    elif brackets[0] == ')':
        return False

    stack = []

    for bracket in brackets:
        if bracket == '(':
            stack.append('(')
        elif bracket == ')':
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                return False

    if not stack:
        return True
    else:
        return False


print(is_right_parenthesis('()()()'))
print(is_right_parenthesis('((()))'))
print(is_right_parenthesis('(())()'))
print(is_right_parenthesis('(('))
print(is_right_parenthesis('))(('))
print(is_right_parenthesis(')('))
print(is_right_parenthesis('())('))

# REVIEW
# 1. 알고리즘을 풀 때 제일 곤란하게 하는 게 임계값 같은 것에 대한 풀이에요. 문제를 제대로 이해해야 한다는 게 이런거에요. 분명 입력에서는 길이가 0 이상이라고 했거든요. 그러면 4번째 검증식에서 인덱스 에러가 나겠죠. 기억해주세요. 문제의 설명, 제시된 입력. 출력의 크기와 조건 등은 확실하게 파악해주세요.
# 2. 20~23번째 줄은 다음과 같이 한 줄로 할 수도 있죠: return not stack 무조건 이게 더 좋은 방법이니 다음엔 저런 반환을 회피해주세요!

# Modified Code
def is_right_parenthesis_modified(brackets):
    if len(brackets) == 0:
        return True
    elif len(brackets) % 2 != 0:
        return False
    elif brackets[0] == ')':
        return False

    stack = []

    for bracket in brackets:
        if bracket == '(':
            stack.append('(')
        elif bracket == ')':
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                return False

    return not stack


print(is_right_parenthesis_modified('()()()'))
print(is_right_parenthesis_modified('((()))'))
print(is_right_parenthesis_modified('(())()'))
print(is_right_parenthesis_modified('(('))
print(is_right_parenthesis_modified('))(('))
print(is_right_parenthesis_modified(')('))
print(is_right_parenthesis_modified('())('))
print(is_right_parenthesis_modified(''))