"""
클래스 내부의 변수를 외부에서 사용 하는 것을 막고 싶을 때 인스턴스 변수 이름을 __변수이름 형태로 선언합니다 이것을 프라이빗 변수라고 합니다.
게터와 세터는 프라이빗 변수의 값을 추출하거나 변경할 목적으로, 간접적으로 속성에 접근하도록 해주는 함수입니다.
get_radius(), set_radius()로 만들어서 사용합니다.
데코레이터를 사용하면 게터 세터를 더 쉽게 만들어서 사용할 수 있습니다.
@property와 @변수이름.setter 로 선언하여 사용합니다.
"""
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius #프라이빗 변수 사용
    def get_circumference(self): #둘레 구하기
        return 2 * math.pi * self.__radius
    def get_area(self): #넒이 구하기
        return math.pi * (self.__radius ** 2)
    #게터와 세터 선언
    
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        if value <= 0:
            raise Exception("양의 숫자여야 합니다.")
        self.__radius = value
        
    #데코레이터 사용 게터와 세터
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise Exception("양의 숫자여야 합니다.")
        self.__radius = value
    
        
circle = Circle(10)
print("원의 둘레와 넒이를 구합니다.")
print("원의 둘례: ", circle.get_circumference())
print("원의 넒이: ", circle.get_area())
print("원의 반지름: ", circle.get_radius())
#circle.set_radius(-2)
print("--데코레이터를 사용한 게터와 세터--")
print("원의 반지름: ", circle.radius)
circle.radius = 5
print("변경된 반지름: ", circle.radius)
circle.radius = -2