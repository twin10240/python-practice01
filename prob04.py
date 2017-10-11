# 다음과 같은 테스트에서 모든 태그를 제외한 텍스트만 출력하세요.
from builtins import print

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tolls int the world.
        </p>
    </body>
</html>"""
l = s.split('>')

#for i in range(len(l)):
#    if l[i].find('<'):
#        l[i] = ''

print(l)

