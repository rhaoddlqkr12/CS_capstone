import math

temp = int(input("현재 온도는 몇도(°C) 입니까? : "))
wind = float(input("그렇다면 현재 풍속(m/s)은 몇입니까? : "))
wind = wind * 3600 / 1000


result= float(13.12 + (0.6215 * temp) - (11.37*(pow(wind, 0.16))) + (0.3965 * temp * pow(wind, 0.16)))


print("정확한 체감 온도는 "+str(result)+ "°C 이며")
result=round(result)
print("대략적인 현재 체감온도는 섭씨" +str(result)+"°C 입니다.")
              
