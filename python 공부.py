python = "Python is Amazing"
print(python.lower()) # 소문자로
print(python.upper()) # 대문자로
print(python[0].isupper()) # 0번쨰 자리 대문자 맞냐?
print(len(python)) # 길이
print(python.replace("Python", "Java")) # 대체

index = python.index("n") # n이 몇번째 자리에 있느냐
print(index)
index = python.index("n", index + 1) # index에서 찾은자리 + 1 자리부터 시작
print(index)

print(python.find("n")) # n이 몇번째 자리에 있느냐
print(python.find("Java")) # find는 내가 원하는 값이 없을 떄 -1을 반환
print(python.index("Java")) # index는 내가 원하는 값이 없을 떄 error 발생, 뒤에 것 진행 못함
print("hi")

print(python.count("n")) # n이 몇 번 등장하느냐