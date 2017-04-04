# data analysis 절차 지향적인 방법
# 평균, 분산 함수를 작성
from functools import reduce
import math #sqrt
import pickle


def average(scores) :#scores = [점수1, 점수2...]
    return reduce(lambda a, b: a + b, scores) / len(scores)
    
def variance(scores, arvg): #scores = [점수1....] avrg : 50,  sum((각 점수 - 평균)**2) / 데이터의 개수)
    return reduce(lambda a, b: (a + b), map(lambda s:(s-avrg)**2, scores))/len(scores)

def evaluateClass(avrg, std_dev):
    if avrg < 50 and std_dev > 20:
        print ("성적저조 편차 큼")
    elif avrg < 50 and std_dev < 20:
        print ("성적저조하고 편차 없음")
    elif avrg > 50 and std_dev > 20:
        print ("성적 우수 편차 큼")
    else :
        print ("성적우수하며 편차 적음")
f = open("class_A.bin","rb")

items = []
while True:
    try:
        items.append(pickle.load(f))
    except EOFError:
        break
f.close()
print(items)

scores = []
for i in items:
    for item in i.values():
        scores.append(item)
#sc2 = []
#for i in items:
#    sc2 = sc2 + list(map(lambda x: x, i.values()))
#print(scores)
#print(sc2)
avrg = average(scores)
vari = round(variance(scores,avrg),1)
std_dev = round(math.sqrt(vari),1)
print("평균: {0}, 분산: {1}, 표준편차 {2}".format(avrg, vari, std_dev))
evaluateClass(avrg,std_dev)