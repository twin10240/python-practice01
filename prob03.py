# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'

l = s.split('/')
l.remove('')
print(l)

# 디렉토리 경로명과 파일명을 분리하여 출력하세요.
print(s.rsplit('/', 1))
