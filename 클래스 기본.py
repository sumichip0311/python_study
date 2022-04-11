"""
추상화: 복잡한 자료, 모듈, 시스템 등에서 핵심적인 개념 혹은 기능을 간추려 내는 것을 의미
객체: 속성을 가질 수 있는 모든 것을 의미
클래스: 객체를 쉽고 편리하게 생성하기 위해 만들어진 구문    ex) 붕어빵 틀
인스턴스: 클래스를 기반으로 생성한 객체를 의미            ex) 틀로 만든 붕어빵
생성자: 클래스 이름과 같은 인스턴스를 생성할 때 만드는 함수
메소드: 클래스가 가진 함수를 의미
class 클래스 이름:
    def 메소드 이름(self, 추가적인 매개변수):
        pass
클래스 내부의 함수는 첫 번쨰 매개변수로 반드시 self를 입력해야 합니다.
self는 자기 자신을 나타내는 딕셔너리입니다. 
self가 가지고 있는 속성과 기능에 접근할 때는 self.<식별자> 형태로 접근합니다.
"""
#클래스를 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
#학생 리스트를 선언
students = [
    Student("박민규", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]
#학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    #출력합니다.
    print(student.to_string())