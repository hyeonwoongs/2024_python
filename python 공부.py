jumin = "010606-3234567"

print("성별 : " + jumin[7])
print('연 : ' + jumin[0:2]) # 0번째부터 2번째 직전까지
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6번째 직전까지
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 끝 수는 -1번째로 볼 수 있다