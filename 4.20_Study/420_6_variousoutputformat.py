print("{0: >10}".format(500))
print("{0: >+10}".format(500))

#양수일 때 + 로 표시, 음수일 때 - 로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0: <+10}".format(500))
print("{0: <10}".format(500))

#3자리마다 콤마 찍어주기
print("{0:,}".format(1000000000))
print("{0:+,}".format(1000000000))
print("{0:-,}".format(1000000000))
print("{0:^<+30,}".format(1000000000))

#소수점 출력
print("{0:f}".format(5/3))

#소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3))




