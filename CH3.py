#2. 같은 클래스 별 폴더 이미지 데이터 사용
#3. 개인 데이터 사용(2 types)

import torch
import torchvision
import torchvision.transforms as tr
from torch.utils.data import DataLoader, Dataset
import numpy as np

###torchvision.transforms는 데이터를 불러오면서 그 다음에 전처리를 바로 할 수 있게 해주는 라이브러리
###DataLoader는 배치 사이즈 형태로 만들어서 실제로 학습을 할 때 이용할 수 있는 형태를 만들어주는 라이브러리
###Dataset은 튜닝을 할 때 사용

#1. 파이토치 제공 데이터 불러오기
#(1)transform 정의
transf = tr.Compose([tr.Resize(8), tr.ToTensor()])
#Transforms on PIL Image
#종류 : Pad, Grayscale, RandomCrop, Normalize ..
#Transforms on torch.*Tensor - tensor image
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transf)
testset = torchvision.datasets.CIFAR10(root='./data', train=Flase, download=True, transform=transf)