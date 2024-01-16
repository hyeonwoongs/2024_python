# 애완동물을 소개해 주세요~
print("우리집 강아지의 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? False")

animal = "강아지"
name = "연탄이"
age = 4 # 숫자열 자료형은 "혹은 ' 필요 없음
hobby = "산책"
is_adult = age >= 3 # 변수를 먼저 적어놓고 출력

print("우리집 " + animal + "의 이름은 연탄이예요") # 변수는 "을 써주고 +을 앞뒤로 쓴다
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # 처음과 끝은 +와"을 쓰지 않아도 된다
print(name + "는 어른일까요? " + str(is_adult)) # boolean과 정수형은 str로 감싸줘야 문자형으로 바꿀 수 있다

# + 대신 ,을 써도 된다. 그리고 ,는 띄어쓰기 한칸이 포함됨. 이떄는 정수형과 boolean을 str로 감싸지 않아도 된다.

print("우리집 " , animal , "의 이름은 연탄이예요")
print(name , "는 " ,(age) , "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))