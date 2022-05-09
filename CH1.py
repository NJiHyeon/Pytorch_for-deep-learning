#0.module불러오기
import torch
import torch.nn as nn
import torchvision
from torchvision import transforms
import numpy as np
from scipy.optimize import linear_sum_assignment as linear_assignment
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

#1.여러가지 torch의 형태
#1.1
torch.empty(5,4)
torch.ones(3,3)
torch.rand(5,6)     #random function
#1.2
l = [13,4]
r = np.array([4,56,7])
torch.tensor(l)     #transformation tensor
torch.tensor(r)
#1.3
x.size()
type(x)

#2.tensor의 연산
x = torch.rand(2,2)
y = torch.rand(2,2)
print(x)
print(y)
x + y
torch.add(x,y)
y.add(x)     #y에 x를 더하는 함수
y   
y.add_(x)   #y에 x를 더하는 함수(단,y가 바뀌어 있어 변수를 대체하고자 할 때 사용)
y

#3.행,열 표현
y[1,1]

#4.함수 view
x = torch.rand(8,8)
print(x)
x.view(64)
x.view(4,16)
x.view(-1,16) #64에서 16을 나누고 나머지 값이 자동으로 -1에 들어감(자주사용)
##CNN의 경우 convolution연산을 하다가 마지막에 layer을 정사각형 이미지를 일렬로 펴줄 때

#5.tensor에서 numpy로
y = x.numpy()
print(y)
type(y)

#6.x안의 값을 뽑아내고 싶을 때
x = torch.ones(1)   #단, 스칼라 형태(원소1개)
print(x)
x.item()
#(1)tensor안의 값을 숫자 형태로 불러오고 싶을 때 사용
#(2)loss function을 사용할 때 loss값이 스칼라 값으로 나오는데 직접 이 값을 뽑아내고 싶을 때