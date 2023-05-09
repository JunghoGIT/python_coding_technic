from functools import wraps
from datetime import datetime

# functools wraps 미사용
def 로그_데코레이터(함수):
    def 감싸는함수(*위치인자, **키원드인자):
        """
        wrapper 함수임
        """
        결과 = 함수(*위치인자, **키원드인자)
        로그 = f"{datetime.now()} | {함수.__name__} 실행"
        return 결과
    return 감싸는함수

@로그_데코레이터
def 최대공약수(x, y):
    """
    유클리드 호제법으로 최대공약수를 구해줌돠
    """
    if x % y == 0:
        return y
    elif y == 0:
        return x
    return 최대공약수(y, x%y)

print(최대공약수)
# 실행 결과 <function 로그_데코레이터.<locals>.감싸는함수 at 0x102dd9000>
print(최대공약수.__doc__)
# 실행 결과 Help on function 감싸는함수 in module __main__:
# 실행 결과 wrapper 함수임

# 데코레이터를 통해 실제 로직이 실행되는 함수가 아닌 랩퍼 함수가 반환 됨으로 랩퍼 함수의 메타 데이터가 저장됨
# 이로인해 코드 추적이 어렵고 실행하고자 하는 함수의 메타 데이터를 사용할 수 없음 

# functools wraps 미사용
def 로그_데코레이터_2(함수):
    @wraps(함수)
    def 감싸는함수(*위치인자, **키원드인자):
        """
        wrapper 함수임
        """
        결과 = 함수(*위치인자, **키원드인자)
        로그 = f"{datetime.now()} | {함수.__name__} 실행"
        return 결과
    return 감싸는함수

@로그_데코레이터_2
def 최대공약수_2(x, y):
    """
    유클리드 호제법으로 최대공약수를 구해줌돠
    """
    if x % y == 0:
        return y
    elif y == 0:
        return x
    return 최대공약수(y, x%y)

print(최대공약수_2)
# 실행 결과 <function 로그_데코레이터.<locals>.감싸는함수 at 0x102dd9000>
print(최대공약수_2.__doc__)
# 실행 결과 Help on function 감싸는함수 in module __main__:
# 실행 결과 유클리드 호제법으로 최대공약수를 구해줌돠