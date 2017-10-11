# 키보드에서 5개의 정수를 입력 받고 평균을 구하는 프로그램을 작성하시오

l = []

# append 리스트에 바로 값이 들어가고 input이 바로 int로 형변환이 가능
for i in range(5):
    l.append(int(input()))

print(sum(l) / 5)
