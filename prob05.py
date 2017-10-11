# 다음 문자열을 모든 대문자를 소문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 각 단어를 순서대로 출력하세요.

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

# 대문자 -> 소문자
s = s.lower()

# 특수문자 없애기
s = s.replace(',', '').replace('.', '').replace('\n', '')

l = list(set(s.split(' ')))

for i in range(len(l)):
    print(l[i])


