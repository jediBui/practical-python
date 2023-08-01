# bounce.py
#
# Exercise 1.5
Height = 100 # 100 meters
#rebound = .60 # 3/5 = 60% = .6
#bounceLimit = 10
bounceCount = 1

while bounceCount <= 10:
    Height = (Height * 3/5)
    print (bounceCount, round(Height, 1))
    bounceCount += 1
