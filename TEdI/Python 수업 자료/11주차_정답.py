# 연습문제
class Calculate :
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    def __str__(self) :
        return 'add 함수 사용해서 더할 수 있습니다'

    def add(self):
        return self.a + self.b


