'''
After 28 days..

대니 보일 감독, 킬리언 머피 주연의 영화 '28일 후'는 저는 정말 무서웠습니다. 제가 무서운 영화를 잘 못 봐요. 대체 무슨 깡으로 그건 보았는지 참...

이 영화의 결말도 다 못봤지만, 그럴 용기도 없었지만 저는 오늘로부터 28일 후가 오늘과 같은 요일이라는 것만은 알고 있었어요.

그러면 묻습니다. 오늘로부터 N일 뒤에는 무슨 요일일지...


문제: N일 뒤가 무슨 요일인지 맞혀라

:입력: int | 0 이상의 정수
:출력: bool | 입력 일 뒤의 요일을 '월화수목금토일' 중의 한 글자로 반환하라
:조건:

오늘이 무슨 요일인지에 대한 정보는 함수 실행에 맞게 동적으로 구한다. datetime 모듈 검색 요망

'''

from datetime import date
from datetime import timedelta
​
def the_day_after_n(n):
    today = date.today()
    weekdays = '월화수목금토일'
    after_n = today + timedelta(days=n)
    return '{}요일'.format(weekdays[after_n.weekday()])
