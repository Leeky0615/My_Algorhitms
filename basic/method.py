'''
    조건문 간소화
'''

score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

# 조건부내에서 부등식을 사용할 때 수학의 부등식을 그래도 사용 가능
x = 14
if 0 < x < 20:
    print("x는 0이상 20미만의 수입니다")

'''
    반복문
    while문 보다 for문을 사용할때 코드가 더 간결하다.
'''
# continue 키워드 : 남은 코드의 실행을 건너뛰고 다음 반복을 실행할때
result = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue  # i의 값이 짝수일 때는 그냥 넘긴다.
    result += i

print(result)

# 예제
scores = [90, 85, 77, 65, 97]
cheating = {2, 4}
for i in range(5):
    if i + 1 in cheating:
        print(i + 1, "번 학생은 실격입니다.")
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 이중 for문
# for i in range(2, 10):
#     for j in range(1,10):
#         print(i, "X", j, "=", i*j)
#     print()


'''
    함수 & 람다표현식
    함수 : 특정한 작업을 하나의 단위로 묶어 놓은 것.
'''


# 해당 함수에서 지역변수를 만들지 않고 함수 바깥에 선언된 변수를 바로 참조 : global
def confirm(score):
    # global scores
    array = list()
    for i in scores:
        if i >= score:
            array.append(i)

    return array


print(confirm(80))


# 파이썬에서는 여러개의 return값을 가질 수 있다.
def operator(a, b):
    add_var = a + b
    minus_var = a - b
    return add_var, minus_var


a, b = operator(5, 6)
print(a, b)

'''
    람다표현식을 이용하면 함수를 간단하게 작성할 수 있다.
    이름없는 함수라고 불리기도 한다.
'''
print("람다표현식을 사용한 더하기 함수 : ", (lambda a, b: a + b)(3, 8))

# 많이 사용되는 람다 표현식
array = [('a', 40), ('bas', 32), ('c', 23)]
arr = ['asd','sd','wqwds']

def my_key(x):
    return x[1]
arr.sort(reverse=True, key=lambda  x: len(x))
print(arr)
print(sorted(array, key=lambda x: x[1]))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a+b, list1, list2)

print(list(result))