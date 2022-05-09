#parameter를 업데이트 할 때마다 Descent method(Gradient descent method, Newton method etc)라는 
#어떤 미분값이 필요한 방법을 취하고 있기 때문에 미분계산 매우 중요
#미분 자동계산 방법과 원리
from importlib.metadata import requires
from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH
import torch
#(1)변수 선언(데이터 입력)
x = torch.ones(2,2, requires_grad=True)    #x에 관한 연산들을 모두 추적할 수 있게 해준다.
print(x)
#(2)모델 내 연산 예측값 산출
y = x + 1
print(y)
#(3)손실함수 계산
z = 2 * y ** 2
res = z.mean()
#(4)손실(loss) 산출
print(res)

##res를 기준으로 미분
